#  Bank Customer Churn Prediction 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tamitkumar24-codsoft-internship-task-03-app-mhfm5u.streamlit.app/)

**Live Web App:** [Click here to view the live Churn Predictor](https://tamitkumar24-codsoft-internship-task-03-app-mhfm5u.streamlit.app/)

##  Overview
This project is a Machine Learning web application designed to predict whether a bank customer is likely to close their account (churn). 

This project was developed as **Task 3** for the **CodSoft Machine Learning Internship**.

##  The Challenge & Solution
**The Problem:** The raw banking dataset was highly imbalanced. The vast majority of customers stayed with the bank (Class 0), while only a small percentage churned (Class 1). A standard model would guess "stay" every time, achieving high accuracy but failing to catch the actual churners.

**The Solution:** I utilized **SMOTE (Synthetic Minority Over-sampling Technique)** to generate synthetic data for the minority class, perfectly balancing the training data. This forced the Random Forest algorithm to learn the underlying patterns of a churner, significantly increasing the model's **Recall** for Class 1.

##  Tech Stack
* **Language:** Python
* **Data Processing & Machine Learning:** `pandas`, `scikit-learn`, `imbalanced-learn` 
* **Algorithm:** Random Forest Classifier
* **Web Framework:** `streamlit`
* **Model Serialization:** `joblib`
* **Deployment:** Streamlit Community Cloud

##  How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tamitkumar24/CodSoft-Internship-.git](https://github.com/tamitkumar24/CodSoft-Internship-.git)
   cd "TASK -03 - CUSTOMER CHURN PREDICTION"


Install the required libraries:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Project Structure
app.py: Streamlit application code.
churn_model.pkl: Pre-trained Random Forest model.
model_columns.pkl: List of required columns for accurate user input translation.
requirements.txt: Python dependencies.
Churn_Modelling.csv: Original raw dataset.

by Amit Kumar
