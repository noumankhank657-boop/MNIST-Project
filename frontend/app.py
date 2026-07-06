import streamlit as st
import numpy as np
import requests
from PIL import Image

BASE_URL = "https://muhammadnuman-mnist-backend-nouman.hf.space"

st.set_page_config(page_title="Digit Recognizer", page_icon="🔢", layout="centered")

st.title("Handwritten Digit Recognizer")
st.caption("Upload a clear image of a handwritten digit (0-9) and let the model predict it.")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Upload Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("L")
        image_resized = image.resize((28, 28))
        st.image(uploaded_file, caption="Your uploaded image", use_container_width=True)

with col2:
    st.subheader("Prediction Result")

    if uploaded_file is None:
        st.info("Upload an image on the left to get started.")
    else:
        predict_btn = st.button("Predict Digit", use_container_width=True, type="primary")

        if predict_btn:
            with st.spinner("Analyzing your digit..."):
                img_array = np.array(image_resized) / 255.0
                img_list = img_array.tolist()

                try:
                    response = requests.post(
                        f"{BASE_URL}/predict",
                        json={"data": img_list}
                    )

                    if response.status_code == 200:
                        result = response.json()
                        if "predicted_class" in result:
                            predicted = result["predicted_class"]
                            st.success("Prediction Complete!")
                            st.metric(label="Predicted Digit", value=predicted)
                        else:
                            st.error("Model could not recognize the digit.")
                    else:
                        st.error(f"Server error: Status {response.status_code}")

                except requests.exceptions.ConnectionError:
                    st.error("Cannot connect to the server. Make sure FastAPI is running.")

st.divider()
st.caption("Model: ANN trained on MNIST Dataset")