# Handwritten Digit Classification using TensorFlow (MNIST)

## Project Overview
This project is a Deep Learning-based handwritten digit classification system built using TensorFlow and trained on the MNIST dataset. The model predicts handwritten digits from **0 to 9** using a fully connected Artificial Neural Network (ANN).

The MNIST dataset contains grayscale images of handwritten digits where each image is of size **28×28 pixels**.

---

## Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- FastAPI
- Uvicorn
- Pydantic
- Streamlit
- PIL

---

## Dataset Information
The MNIST dataset consists of:

- 60,000 training images
- 10,000 testing images
- Image size: 28×28
- Total classes: 10 (digits 0–9)

Before training, the pixel values were normalized from **0–255** to **0–1** for better model performance.

---

## Model Architecture

The model was built using a Sequential Neural Network with the following architecture:

### Input Layer
- Flatten layer
- Converts input image from `(28, 28)` into a vector of `784`

### Hidden Layer 1
- Dense layer with **256 neurons**
- Activation Function: **ReLU**

### Hidden Layer 2
- Dense layer with **128 neurons**
- Activation Function: **ReLU**

### Output Layer
- Dense layer with **10 neurons**
- Activation Function: **Softmax**

### Architecture Flow

```text
Input (28×28)
      ↓
Flatten (784)
      ↓
Dense (256, ReLU)
      ↓
Dense (128, ReLU)
      ↓
Dense (10, Softmax)
```

---

## Training Details

- Optimizer: rmsprop
- Loss Function: sparse_categorical_crossentropy
- Evaluation Metric: Accuracy
- Epochs: 10

---

## Model Performance

After training and evaluation:

| Metric | Score |
|---|---|
| Training Accuracy | 99.54% |
| Testing Accuracy | 97.82% |

The model achieved **97.82% test accuracy** on unseen handwritten digit images.

---

## Backend Deployment

The backend API was developed using FastAPI with a `/predict` route and Deployed on Hugging Face. The trained TensorFlow model is loaded and used for prediction through API requests. Backend Deployed URL: https://muhammadnuman-mnist-backend-nouman.hf.space

---

## Frontend Deployment

The frontend of this project was developed using Streamlit and deployed successfully. The web application allows users to upload a handwritten digit image for prediction. Frontend Deployed URL: https://mnist-project-numan.streamlit.app/

### How it Works
1. The user uploads a handwritten digit image.
2. The image is preprocessed into a **28×28 grayscale format**.
3. Pixel values are normalized between **0 and 1**.
4. The processed image is sent to the FastAPI backend.
5. The trained TensorFlow model predicts the digit.
6. The predicted number is displayed on the screen.


## Project Workflow

The complete workflow of this project follows these steps:

1. **Dataset Loading**  
   The MNIST dataset was loaded using TensorFlow/Keras.

2. **Data Preprocessing**  
   - Images were normalized from `0–255` to `0–1`
   - Data was prepared for training and testing

3. **Model Building**  
   A Sequential Artificial Neural Network (ANN) was built with:
   - Flatten Layer `(28×28 → 784)`
   - Hidden Layer 1 `(256 neurons, ReLU)`
   - Hidden Layer 2 `(128 neurons, ReLU)`
   - Output Layer `(10 neurons, Softmax)`

4. **Model Training**  
   The model was trained on the MNIST training dataset.

5. **Model Evaluation**  
   The trained model was tested on unseen test data and achieved **97.82% test accuracy**.

6. **Model Saving**  
   The trained model was saved as `model.keras`.

7. **Backend Development**  
   A FastAPI backend was created with a `/predict` endpoint to load the model and make predictions.

8. **Backend Deployment**  
   The backend API was deployed for online prediction requests.

9. **Frontend Development**  
   A Streamlit frontend was created where users can upload handwritten digit images.

10. **Image Processing in Frontend**  
    The uploaded image is:
    - Converted into grayscale
    - Resized to `28×28`
    - Normalized into `0–1`

11. **Prediction Request**  
    The processed image is sent to the FastAPI backend.

12. **Prediction Result**  
    The backend predicts the digit and sends the result back to Streamlit.

13. **Result Display**  
    The predicted number is displayed to the user on the frontend.

---

### Workflow Summary

Dataset → Preprocessing → Model Building → Training → Evaluation → Save Model → Backend API → Frontend Upload → Image Processing → Prediction → Result Display
