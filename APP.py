# -*- coding: utf-8 -*-
"""
Airport Cargo Price Prediction App
"""

import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    with open('Model_saving.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file not found. Please upload 'Model_saving.pkl' to the app folder.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Error loading model: {e}")
    st.stop()

# App title
st.title("✈️ Airport Cargo Price Prediction")
st.write("Fill the following information to estimate your cargo cost:")

# Inputs
dist = st.number_input("Distance (Km)", min_value=0.0)
Area = st.selectbox("Destination Area", ['Ethiopia', 'China', 'USA'])
size = st.number_input("Cargo Size (liters)", min_value=0.0)
weight = st.number_input("Weight (kg)", min_value=0.0)

# Encode area
if Area == 'Ethiopia':
    area = 0
elif Area == 'China':
    area = 1
elif Area == 'USA':
    area = 2

# Predict
if st.button("Predict"):
    Input = np.array([[dist, area, size, weight]])
    try:
        pred = model.predict(Input)
        st.success(f"💰 Estimated Price: {pred[0]:.2f} USD")
    except Exception as e:
        st.error(f"⚠️ Prediction error: {e}")
