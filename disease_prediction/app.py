import streamlit as st
import pandas as pd
from model import predict_disease

# -----------------------------
st.set_page_config(page_title="Disease Prediction System", layout="centered")
# -----------------------------

st.title("🩺 Disease Prediction System")
st.markdown("""
This app predicts whether a person is **Diabetic or Not** based on their medical parameters.
""")

st.sidebar.header("📋 Input Patient Details")

# Sidebar inputs
pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.sidebar.number_input("Glucose", min_value=0, max_value=300, value=120)
bp = st.sidebar.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin = st.sidebar.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.sidebar.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=70.0, value=25.5)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=33)

# Predict button
if st.sidebar.button("Predict Disease"):
    input_data = [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]
    result = predict_disease(input_data)
    st.success(f"### 🩸 Prediction Result: {result}")

