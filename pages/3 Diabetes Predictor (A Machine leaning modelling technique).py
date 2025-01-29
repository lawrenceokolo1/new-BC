import streamlit as st
import joblib
import pandas as pd
import numpy as np
from transformers import LlamaTokenizer, LlamaForCausalLM

st.title("Diabetes Predictor") 
st.caption("by lawrence okolo ")

st.info('''The Diabetes Predictor is a machine learning-based application designed to predict the likelihood of diabetes in patients based on key health metrics and symptoms. Using features such as  glucose level, BMI,  HbA1c, insulin, cholesterol, and symptoms like polyuria (frequent urination) and polydipsia (excessive thirst), the model provides a probabilistic classification of whether a patient is diabetic or not.''')

#load the saved model
model_path = "diabetes files/diabetesNbest_model.joblid"
model = joblib.load(model_path)

#load llama model and tokenizer

#llama_model_name = "meta-llama/Llama-2-7b"

#tokenizer = LlamaTokenizer.from_pretrained(llama_model_name)

#llama_model = LlamaForCausalLM.from_pretrained(llama_model_name, device_map="auto", torch_dtype="float16")

#function to prompt recommendation

#def get_recommendation(prediction):
    #if prediction == 1:
        #prompt = "The patient is likely diabetic. provide a short recommendation for managing diabetes"
    #else:
        #prompt= "The patient is not likely diabetic. provide a short recommendation for maintaining a healthy lifestyle"
        
    #inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    #outputs = llama_model.generate(inputs["input_ids"], max_length=100,  temperature=0.7)
    #response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    #return response


#streamlit app interface
st.header("Diabetes Predictor")
col1,col2,col3 = st.columns(3)
with col1:
    st.subheader("glucose")
    st.image("diabetes files/Main Scene.gif")
    glucose = st.number_input("Glucose Level(max_value=300)", min_value=0, max_value=300, value=120)

with col2:
    st.subheader("HbA1c")
    st.image("diabetes files/hba1c main.jpeg")
    hba1c = st.number_input("HbA1c Level (max_value=15)", min_value=0, max_value=15, value=6)

with col3:
    st.subheader("Blood Pressure")
    st.image("diabetes files/turn bowl.gif")
    blood_pressure = st.number_input("Blood Pressure(max=300) ", min_value=50, max_value=300, value=80)

col4,col5,col6 = st.columns(3)
with col4:
    st.subheader("insulin")
    st.image("diabetes files/turn bowl.gif")
    insulin = st.number_input("Insulin Level (max=500)", min_value=0, max_value=500, value=100)
with col5:
    st.subheader("cholesterol")
    st.image("diabetes files/cholesterol test.jpeg")
    cholesterol= st.number_input("Cholesterol Level(max=500)", min_value=0, max_value=500, value=100)
with col6:
    st.subheader("age")
    st.image("diabetes files/Main Scene.gif")  
    age= st.number_input("age", min_value = 10, max_value=180, value=45)

col7,col8,col9 = st.columns(3)
with col7:
    st.subheader("polyuria")
    st.image("diabetes files/Main Scene.gif")
    polyuria = st.selectbox("Polyuria(frequent urination)", options=["Yes", "No"])

with col8:
    st.subheader("polydipsia")
    st.image("diabetes files/polydipsia.jpeg")
    polydipsia = st.selectbox("Polydipsia(excessive thirst)", options=["Yes", "No"])

with col9:
    st.subheader("BMI")
    st.image("diabetes files/turn bowl.gif")
    bmi = st.number_input("body mass(max=70)", min_value=10, max_value=70, value=20)

#convert categorical features to numerical
polyuria = 1 if polyuria == "yes" else 0
polydipsia = 1 if polydipsia == "yes" else 0

if st.button("predict"):
    #combine inputs into a feature array
    features = np.array([[bmi, glucose, hba1c,  insulin, cholesterol, polyuria, polydipsia ]])

    #make prediction using the diabeties model
    prediction = model.predict(features)[0]
    prediction_proba = model.predict_proba(features)[0]

    #display result and generate recommendation
    st.write(f"Prediction: {prediction}")

    if prediction == 1:
        st.success(f"the patient is likely diabetic with a probability of {prediction_proba[1]*100:.2f}%.")
    else:
        st.success(f"the patient is NOT likely diabetic with a probability of {prediction_proba[0]*100:.2f}%.")
    
    #recommendation = get_recommendation(prediction)
    #st.info(f"Recommendation: {recommendation}")


   

