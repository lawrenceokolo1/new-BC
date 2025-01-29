import streamlit as st


st.logo("home care schedular files/obalogop.jpg")
st.title("welcome to lawrence projects")
st.caption("A unique portflio")
st.image("home care schedular files/data anime.gif", width= 250)




st.markdown("# projects")
st.info("use the widget at the left to access all projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### [1. bc home schedular](https://lawrence-project.streamlit.app/BC_Health_Appointment_Scheduler)")
    st.image("home care schedular files/beautiful columbians.webp")


with col2:
    st.markdown("#### [2. 60 seconds CSV Analysis](https://lawrence-project.streamlit.app/60sec_CSV_analysis)")
    st.image("home care schedular files/humainoid csv.jpg")
   
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### [3. Diabetics predictor(In Progress) ](https://lawrence-project.streamlit.app/Diabetes_Predictor_(A_Machine_leaning_modelling_technique))")
    st.image("diabetes files/diabetic predictor.webp")

with col4:
    st.markdown("#### 4. Real Time Bed Management(In Progress) ")
    st.image("home care schedular files/real time bed mgt.webp")

