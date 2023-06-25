import streamlit as st
import joblib 
import numpy as np
from content import labels_dic

model = joblib.load("crop recommendation")
st.title("crop recommendation system")

N = st.slider(label="Select Nitrogen level",min_value=0.0,max_value=200.0)
P = st.slider(label="Select Phosphorus Level",min_value=0.0,max_value=200.0)
K = st.slider(label="Select Potassium Level",min_value=0.0,max_value=250.0)
temp = st.slider(label="Select temperature Level",min_value=0.0,max_value=60.0)
humidity = st.slider(label="Select humidity Level",min_value=0.0,max_value=150.0)
ph = st.slider(label="Select ph Level",min_value=0.0,max_value=14.0)
rainfall = st.slider(label="Select Rainfall Level",min_value=0.0,max_value=300.0)

lis = np.array([[N,P,K,temp,humidity,ph,rainfall]])

with st.expander("Suggested crop"):
    if lis.max() > 0:
        result = labels_dic[model.predict(lis)[0]]
        st.success(result)
    else:
        st.warning("Select values")
