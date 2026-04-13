# House Price Prediction using Linear Regression

## Project Overview

This project focuses on building a **House Price Prediction System** using **Linear Regression**.
The model analyzes different house features such as area, number of bedrooms, bathrooms, and other amenities to **predict the price of a house**.

The trained model is deployed using a **Flask web application**, allowing users to input house details and get an estimated price instantly.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Flask
* HTML
* Pickle

---

# Dataset Description

The dataset used in this project contains **545 rows and 13 columns**.
It includes various features that influence house prices.

### Features Used for Prediction

* Area
* Bedrooms
* Bathrooms
* Stories
* Mainroad
* Guestroom
* Basement
* Hotwaterheating
* Airconditioning
* Parking
* Prefarea
* Furnishingstatus

**Target Variable:**

* Price

---

# How the Model Predicts House Prices

The prediction process follows these steps:

### 1. Data Preprocessing

* The dataset is cleaned and prepared
* Categorical values are converted into numerical values
* Binary values such as Yes/No are converted into 1 and 0
* Data becomes suitable for machine learning model training

---

### 2. Model Training

* Linear Regression algorithm is used
* The model learns relationships between features and house price
* Multiple features are used to improve prediction accuracy

---

### 3. Model Evaluation

The model performance is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score
* Accuracy using MAPE

These metrics help measure how well the model predicts house prices.

---

### 4. Model Saving

* After training, the model is saved using Pickle
* Saved as **model.pkl**
* This allows reuse without retraining

---

### 5. Web Application Prediction

* User enters house details in the web interface
* Flask app loads the trained model
* Model processes the input data
* Predicted house price is displayed to the user

---

# Project Structure

```
House-Price-Prediction/
│
├── app.py
├── model.pkl
├── Housing.csv

│─ index.html
│
└── README.md
```

---

# Files Included

* **app.py** — Flask application for prediction
* **model.pkl** — Trained Linear Regression model
* **index.html** — Web interface
* **Housing.csv** — Dataset
* **README.md** — Project documentation

---

# Features of the Project

* Predict house price using multiple features
* User-friendly web interface
* Machine learning based prediction
* Model saved using Pickle
* Fast and efficient prediction

---

# Learning Outcomes

* Linear Regression implementation
* Data preprocessing techniques
* Model training and evaluation
* Machine learning deployment
* Flask web application development
* Model saving using Pickle

---

# Conclusion

This project demonstrates how **Linear Regression** can be used to predict house prices based on various features.
The trained model is deployed as a **web application**, making it easy for users to estimate house prices quickly and efficiently.

---

# Author

**Sachin Singh**
Machine Learning Project
House Price Prediction
