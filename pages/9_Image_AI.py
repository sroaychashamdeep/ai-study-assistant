import streamlit as st
from PIL import Image
import numpy as np
import cv2
from utils.ai_service import analyze_image

st.set_page_config(page_title="Image AI", page_icon="📸")

st.title("📸 AI Image Analyzer")

st.markdown("Upload an image (notes, question, diagram)")

# ---------------- UPLOAD ----------------

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# ---------------- MAIN LOGIC ----------------

if uploaded_file:

    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    st.subheader("🧠 Processed Image")
    st.image(gray, use_column_width=True)

    # ---------------- ANALYZE BUTTON ----------------

    if st.button("Analyze Image"):

        with st.spinner("Analyzing..."):

            image_bytes = uploaded_file.read()
            response = analyze_image(image_bytes)

        st.subheader("🤖 AI Output")
        st.write(response)