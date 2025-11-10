import numpy as np
import pickle

# Load saved model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

def predict_disease(input_data):
    """
    Predicts diabetes based on input data (list or array)
    """
    input_array = np.array([input_data])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        return "Positive — Diabetes Detected"
    else:
        return "Negative — No Diabetes"

