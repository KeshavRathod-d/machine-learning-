import streamlit as st
import requests
import pandas as pd

st.title("🩺 Disease Prediction Web App")


st.write("Enter your medical details below:")


preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)


if st.button("Predict"):
    features = [preg, glucose, bp, skin, insulin, bmi, dpf, age]
    response = requests.post("http://127.0.0.1:5000/predict", json={"features": features})
    result = response.json()["prediction"]

    if result == 1:
        st.error("⚠️ You are likely to have Diabetes. Please consult a doctor.")
    else:
        st.success("✅ You are healthy! Keep maintaining your lifestyle.")

