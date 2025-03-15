from flask import Flask, request, jsonify
from flask_cors import CORS
import utils

app = Flask(__name__)
CORS(app, resources={r"/classify": {"origins": "https://political-figure-classifier-a.vercel.app"}})

# Load artifacts
utils.load_artifacts()

@app.route('/classify', methods=['POST'])
def classify():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.get_json()
        img_b64 = data.get('image_data')

        if not img_b64:
            return jsonify({'error': 'Missing image data'}), 400

        result = utils.classify_image(img_b64)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
