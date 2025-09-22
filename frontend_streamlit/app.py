import streamlit as st
from PIL import Image

st.set_page_config(page_title="Radar Vision AI", page_icon="🛰️", layout="wide")

# --- Header ---
st.title("🌌 SAR Image Colorization – Unlocking Hidden Insights")
st.subheader("“From invisible radar scans to vivid, human-readable visuals.”")

# --- Hero Section ---
col1, col2 = st.columns(2)
with col1:
    sar_img = Image.open("assets/sample_sar.png").resize((400, 350))
    st.image(sar_img, caption="SAR (Grayscale)")
with col2:
    colorized_img = Image.open("assets/sample_colorized.png").resize((400, 350))
    st.image(colorized_img, caption="Colorized Output")

st.markdown(
    "<h4 style='text-align: center;'>Colorizing radar images for better disaster response, agriculture, and urban planning.</h4>",
    unsafe_allow_html=True
)

# --- CTA Button ---
col1, col2, col3 = st.columns([1,2,1])  # middle column wider
with col2:
    if st.button("🚀 Try It Now → Upload Your SAR Image"):
        st.switch_page("pages/1_Upload_Process.py")