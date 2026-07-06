import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model

class InputData(BaseModel):
    data: list

app = FastAPI()
model = load_model('model.keras')

@app.get("/")
def home():
    return {"message": "Welcome to the ANN MNIST Dataset API!"}

@app.post("/predict")
def predict(input_data: InputData):
    input_array = np.array(input_data.data).reshape(1, 28, 28)
    prediction = model.predict(input_array)
    predicted_class = prediction.argmax()
    return {"predicted_class": int(predicted_class)}