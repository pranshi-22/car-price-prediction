import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your trained model
model = pickle.load(open('car_price_model.pkl', 'rb'))
X_columns = pickle.load(open('x_columns.pkl', 'rb'))

st.title("🚗 Car Price Prediction App")
st.write("Enter the details of the car below to estimate its selling price:")

# Input fields
year = st.number_input("Year of manufacture", min_value=1990, max_value=2025, value=2015)
present_price = st.number_input("Present price (in lakhs)", min_value=0.0, value=5.0)
kms_driven = st.number_input("Kms driven", min_value=0, value=50000)
fuel_type = st.selectbox("Fuel type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission type", ["Manual", "Automatic"])
owner = st.number_input("Number of previous owners", min_value=0, max_value=3, value=0)

# Prepare data
input_data = pd.DataFrame({
    'Year': [year],
    'Present_Price': [present_price],
    'Kms_Driven': [kms_driven],
    'Fuel_Type': [fuel_type],
    'Seller_Type': [seller_type],
    'Transmission': [transmission],
    'Owner': [owner]
})

# Match encoding
input_data_encoded = pd.get_dummies(input_data, drop_first=True).reindex(columns=X_columns, fill_value=0)

# Predict button
if st.button("Predict Price 💰"):
    prediction = model.predict(input_data_encoded)[0]
    st.success(f"Estimated Selling Price: ₹{prediction:.2f} Lakhs")