import logging
import json
import exifread
from PIL import Image
import requests
from io import BytesIO


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/imagesGPS', methods=['POST'])
def image_gps():
    data = request.get_json()

    #inputValue = data.get("path")

    json_array = json.load(data)

    for my_item in json_array:
        jsonitem = my_item['path']

    teststring = str(jsonitem)


    return teststring;


