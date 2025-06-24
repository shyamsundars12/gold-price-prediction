import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load scaler and model
scaler = pickle.load(open("scaler.pkl", "rb"))
model = pickle.load(open("regressor.pkl", "rb"))

# App title
st.title("💰 How much is 1g of gold in India NOW?")

# Info message about training data
st.info("ℹ️ This model is trained on 2024 data. Please enter USD to INR values from 76 and above.")

# Input for USD to INR with minimum value constraint
usd_inr = st.number_input("Enter USD to INR exchange rate:", min_value=76.0, format="%.2f")

# Prediction button
if st.button("Predict"):
    try:
        input_df = pd.DataFrame([[usd_inr]], columns=["USD_INR"])
        input_scaled = scaler.transform(input_df)

        predicted_gold_price = round(model.predict(input_scaled)[0][0], 2)

        st.success(f"Predicted Gold Price is (1g): ₹{predicted_gold_price}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
