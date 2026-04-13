# Task 3: Linear Regression — House Price Prediction

## Objective

To implement and understand **Simple and Multiple Linear Regression** using a **House Price Prediction Dataset**, and evaluate the model performance using various regression metrics.

---

# Tools & Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

# Dataset Information

**Dataset:** Housing.csv
**Rows:** 545
**Columns:** 13
**Target Variable:** Price

Features included:

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

---

# Step 1: Import and Preprocess Dataset

### What was done

* Dataset loaded using Pandas
* Checked dataset structure and missing values
* Converted categorical values to numeric format
* Binary features converted (Yes/No → 1/0)
* Furnishing status encoded using label encoding
* Dataset prepared for regression model

### Findings

* Dataset contained categorical values
* Binary encoding applied to features like mainroad, guestroom, basement
* Label encoding applied to furnishing status
* No major missing values found
* Data successfully cleaned and ready for model training

### Learning

* Importance of data preprocessing
* Binary encoding of categorical values
* Label encoding for multiple categories
* Preparing dataset for machine learning

---

# Step 2: Train-Test Split

### What was done

* Features and target variable separated
* Dataset split into training and testing sets
* 80% used for training
* 20% used for testing

### Findings

* Training dataset used for model learning
* Testing dataset used for evaluation
* Proper data splitting avoids overfitting

### Learning

* Train-test split concept
* Importance of testing dataset
* Avoiding overfitting in machine learning

---

# Step 3: Fit Linear Regression Model

### What was done

* Linear Regression model created
* Model trained using training data
* Multiple regression applied using all features

### Findings

* Model successfully trained
* Coefficients generated for each feature
* Features like area, bathrooms showed strong influence

### Learning

* Simple vs Multiple Linear Regression
* Model fitting process
* Understanding feature coefficients
* Regression modeling fundamentals

---

# Step 4: Model Evaluation and Accuracy

### What was done

* Predictions made on test data
* Evaluation metrics calculated

Metrics used:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score
* Accuracy using MAPE

### Findings

* Model predicted house prices successfully
* R² score showed model performance
* Accuracy calculated using percentage error
* Lower error values indicate better model

### Learning

* Model evaluation metrics
* Understanding regression accuracy
* Importance of R² score
* Error interpretation

---

# Step 5: Plot Regression Line and Interpretation

### What was done

* Simple linear regression performed using area vs price
* Regression line plotted
* Relationship visualized

### Findings

* Area strongly affects house price
* Linear relationship observed
* Model visually validated

### Learning

* Visualizing regression
* Understanding linear relationships
* Simple regression interpretation

---

# Overall Results

* Linear Regression model successfully implemented
* Dataset cleaned and preprocessed
* Model trained and evaluated
* Accuracy calculated
* Relationship between features analyzed

---

# What I Learned

* Linear Regression fundamentals
* Simple Linear Regression
* Multiple Linear Regression
* Data preprocessing
* Binary encoding
* Label encoding
* Train-test split
* Model training
* Model evaluation
* Accuracy calculation
* Regression visualization
* Feature importance

---

# Conclusion

The Linear Regression model was successfully implemented for house price prediction.
Data preprocessing improved model performance.
Evaluation metrics helped understand accuracy.
The project provided practical knowledge of regression modeling.

---

# Project Outcome

Successfully learned:

* Regression modeling
* Evaluation metrics
* Model interpretation
* Machine learning workflow

---

# Author

Sachin Singh
House Price Prediction Project
