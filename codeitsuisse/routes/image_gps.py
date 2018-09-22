import logging
import json
import exifread
from PIL import Image
import requests
from io import BytesIO


from flask import request, jsonify;

from codeitsuisse import app;

@app.route('/imagesGPS', methods=['POST'])
def image_gps():
    data = request.get_json()
    #inputValue = data.get("path")

    #json_object = json.load(data)
    #jsonitem = json_object[0]['path']


    return data;


