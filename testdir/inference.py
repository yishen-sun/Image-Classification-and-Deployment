
from flask import Flask, request, jsonify
import base64, os
from flask_cors import CORS, cross_origin
# Load the model
#infer = Inference()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api', methods=['POST'])
@cross_origin()
def predict():
    f = request.files['static_file']
    f.save(os.path.join("./data", f.filename))
    #data = request.form["base64"]
    #print(data.content_length)
    #file = open('./test.jpg','w')
    #file.write(data)
    #file.close()
    #predict = infer(data)
    #return predict
    #print(data)
    resp = {"success": True, "response": "file saved!"}
    return jsonify(resp), 200
    
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return "responsed!"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
