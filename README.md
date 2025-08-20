🏡✨ Dream Home Price Predictor: A Full-Stack ML Journey ✨🏡
🌟 Project Overview: Bringing ML to Life!
This project is a comprehensive demonstration of building and deploying a full-stack Machine Learning application for House Price Prediction. It showcases the entire journey from training a predictive model to making it accessible via an interactive web interface, all hosted publicly.

The core idea is to predict house prices based on various features using a Linear Regression model. What makes this project truly exciting is its end-to-end nature: it integrates a Python-based ML backend with a modern web frontend, connected seamlessly via a RESTful API, and deployed to a cloud platform.

This project serves as a practical example of MLOps principles, demonstrating how a data science model can be transformed into a tangible, user-friendly product.

✨ Key Features
The application predicts house prices based on the following input features:

Area_sqft: The size of the house in square feet.

Bedrooms: The number of bedrooms.

Bathrooms: The number of bathrooms.

YearBuilt: The year the house was constructed.

Location: The geographical area (e.g., 'Downtown', 'Suburban', 'Rural', 'Urban outskirts').

The output is the Price_USD, an estimated market value in US Dollars.

🚀 Architecture: The Full-Stack Blueprint
This application follows a standard client-server architecture, divided into three main components:

Machine Learning Model (Python/Scikit-learn):

The "brain" of the application.

A Linear Regression model trained on a synthetic dataset.

Responsible for learning the relationships between house features and their prices.

The trained model is saved as a .pkl file using joblib.

Backend API (Python/Flask):

A lightweight web server built with Flask.

Serves as the bridge between the frontend and the ML model.

Loads the pre-trained house_price_model.pkl into memory when the server starts.

Exposes a /predict API endpoint that accepts house features (JSON payload) via POST requests.

Uses the loaded ML model to make predictions and returns the estimated price as a JSON response.

Also serves the index.html file (frontend) from its root (/) route.

Frontend (HTML/JavaScript/Tailwind CSS):

The interactive user interface that runs in the user's web browser.

Built with clean HTML for structure.

Styled beautifully and responsively using Tailwind CSS.

JavaScript handles user input, sends prediction requests to the Flask API using fetch(), and dynamically displays the predicted price.

🛠️ Technologies Used
Python 3.x: Core programming language.

Scikit-learn: For Machine Learning model training (Linear Regression, OneHotEncoder, ColumnTransformer, Pipeline).

Pandas: For data manipulation and handling.

NumPy: For numerical operations.

Flask: Lightweight web framework for building the backend API.

Flask-CORS: To enable Cross-Origin Resource Sharing for seamless frontend-backend communication.

Joblib: For saving and loading the trained ML model.

Gunicorn: Production-ready WSGI HTTP server used by Hugging Face Spaces to run the Flask app.

HTML5: Structure of the web interface.

Tailwind CSS: Utility-first CSS framework for rapid and responsive UI development.

JavaScript: For dynamic client-side interactions and API calls.

Git: Version control system.

Hugging Face Spaces: Cloud platform for deploying and hosting the full-stack ML application.

🏁 Getting Started Locally
To run this project on your local machine, follow these steps:

1. Clone the Repository
First, clone this GitHub repository to your local machine:

git clone https://github.com/Sagnik07/sagnic-house-price-predictor.git # Replace with your actual repo URL
cd sagnic-house-price-predictor

2. Set Up Python Environment
It's highly recommended to use a virtual environment:

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Install all required Python libraries from requirements.txt:

pip install -r requirements.txt

4. Train and Save the ML Model
You need to train the model and save it locally. The retrain_and_save.py script handles this.

python retrain_and_save.py

This will create the models/house_price_model.pkl file, compatible with your local scikit-learn version.

5. Run the Flask Backend API
Start the Flask server. Ensure you are in the project's root directory (sagnic-house-price-predictor).

python app.py

The API will run on http://127.0.0.1:5000. Keep this terminal window open.

6. Open the Frontend
Your index.html file is configured to point to http://127.0.0.1:5000/predict by default.

Open your file explorer, navigate to the sagnic-house-price-predictor folder.

Double-click index.html to open it in your web browser.

You can now interact with the application locally!

🚀 Deployment: Live on Hugging Face Spaces
This project is deployed as a Hugging Face Space, making it publicly accessible.

Deployment Process:
Project Preparation:

Ensured app.py, index.html, models/, requirements.txt, and Procfile were correctly configured.

requirements.txt was cleaned to include only essential dependencies (Flask, scikit-learn, pandas, numpy, joblib, Flask-Cors, gunicorn).

Procfile was set to web: gunicorn app:app -b 0.0.0.0:$PORT to instruct Hugging Face on how to run the Flask app.

app.py was modified to serve index.html from its root route and listen on the dynamic $PORT provided by the environment.

Git Integration:

The entire project was version-controlled using Git.

Changes were pushed to the Hugging Face Space's Git repository using a User Access Token for authentication.

Automatic Build & Deployment:

Hugging Face Spaces automatically detected the Python project, installed dependencies, and built the application.

Any git push to the Space's repository triggers an automatic rebuild and redeployment.

Frontend-Backend Connection:

The API_URL in index.html's JavaScript was updated to point to the public URL of the deployed Hugging Face Space (e.g., https://your-space-url.hf.space/predict).

🌐 Live Demo
Experience the Dream Home Price Predictor live!

Visit the deployed application here:
https://huggingface.co/spaces/Sagnik07/sagnic-house-price-predictor

📂 Project Structure
.
├── models/
│   └── house_price_model.pkl   # Trained ML model
├── app.py                      # Flask Backend API
├── index.html                  # Frontend HTML/JS/CSS
├── requirements.txt            # Python dependencies for Flask app
├── Procfile                    # Heroku/Hugging Face process definition
├── House_price_prediction_using_linear_regression.ipynb # Jupyter Notebook (training/exploration)
└── retrain_and_save.py         # Script to train and save model locally

🔮 Future Enhancements
More Sophisticated Models: Experiment with Random Forest, Gradient Boosting (XGBoost/LightGBM) for potentially higher accuracy.

Real-world Data: Integrate with a larger, more complex real-world housing dataset (e.g., from Kaggle) to handle missing values, outliers, and diverse features.

Feature Engineering: Create more advanced features (e.g., age of house, distance to amenities).

Model Monitoring: Implement logging and monitoring for model performance in production.

User Authentication: Add user login/signup functionality.

Database Integration: Store prediction history or user preferences.

Containerization: Package the Flask app in a Docker container for more consistent deployment across environments.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

✉️ Contact
Feel free to connect with me on LinkedIn for any questions or collaborations!
