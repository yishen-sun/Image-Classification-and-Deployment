
from flask import Flask, request, jsonify
import base64, os
from src.inference import Inference
from flask_cors import CORS, cross_origin
# Load the model
infer = Inference()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api', methods=['POST'])
@cross_origin()
def predict():
    f = request.files['static_file']
    f.save(os.path.join("./data", f.filename))
    predict = infer(os.path.join("./data", f.filename))
    return predict, 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
