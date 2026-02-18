import streamlit as st
import joblib
import numpy as np
st.write("Streamlit app")
model=joblib.load('salary_model.pkl')
Experience=st.slider("Years of experience",min_value=0.0,max_value=15.0,step=0.5)
prediction=model.predict([[Experience]])
st.subheader("Predicted Salary")
st.write(f"${prediction[0]:,.2f}")


