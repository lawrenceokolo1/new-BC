import streamlit as st
import pandas as pd
import ydata_profiling
import pandas_profiling
import streamlit_pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


st.title("60 Sec CSV for Data Professional")
st.image("images/humainoid csv.jpg", caption= "Analyse your CSV dataset in 60 seconds")

st.subheader("Overview")
st.markdown("The *60 seconds CSV Report* provides a comprehensive overview of a dataset, enabling data professionals to quickly understand its structure, quality, and key statistics without manual exploration. It saves time and effort, allowing professionals to focus on deriving insights and building models.Feel free to use it by importing a CSV file into it ")

st.subheader("import CSV here!")
file_uploader = st.file_uploader("CSV here!", type=["csv"])

if file_uploader:
    df = pd.read_csv(file_uploader)
    st.dataframe(df)
    profile= ProfileReport(df, title="pandas report", samples = None, missing_diagrams= {"bar": False, "matrix": False, "heatmap": False }, explorative=True)
    st.snow()
    st_profile_report(profile)

    

    # Add download button for HTML version of the report
    html_report = profile.to_html()
    
    st.download_button(
        label="Download Full Report",
        data=html_report,
        file_name="60 seconds analysis.html",
        mime="text/html",
    )