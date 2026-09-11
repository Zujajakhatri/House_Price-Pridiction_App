import joblib
import pandas as pd
import streamlit as st

model = joblib.load("house_price_model.pkl")
st.title("House Price Prediction")

st.write("Enter the details of the house to predict its price.")

area= st.slider("Area (in square feet)", 500, 10000, 1500)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5, 6])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4, 5])

location = st.selectbox(
    "Location", 
    ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", "Multan", "Gujranwala", "Sialkot", "Bahawalpur", "Sheikhupura"])

house_age = st.slider("House Age (in years)", 0, 30, 5)

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "area_sqft": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "location": [location],
        "house_age": [house_age]
    })
    price = model.predict(input_data)[0]

    prediction = model.predict(input_data)
    st.success(f"The predicted price of the house is: Rs {prediction[0]:,.0f}")