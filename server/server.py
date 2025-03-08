from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import utils

app = Flask(__name__)
#CORS(app, resources={r"/classify": {"origins": "https://political-figure-classifier.vercel.app"}})
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return 'hello'

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    img_b64 = request.json['image_data']

    # Classify the image and return our results
    res = jsonify(utils.classify_image(img_b64))

    if not res:
        return make_response(jsonify({'error': 'Image is unclear'}), 400)

    return res

# Run server
if __name__ == "__main__":
    utils.load_artifacts()  # Load our model and label dict
    app.run(port=3000)
