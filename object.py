import streamlit as st
import requests
from PIL import Image, ImageDraw
import io

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to query the model
def query_image(image_file):
    # Ensure the image is sent as a binary file object
    files = {"file": image_file}
    response = requests.post(API_URL, headers=headers, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Draw bounding boxes on the image
def draw_boxes(image, predictions):
    draw = ImageDraw.Draw(image)
    for pred in predictions:
        # Extract the box coordinates and label
        box = pred["box"]  # Expected format: [x1, y1, x2, y2]
        label = pred["label"]
        score = pred["score"]
        
        # Draw the bounding box
        draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline="red", width=2)
        # Add a label with the confidence score
        draw.text((box[0], box[1] - 10), f"{label} ({score:.2f})", fill="red")
    return image

# Streamlit UI
def objectpage():
    st.title("Object Detection with Hugging Face DETR")
    st.write("Upload an image to detect objects using the Facebook DETR model.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Convert the uploaded file to an image and also read it as bytes
        image = Image.open(uploaded_file).convert("RGB")
        
        # Read the image file into a binary object for API request
        image_bytes = uploaded_file.read()

        # Query the Hugging Face model
        with st.spinner("Processing..."):
            output = query_image(io.BytesIO(image_bytes))  # Send the image as file-like object

        # Display the results
        if output:
            # Ensure predictions are present in the response
            if "outputs" in output:
                predictions = []
                for pred in output["outputs"][0]["instances"]:
                    # Process bounding box coordinates
                    box = pred["bbox"]  # Bounding box in format [x1, y1, x2, y2]
                    label = pred["label"]  # Label for the detected object
                    score = pred["score"]  # Confidence score
                    predictions.append({"box": box, "label": label, "score": score})
                
                st.success("Object detection complete!")
                image_with_boxes = draw_boxes(image, predictions)
                st.image(image_with_boxes, caption="Detected Objects", use_container_width=True)
            else:
                st.error("No objects detected. Please try again.")

# Run the Streamlit app
if __name__ == "__main__":
    objectpage()
