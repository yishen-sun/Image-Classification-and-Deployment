
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
    
    #data = request.form["base64"]
    # print(request)
    
    #imgdata = base64.b64decode(data)
    #file = open('/app/data/test.jpg','wb')
    #file.write(data)
    #file.close()
    # print(os.getcwd())
    # files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # for f in files:
    #     print(f)
    predict = infer(os.path.join("./data", f.filename))
    #print(predict)
    return predict, 200
    #print(data)
    
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #return "responsed!"
    #resp = {"success": True, "response": "file saved!"}
    #return jsonify(resp), 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
