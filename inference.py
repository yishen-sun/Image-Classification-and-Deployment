from src.inference import Inference
from flask import Flask, request, jsonify

# Load the model
infer = Inference()

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def predict():
    return infer("data/tmp_1903.jpg")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')