import streamlit as st
import joblib
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM


st.title("Diabetes Predictor(In Progress)") 


st.write('''The Diabetes Predictor Project is a machine learning-based application designed to predict the likelihood of diabetes in patients based on key health metrics and symptoms. Using features such as glucose level, HbA1c, 
blood pressure, insulin, cholesterol, and symptoms like polyuria (frequent urination) and polydipsia (excessive thirst), the model provides a probabilistic classification of whether a patient is diabetic or not.''')

#load the saved model
model_path = "diabetes files/diabetesmain_model.joblid"
model = joblib.load(model_path)

#load llama model and tokenizer

#llama_model_name = "meta-llama/Llama-2-7b"

#tokenizer = AutoTokenizer.from_pretrained(llama_model_name)
#llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name, device_map="auto", torch_dtype="float16")

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
glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0, value=120.0)
hba1c = st.number_input("HbA1c Level", min_value=0.0, max_value=15.0, value=6.0)
blood_pressure = st.number_input("Blood Pressure", min_value=50.0, max_value=300.0, value=80.0)
insulin = st.number_input("Insulin Level", min_value=0.0, max_value=500.0, value=100.0)
cholesterol= st.number_input("Cholesterol Level", min_value=0.0, max_value=500.0, value=100.0)  
age= st.number_input("age", min_value = 10, max_value=180, value=45)
polyuria = st.selectbox("Polyuria(frequent urination)", options=["Yes", "No"])
polydipsia = st.selectbox("Polydipsia(excessive thirst)", options=["Yes", "No"])
bmi = st.number_input("body mass", min_value=10.0, max_value=70.0, value=20.0)

#convert categorical features to numerical
polyuria = 1 if polyuria == "yes" else 0
polydipsia = 1 if polydipsia == "yes" else 0

if st.button("predict"):
    #combine inputs into a feature array
    features = np.array([[glucose, hba1c, blood_pressure, insulin, cholesterol, age, polyuria, polydipsia, bmi]])

    #make prediction using the diabeties model
    prediction = model.predict(features)[0]
    prediction_proba = model.predict_proba(features)[0]

    #display result and generate recommendation

    if prediction == 1:
        st.success(f"the patient is likely diabetic with a probability of {prediction_proba[1]*100:.2f}%.")
    else:
        st.success(f"the patient is not likely diabetic with a probability of {prediction_proba[0]*100:.2f}%.")
    
    #recommendation = get_recommendation(prediction)
    #st.info(f"Recommendation: {recommendation}")


   

