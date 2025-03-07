from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    img_b64 = request.form['image_data']

    # Classify the image and return our results
    res = jsonify(utils.classify_image(img_b64))
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

# Run server
if __name__ == "__main__":
    utils.load_artifacts() # Load our model and label dict
    app.run(port=3000)