"""
Simple Streamlit application for California House Price Prediction.

Requirements:
pip install -r requirements.txt

Run:
streamlit run app.py
"""


import streamlit as st
import pickle
import pandas as pd

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("California House Price Prediction")

medinc = st.number_input("Median Income", value=3.5)
houseage = st.number_input("House Age", value=25.0)
averooms = st.number_input("Average Rooms", value=5.0)
avebedrms = st.number_input("Average Bedrooms", value=1.0)
population = st.number_input("Population", value=1000.0)
aveoccup = st.number_input("Average Occupancy", value=3.0)
latitude = st.number_input("Latitude", value=34.0)
longitude = st.number_input("Longitude", value=-118.0)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "MedInc": [medinc],
        "HouseAge": [houseage],
        "AveRooms": [averooms],
        "AveBedrms": [avebedrms],
        "Population": [population],
        "AveOccup": [aveoccup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted House Value: {prediction[0]:.3f}")