import streamlit as st
st.logo("images/obalogop.jpg")
st.title("this is my home page")

st.markdown(" ### Project 1 : British Colmbia Home Care Schedular (A database project)" )
st.title("Welcome to the Project Hub!")
st.write("Explore our innovative tools and applications designed to simplify your workflows.")

# Section: Project Overview
st.header("Explore Our Projes")

# Project 1: Health Scheduler
st.subheader("Health Scheduler")
st.write("A centralized platform for booking home and community care appointments.")
if st.button("Go to Health Scheduler"):
    st.experimental_set_query_params(page="Health_Scheduler")

# Title and Welcome Message
st.title("Welcome to the Project Hub!")
st.write("""
Explore our innovative tools and applications designed 
to simplify your workflows. Select a project below:
""")

# Navigation Buttons with Query Parameters
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Health Scheduler"):
        st.query_params.update({"page": "BC_Health_Appointment_Scheduler.py"})

with col2:
    if st.button("Task Manager"):
        st.query_params.update({"page": "Task_Manager"})
