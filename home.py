import streamlit as st

from streamlit_lottie import st_lottie

st.logo("images/obalogop.jpg")
st.title("welcome to lawrence projects")
st.caption("A unique portflio")
st.image("images/data anime.gif", width= 250)



st.markdown("# projects")
st.info("use the widget at the left to access all projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### [1. bc home schedular](http://localhost:8501/BC_Health_Appointment_Scheduler)")
    st.image("images/beautiful columbians.webp")


with col2:
    st.markdown("#### [2. 60 seconds CSV Analysis](http://localhost:8501/60sec_CSV_analysis)")
    st.image("images/friendly humainoid csv.webp")
   
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### [3. Canada mill feed predictor(In Progress) ](http://localhost:8501/mill_feed_predictor)")
    st.image("images/wheat mill production.webp")
