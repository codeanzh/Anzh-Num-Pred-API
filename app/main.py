from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()
import os
from API.test import x

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get('name', None)

    if not name:
        return f"Not Found {x}"

    return f"Data you send {name}"