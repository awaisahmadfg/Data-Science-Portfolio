from flask import Flask, render_template, request
import numpy as np
import re
import base64
from PIL import Image
from io import BytesIO

import sys 
import os
sys.path.append(os.path.abspath("./model-new"))
from load import *

app = Flask(__name__)
global model, graph, sess
model, graph, sess = init()
print(model, graph)
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['GET','POST'])
def predict():
    class_mapping = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt'
    
    # get data from drawing canvas and save as image
    decoded = parseImage(request.get_data())

    # read parsed image back in 8-bit, black and white mode (L)
    x = Image.open(BytesIO(decoded))
    
    #x = Image.composite(x, Image.new('RGB', x.size, 'white'), x)
    x = x.convert('L')  
    x = x.resize((28, 28), Image.ANTIALIAS)  
    x = 1 - np.array(x, dtype=np.float32) / 255.0
    
    # reshape image data for use in neural network
    x = x.reshape(1,28,28,1)

    #sess = tf.Session()
    #graph = tf.get_default_graph()
    print(graph)

    with graph.as_default():
        set_session(sess)
        out = model.predict(x)
        print(out)
        print(np.argmax(out, axis=1))
        
        res = class_mapping[np.argmax(out, axis=1)[0]]
        print(res)
        #response = np.array_str(res)
        response = res
        return response
    
def parseImage(imgData):
    # parse canvas bytes and save as output.png
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    #with open('output.png','wb') as output:
    #    output.write(base64.decodebytes(imgstr))
    #imgdata = imgstr.split(',')[1]
    #imgData = imgData.split("base64,")[1]
    decoded = base64.decodebytes(imgstr)
    return decoded


if __name__ == '__main__':
    app.debug = False
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)