import streamlit as st


st.title("Millfeed Predictor(In Progress)")
st.subheader("A Simple Model for Predicting Canadian Millfeed Production")
st.image("images/agric.gif")
st.caption("A Canadian wheat predictor")

st.write("This project uses historical data on wheat milling to build a simple predictive model for estimating millfeed production. By leveraging statistical methods and visualizations, the project provides insights into milling operations and helps optimize resource planning.")

st.markdown('''The dataset used to build this project was collected from [Statistics Canada](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3210001601&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2014&cubeTimeFrame.endMonth=12&cubeTimeFrame.endYear=2024&referencePeriods=20140101%2C20241201). It contains data from January 2014 to November 2024, covering metrics such as Total Wheat Milled, Total Wheat Flour Produced, and Millfeeds Produced (all in metric tons).''')

st.header("Analysis and visualisation")