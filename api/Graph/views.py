from flask_restful import Resource
from flask import send_file
import os
  
class GraphImage(Resource):
    def get(self, image): 
        img_dir = "./static"
        img_path = os.path.join(img_dir, image)
        return send_file(img_path, mimetype='image/png')