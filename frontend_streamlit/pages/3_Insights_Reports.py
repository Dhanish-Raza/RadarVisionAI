import streamlit as st

st.title("📊 Insights & Reports")

st.markdown("### 🤖 AI Assistant (Prototype)")
user_q = st.text_input("Ask: What does this image show?")
if user_q:
    st.info("This area has dense vegetation on the east, water bodies in the south, and urban settlement in the north.")

st.markdown("### 📥 Export Options")
col1, col2 = st.columns(2)
with col1:
    st.download_button("⬇️ Download as PNG", data=b"demo", file_name="output.png")
with col2:
    st.download_button("📑 Export Report as PDF", data=b"demo", file_name="report.pdf")
