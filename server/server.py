from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import utils

app = Flask(__name__)
CORS(app, resources={r"/classify": {"origins": "https://political-figure-classifier-a.vercel.app"}})

@app.route('/', methods=['GET'])
def hello():
    return 'hello'


@app.route('/classify', methods=['POST'])
def classify():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400

    data = request.get_json()
    img_b64 = data.get('image_data')

    if not img_b64:
        return jsonify({'error': 'Missing image data'}), 400

    result = utils.classify_image(img_b64)
    return jsonify(result)

# Run server
if __name__ == "__main__":
    utils.load_artifacts()  # Load our model and label dict
    app.run(host="0.0.0.0", port=10000)
