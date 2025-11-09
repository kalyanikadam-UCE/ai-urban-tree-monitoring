import streamlit as st

st.title("🌳 AI Powered Urban Tree Monitoring")
st.write("Upload a tree image to analyze its health.")

uploaded = st.file_uploader("Upload Tree Image", type=["jpg", "png", "jpeg"])

if uploaded:
    st.image(uploaded, caption="Uploaded Image", use_column_width=True)
    st.write("🔍 Analyzing tree health...")
    st.success("Health Status: Example Output (Model Coming Soon)")
