import logging
import json
import exifread
from PIL import Image
import requests
import os.path
import random
from codeitsuisse.routes import ImageMetaData
import urllib.request
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/imagesGPS', methods=['POST'])
def image_gps():





    data = request.get_json()
    mydict = {}
    myarr = []
    i = 0
    for my_item in data:
        jsonitem = my_item['path']
        file_name = random.randrange(1,10000)


        full_file_name = str(file_name) + '.jpg'
        script_dir = os.path.join(os.path.dirname(__file__), full_file_name)

        myimg = urllib.request.urlretrieve(jsonitem, script_dir)
        #full_file_name = 'testgeo.jpg'
        meta_data = ImageMetaData.ImageMetaData(script_dir)
        latlng = meta_data.get_lat_lng()
        latitude = latlng[0]
        longitude = latlng[1]
        mydict['lat'] = latitude
        mydict['lon'] = longitude
        myarr.append(mydict.copy())
    teststring = jsonify(myarr)



    return teststring;


