import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# Page styling
st.set_page_config(page_title="Student Mark Predictor", page_icon="🎓", layout="centered")

st.title("🎓 Student Mark Predictor")
st.write("Enter your daily study hours to predict your expected percentage score.")

# Model safe loading
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'student_mark_predictor.pkl')
csv_path = os.path.join(BASE_DIR, 'smp_data_from_app.csv')

try:
    model = joblib.load(model_path)
    
    # User Input Slider
    study_hours = st.slider("Select Study Hours per Day:", min_value=0.0, max_value=24.0, value=5.0, step=0.5)

    if st.button("Predict Score 📊"):
        # Prediction logic
        features = np.array([[study_hours]])
        prediction = model.predict(features)
        output_round = round(float(prediction[0]), 2)
        
        # Display Result
        st.success(f"🎯 Your Predicted Marks: **{output_round}%**")
        
        # Save logs to CSV silently
        df = pd.DataFrame([[study_hours, output_round]], columns=['study_hours', 'predicted_marks'])
        df.to_csv(csv_path, mode='a', header=not os.path.exists(csv_path), index=False)

except Exception as e:
    st.error(f"Error loading model or files: {e}")
