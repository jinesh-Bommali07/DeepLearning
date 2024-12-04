import streamlit as st
import requests
from PIL import Image

# Constants
API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
API_KEY = "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"  # Replace with your Hugging Face API key

headers = {"Authorization": f"Bearer {API_KEY}"}

# Function to query Hugging Face API
def query(image_file):
    response = requests.post(API_URL, headers=headers, data=image_file)
    return response.json()

# Streamlit app
def objectpage():
    st.title("Object Detection with Hugging Face")

    st.write(
        """
        This app uses the Hugging Face DETR ResNet-50 model for object detection. Upload an image to see the model's predictions!
        """
    )

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        with st.spinner("Processing..."):
            # Convert image to binary for API
            image_bytes = uploaded_file.getvalue()
            result = query(image_bytes)

        st.subheader("Detection Results")
        if isinstance(result, list):
            for obj in result:
                label = obj.get("label", "Unknown")
                score = obj.get("score", 0)
                st.write(f"- **{label}**: {score:.2%}")
        else:
            st.error("An error occurred while processing the image.")

        st.write("### Raw Output")
        st.json(result)

