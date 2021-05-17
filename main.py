from eval_model import cap 
from flask import Flask, render_template, request, jsonify,Response
import cv2
import numpy as np
import jsonpickle
app = Flask(__name__)
@app.route('/uploads', methods=['POST'])
def test():
    r = request
    
    #filename = secure_filename(file.filename)
    #file.save(os.path.join(app.config['upload_folder'], filename))    
    
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    filename = 'savedImage.jpg'
    cv2.imwrite(filename, img)    
    desc = cap(filename)
    print(desc)
    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    response = Response("{}".format(desc), content_type='text/plain')
    return response
app.run(host="0.0.0.0", port=80, debug=True)