# Import necessary libraries
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = load_model("cifar10_resnet50.h5")
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if an image is in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Load the image
        image = Image.open(file).resize((32, 32))  # Resize to CIFAR-10 dimensions
        image = img_to_array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make prediction
        predictions = model.predict(image)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions)

        return jsonify({"class": predicted_class, "confidence": float(confidence)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
