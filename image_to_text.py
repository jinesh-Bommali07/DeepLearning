import streamlit as st
import requests
from PIL import Image

# API details
API_URL = "https://api-inference.huggingface.co/models/Falconsai/nsfw_image_detection"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query_image(file_data):
    try:
        response = requests.post(API_URL, headers=headers, data=file_data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while making the request: {e}")
        return None

# Streamlit UI
def image_to_textpage():
    st.title("Image Detection")
    st.write("Upload an image to check if it is safe for work.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)

            # Call the API
            with st.spinner("Analyzing the image..."):
                response = query_image(uploaded_file.getvalue())

            # Display the result
            if response:
                st.write("### Detection Results")
                st.json(response)  # Display raw response for debugging
            else:
                st.error("Failed to process the image. Please try again.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    image_to_textpage()
