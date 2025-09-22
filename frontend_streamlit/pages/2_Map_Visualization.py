import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Radar Vision AI - Map", page_icon="🗺️", layout="wide")

st.title("🗺️ Map Visualization")

# Create folium map
m = folium.Map(location=[20, 78], zoom_start=5, tiles="CartoDB positron")

# Add a marker
folium.Marker(
    [28.6, 77.2],
    popup="📍 New Delhi - SAR Sample",
    tooltip="Click for details"
).add_to(m)

# Render map in Streamlit
st_data = st_folium(m, use_container_width=True, height=500)

# Add description below
st.markdown(
    """
    🔍 Toggle between **SAR grayscale**, **AI Colorized**, and **Optical Reference** 
    (future integration planned).
    """
)
