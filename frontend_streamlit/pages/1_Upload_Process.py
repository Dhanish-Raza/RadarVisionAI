import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Radar Vision AI", page_icon="🛰️", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Center the title */
    .center-title {
        text-align: center;
        font-size: 2.2rem !important;
        font-weight: bold;
        color: #2E86C1;
        margin-bottom: 1rem;
    }
    /* Subheaders */
    .stSubheader {
        font-size: 1.3rem !important;
        font-weight: 600;
        color: #1A5276;
    }
    /* Add padding to images */
    .stImage > img {
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 1rem;
        background-color: #2E86C1;
        color: white;
        border: none;
    }
    .stButton > button:hover {
        background-color: #1B4F72;
        color: #f2f2f2;
    }
    /* Download button */
    .stDownloadButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 1rem;
        background-color: #28B463;
        color: white;
        border: none;
    }
    .stDownloadButton > button:hover {
        background-color: #1D8348;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 class='center-title'>📤 Radar Vision AI</h1>", unsafe_allow_html=True)

# --- Initialize session state ---
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "processed" not in st.session_state:
    st.session_state.processed = False

# --- Pre-fed image path ---
pre_fed_image_path = "assets/sample_colorized.png"  # Replace with your image path
pre_fed_img = Image.open(pre_fed_image_path).convert("RGB")

# --- Max width for images ---
MAX_IMAGE_WIDTH = 320  # pixels

# =======================
# STEP 1: UPLOAD + PREVIEW
# =======================
if not st.session_state.processed:
    uploaded_file = st.file_uploader(
        "Upload SAR Image (GeoTIFF / PNG)", 
        type=["tif", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
        uploaded_img = Image.open(uploaded_file).convert("RGB")

        st.subheader("📷 SAR Image")
        st.image(uploaded_img, width=MAX_IMAGE_WIDTH, output_format="PNG")

        # Centered Colorize button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Colorize Image"):
                st.session_state.processed = True
                st.rerun()

# =======================
# STEP 2: COMPARISON VIEW
# =======================
elif st.session_state.processed and st.session_state.uploaded_file is not None:
    uploaded_img = Image.open(st.session_state.uploaded_file).convert("RGB")

    st.subheader("🎨 Comparison")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("**SAR Image**")
        st.image(uploaded_img, width=MAX_IMAGE_WIDTH, output_format="PNG")
    with col2:
        st.markdown("**Colorized Image**")
        st.image(pre_fed_img, width=MAX_IMAGE_WIDTH, output_format="PNG")

    # Download button for pre-fed image
    buf = io.BytesIO()
    pre_fed_img.save(buf, format="PNG")
    st.download_button(
        "⬇️ Download Colorized Image",
        data=buf.getvalue(),
        file_name="colorized_image.png",
        mime="image/png"
    )

    # Reset button to upload new image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Upload New Image"):
            st.session_state.uploaded_file = None
            st.session_state.processed = False
            st.rerun()
