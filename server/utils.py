import cv2
import json
import numpy as np
import base64
import pywt
import joblib

# Globals
__label_name_to_num = {}
__label_num_to_name = {}
__model = None

# Load our model and label dict
def load_artifacts():
    global __label_name_to_num
    global __label_num_to_name
    global __model

    with open('./artifacts/class_dict.json', 'r') as f:
        __label_name_to_num = json.load(f)
        __label_num_to_name = {val:key for key, val in __label_name_to_num.items()}

    if __model is None:
        with open('./artifacts/model.pkl', 'rb') as f:
            __model = joblib.load(f)

# get important features from the image
def wav_transform(image, mode='haar', level=1):
    im_array = image

    im_array = cv2.cvtColor(im_array, cv2.COLOR_BGR2GRAY)
    im_array = np.float32(im_array)
    im_array /= 255

    # get coefficients
    coeffs = pywt.wavedec2(im_array, mode, level=level)

    coeffs_h = list(coeffs)
    coeffs_h[0] *= 0

    # construct
    im_array_h = pywt.waverec2(coeffs_h, mode)
    im_array_h *= 255
    im_array_h = np.uint8(im_array_h)

    return im_array_h

# get the decoded version of the image
def get_cv2_img_from_b64(img_b64):
    encoded = img_b64.split(',')[1]
    np_arr = np.frombuffer(base64.b64decode(encoded), np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

# get the cropper image if possible
def get_cropped_img(img_b64, img_path):
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')

    # check if a file path or a base 64 encoded text was given
    if img_path:
        img = cv2.imread(img_path)
    else:
        img = get_cv2_img_from_b64(img_b64)

    # detect the faces
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cropped = []

    # Add the face to the cropped list if both eyes are visible
    for x, y, w, h in faces:
        face_img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0,), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = face_img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            cropped.append(roi_color)

    return cropped

# classify the image
def classify_image(img_b64, img_path=None):
    imgs = get_cropped_img(img_b64, img_path)
    res = []

    # loop through all cropped faces
    for img in imgs:
        img_har = wav_transform(img, 'db1', 5)

        # Resize the raw image and haar feature image
        raw_img_scaled = cv2.resize(img, (32, 32))
        img_har_scaled = cv2.resize(img_har, (32, 32))

        # stack the 2 images on top of one another
        combined_img = np.vstack((raw_img_scaled.reshape(32 * 32 * 3, 1), img_har_scaled.reshape(32 * 32, 1)))
        combined_img = combined_img.reshape(1, 4096).astype(float)

        # Add models predictions to list
        res.append({
            'label': __label_num_to_name[__model.predict(combined_img)[0]],
            'label_probability': np.round(__model.predict_proba(combined_img) * 100, 2).tolist()[0],
            'label_dict': __label_name_to_num
        })

    return res