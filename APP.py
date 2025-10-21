# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pickle
import numpy as np

with open('Model_saving.pkl','rb') as file:
   model=pickle.load(file)

st.title("Airport Cargo price prediction")
st.write("Fill the following information to get the price you will pay")
dist=st.number_input("Distance in Km")
Area=st.selectbox ("Area of desatination",['Ethiopia','China','USA' ])
size=st.number_input("Size in liters")
weight=st.number_input("Weight")

area=0
if Area=='Ethiopia':
    area=0
if Area=='Chine':
    area=1
if Area=='USA':
    area=2

if st.button("Predict"):
    Input=np.array([[dist,area,size,weight]])
    pred=model.predict(Input)
    st.success(f'Price will be: {pred[0]:.2f} $')


