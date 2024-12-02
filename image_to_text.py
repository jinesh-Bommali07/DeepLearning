import streamlit as st
import requests
from PIL import Image

# API details
API_URL = "https://api-inference.huggingface.co/models/Falconsai/nsfw_image_detection"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query_image(file):
    response = requests.post(API_URL, headers=headers, data=file)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error in API request.")
        return None

# Streamlit UI
def image_to_textpage():
    st.title("Image Detection")
    st.write("Upload an image to check if it is safe for work.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(Image.open(uploaded_file), caption="Uploaded Image", use_column_width=True)

        # Call the API
        with st.spinner("Analyzing the image..."):
            response = query_image(uploaded_file.getvalue())
        
        # Display the result
        if response:
            st.write("### Detection Results")
            st.json(response)
