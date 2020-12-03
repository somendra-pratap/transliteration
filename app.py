from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return "स्वागत है"


@app.route('/hi')
def who():
    return "तुम कौन हो ?"


@app.route('/hi/<username>')
def greet(username):
    return "नमस्ते, बड़े भाई!"