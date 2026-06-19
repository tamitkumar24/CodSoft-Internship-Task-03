import streamlit as st
import pandas as pd
import joblib


model = joblib.load('churn_model.pkl')
model_columns = joblib.load('model_columns.pkl')


st.title("🏦 Bank Customer Churn Predictor")
st.write("Enter customer details below to predict if they are at risk of closing their account.")

st.markdown("### Customer Details")
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
    geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=5)

with col2:
    balance = st.number_input("Account Balance ($)", min_value=0.0, value=50000.0)
    num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
    has_cr_card = st.selectbox("Has Credit Card?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    is_active = st.selectbox("Is Active Member?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    estimated_salary = st.number_input("Estimated Salary ($)", min_value=0.0, value=60000.0)

if st.button("Predict Churn Risk", type="primary"):
    
    input_data = {
        'CreditScore': credit_score,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active,
        'EstimatedSalary': estimated_salary,
        'Geography_Germany': 1 if geography == 'Germany' else 0,
        'Geography_Spain': 1 if geography == 'Spain' else 0,
        'Gender_Male': 1 if gender == 'Male' else 0
    }

   
    input_df = pd.DataFrame([input_data])
    
    
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    
    prediction = model.predict(input_df)

    
    st.divider()
    if prediction[0] == 1:
        st.error("🚨 **High Risk:** This customer exhibits patterns of someone who will leave the bank.")
    else:
        st.success("✅ **Low Risk:** This customer is likely to stay loyal.")