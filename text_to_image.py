import streamlit as st

from huggingface_hub import InferenceClient
from PIL import Image
import io

# API configuration
API_MODEL = "ZB-Tech/Text-to-Image"
API_TOKEN = "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"  # Replace with your Hugging Face API token

# Initialize Inference Client
client = InferenceClient(model=API_MODEL, token=API_TOKEN)

# Streamlit UI
def text_to_imgpage():
    st.title("Text-to-Image Generator")
    st.write("Enter a text prompt to generate an image using the Hugging Face model.")

    # Input text prompt
    prompt = st.text_input("Enter your prompt:", placeholder="e.g., Astronaut riding a horse")

    if st.button("Generate Image"):
        if prompt:
            # Generate image
            with st.spinner("Generating image..."):
                try:
                    image = client.text_to_image(prompt)
                    st.image(image, caption="Generated Image", use_column_width=True)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a prompt.")

    # Footer
    st.markdown("---")
    st.write("Powered by [Hugging Face](https://huggingface.co) and Streamlit.")
