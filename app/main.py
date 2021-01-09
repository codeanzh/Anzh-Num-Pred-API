from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
from API.model import predict

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    name = request.args.get('name', None)

    if not name:
        return "No Data Sent"

    return f"Data you send {name}"

@app.route("/sendData", methods=['post'])
def imageData():
    JSON = request.get_json()
    data_url = JSON['imgData'].split(",")[1]
    img_bytes = base64.b64decode(data_url)
    img = Image.open(BytesIO(img_bytes))
    img = np.array(img)
    img = img[:, :, 3:4].reshape(300, 300)
    img = cv2.resize(img, (28, 28))/255
    img = img.reshape(784, 1)

    return str(predict(img)), 200