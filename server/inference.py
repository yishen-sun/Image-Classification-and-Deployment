
from flask import Flask, request, jsonify
import base64, os
from src.inference import Inference
from flask_cors import CORS, cross_origin
# Load the model
infer = Inference()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def getFileList(dir, Filelist, ext=None):
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)
    
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            getFileList(newDir, Filelist, ext)
 
    return Filelist
 


@app.route('/api', methods=['POST'])
@cross_origin()
def predict():
    f = request.files['static_file']
    f.save(os.path.join("./data", f.filename))
    predict = infer(os.path.join("./data", f.filename))
    return predict, 200

@app.route('/api', methods=['GET'])
@cross_origin()
def predict1():
    imglist = getFileList("./data", [], 'jpg')
    predicts = []
    for imgpath in imglist:
        #print(imgpath)
        #imgname = os.path.splitext(os.path.basename(imgpath))[0]
        predicts.append([imgpath, infer(imgpath)])
    return jsonify(predicts), 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
