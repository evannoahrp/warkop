from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, how are you?"

if __name__ == "__name__":
    print("Starting Python Flask Server For Warkop System")