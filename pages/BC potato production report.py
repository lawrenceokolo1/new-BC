import streamlit as st
st.title("Can we play with big boys in potato production")


import pandas as pd

# Clinic data
data = {
    "lat": [49.2827, 49.2488, 49.1666],
    "lon": [-123.1207, -122.9805, -123.1336],
    "name": ["Vancouver Clinic", "Burnaby Clinic", "Richmond Clinic"]
}
df = pd.DataFrame(data)

# Display the map
st.title("Health Resource Locator")
st.map(df)



import streamlit as st
from streamlit_folium import st_folium
import folium

# Title of the app
st.title("Interactive Map with Folium")

# Create a Folium map centered on Vancouver, BC
m = folium.Map(location=[49.2827, -123.1207], zoom_start=12)

# Add a marker to the map
folium.Marker(
    location=[49.2827, -123.1207],
    popup="Vancouver, BC",
    tooltip="Click for more info"
).add_to(m)

st.write("Below is an interactive map centered on Vancouver:")
st_folium(m, width=725, height=500)