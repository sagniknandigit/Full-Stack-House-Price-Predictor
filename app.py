import pandas as pd
from flask import Flask, request, jsonify
import joblib # For loading the saved model
from flask_cors import CORS # For handling Cross-Origin Resource Sharing
import os # For path operations

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all routes, allowing requests from your frontend
# This is crucial for your browser-based frontend to communicate with this API
CORS(app)

# Define the path to the saved model
# The 'models' directory should be in the same location as this app.py file
MODEL_DIR = 'models'
MODEL_PATH = os.path.join(MODEL_DIR, 'house_price_model.pkl')

# --- Load the trained model ---
# This model will be loaded once when the Flask app starts.
# Loading it here (globally) prevents reloading it for every request, improving performance.
try:
    model_pipeline = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}.")
    print("Please ensure you have run the house price prediction script to train and save the model.")
    print("The 'models' directory with 'house_price_model.pkl' should be in the same folder as app.py.")
    model_pipeline = None # Set to None to indicate model is not loaded
except Exception as e:
    print(f"Error loading model: {e}")
    model_pipeline = None

# --- API Routes ---

@app.route('/')
def home():
    """
    A simple home route to confirm the API server is running.
    Access this by navigating to http://localhost:5000/ in your browser.
    """
    return "House Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to predict house prices.
    It expects a JSON payload containing the house features.

    Example JSON Request Body:
    {
        "Area_sqft": 2500,
        "Bedrooms": 4,
        "Bathrooms": 3,
        "YearBuilt": 2010,
        "Location": "Downtown"
    }
    """
    if model_pipeline is None:
        # If the model failed to load at startup, return an error
        return jsonify({'error': 'Prediction service unavailable: Model not loaded.'}), 500

    try:
        # Get JSON data from the incoming request
        # force=True is used to parse incoming data as JSON even if the Content-Type header is not application/json
        data = request.get_json(force=True)

        # Convert the received JSON data into a Pandas DataFrame.
        # It's crucial that the keys in the JSON (e.g., "Area_sqft") match the column names
        # that your original Python model was trained with.
        features_df = pd.DataFrame([data])

        # Define the expected features to validate the input
        required_features = ['Area_sqft', 'Bedrooms', 'Bathrooms', 'YearBuilt', 'Location']

        # Check if all required features are present in the incoming data
        if not all(feature in features_df.columns for feature in required_features):
            missing_features = [f for f in required_features if f not in features_df.columns]
            return jsonify({'error': f'Missing required features: {", ".join(missing_features)}. '
                                     f'Please provide all of: {", ".join(required_features)}'}), 400

        # Make prediction using the loaded model pipeline.
        # The pipeline automatically handles preprocessing steps like OneHotEncoding for 'Location'.
        # [0] is used because model_pipeline.predict() returns a NumPy array, even for a single prediction.
        prediction = model_pipeline.predict(features_df)[0]

        # Return the prediction as a JSON response
        # round() is used for clean formatting, float() ensures it's a standard number type for JSON.
        return jsonify({'predicted_price': round(float(prediction), 2)})

    except KeyError as e:
        # Catch errors if an expected key is missing from the JSON payload
        return jsonify({'error': f'Invalid input data format. Missing key: {e}. '
                                 f'Ensure all features are correctly named.'}), 400
    except Exception as e:
        # Catch any other unexpected errors during the prediction process
        print(f"An unexpected error occurred: {e}")
        return jsonify({'error': f'An internal server error occurred during prediction: {str(e)}'}), 500

# --- Run the Flask Application ---

if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # host='0.0.0.0': Makes the server accessible from any IP address on your network.
    #                Useful for testing from other devices or in Docker/cloud environments.
    # port=5000: The port number the server will listen on.
    # debug=True: Enables Flask's debugger and auto-reloader.
    #             IMPORTANT: Set to False in a production environment for security and performance.
    app.run(host='0.0.0.0', port=5000, debug=True)
