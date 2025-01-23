import streamlit as st
import joblib
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM

st.title("Diabetes Predictor(In Progress)") 
st.write('''The Diabetes Predictor Project is a machine learning-based application designed to predict the likelihood of diabetes in patients based on key health metrics and symptoms. Using features such as glucose level, HbA1c, 
blood pressure, insulin, cholesterol, and symptoms like polyuria (frequent urination) and polydipsia (excessive thirst), the model provides a probabilistic classification of whether a patient is diabetic or not.''')
col1, col2 = st.columns(2)
with col1:
    st.image("images/Animation - 1736490494777.gif")


with col2:
    st.image("images/Main Scene.gif")

#load the saved model
model_path = "diabetes files/diabetesmain_model.joblid"
model = joblib.load(model_path)

#load llama model and tokenizer

llama_model_name = "meta-name/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(llama_model_name)
llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name, device_map="auto", torch_dtype="float16")

#function to prompt recommendation

def get_recommendation(prediction):
    if prediction == 1:
        prompt = "The patient is likely diabetic. provide a short recommendation for managing diabetes"
    else:
        prompt= "The patient is not likely diabetic. provide a short recommendation for maintaining a healthy lifestyle"
        
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = llama_model.generate(inputs["input_ids"], max_length=100,  temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


#streamlit app interface
st.header("Diabetes Predictor")

   

