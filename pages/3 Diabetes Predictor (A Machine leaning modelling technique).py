import streamlit as st
st.write("The Diabetes Predictor Project is a machine learning-based application designed to predict the likelihood of diabetes in patients based on key health metrics and symptoms. Using features such as glucose level, HbA1c, blood pressure, insulin, cholesterol, and symptoms like polyuria (frequent urination) and polydipsia (excessive thirst), the model provides a probabilistic classification of whether a patient is diabetic or not.")


st.title("Diabetes Predictor(In Progress)")
col1, col2 = st.columns(2)

with col1:
    st.image("images/Animation - 1736490494777.gif")


with col2:
    st.image("images/Main Scene.gif")
