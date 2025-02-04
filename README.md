# price_prediction
The House Price Prediction project is a machine learning-based system that predicts house prices based on various factors such as location, number of bedrooms, area, and other features. This project helps to find rent price of the house in particular loation with prices more accurately.

│-- ve3                         # Project directory
│   │-- main.py                 # Main script
│   │-- train_model.py          # Model training script
│   │-- model.pkl               # Trained model file
│   │-- Pune_rent.csv           # Dataset
│   │-- requirements.txt        # Dependencies
│   │-- static/                 # Static files (CSS)
│   │-- templates/              # HTML Templates

✅ Predicts house prices based on given input features such as number of bedrooms, bathrooms, square footage, location, etc.
✅ Uses machine learning algorithms for accurate estimation on  input features.
✅ Trained on Pune_rent.csv dataset
✅ Deployable as a Flask web app

Technologies Used
Backend: Flask (Python)
Frontend: HTML, CSS, Bootstrap
Machine Learning: Scikit-learn, Pandas, NumPy
Dataset: Open-source housing price dataset

Installation and Setup
Steps to Set Up the Project
Clone the Repository
cd flask-house-price-prediction
Create a Virtual Environment (Optional but recommended)
python -m venv env
On Windows use `env\Scripts\activate`
Install Dependencies

pip install -r requirements.txt

Run the Flask Application

python main.py

Access the Web Application
Open your browser and go to:

http://127.0.0.1:5000/

Usage

Open the web application in your browser.

Enter the required house details in the input form.

Click on the " Check Predict Price" button.

View the estimated house price displayed on the screen..
