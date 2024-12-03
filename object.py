import streamlit as st
import requests
from PIL import Image, ImageDraw

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to query the model
def query_image(image_data):
    response = requests.post(API_URL, headers=headers, data=image_data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Draw bounding boxes on the image
def draw_boxes(image, predictions):
    draw = ImageDraw.Draw(image)
    for pred in predictions:
        box = pred["box"]
        label = pred["label"]
        score = pred["score"]
        draw.rectangle(box, outline="red", width=2)
        draw.text((box[0], box[1] - 10), f"{label} ({score:.2f})", fill="red")
    return image

# Streamlit UI
def objectpage():
    st.title("Object Detection with Hugging Face DETR")
    st.write("Upload an image to detect objects using the Facebook DETR model.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Convert image to bytes
        image = Image.open(uploaded_file).convert("RGB")
        image_data = uploaded_file.read()

        # Query the Hugging Face model
        with st.spinner("Processing..."):
            output = query_image(image_data)

        # Display the results
        if output:
            predictions = [
                {
                    "box": [box[0], box[1], box[2], box[3]],
                    "label": pred["label"],
                    "score": pred["score"],
                }
                for pred in output.get("outputs", [])
            ]
            st.success("Object detection complete!")
            image_with_boxes = draw_boxes(image, predictions)
            st.image(image_with_boxes, caption="Detected Objects", use_column_width=True)
