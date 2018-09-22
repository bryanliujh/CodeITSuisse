import logging
from codeitsuisse import  app
from codeitsuisse.routes import square
from codeitsuisse.routes import bryan
logger = logging.getLogger(__name__)
import logging
import json
import exifread
from PIL import Image
import requests
from io import BytesIO

from flask import request, jsonify;

@app.route('/', methods=['GET'])
def default_route():
    #data = request.get_json()
    #inputValue = data.get("path")


    teststr = "hi"

    return jsonify(teststr);

if __name__ == "__main__":
    logFormatter = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(lineno)d] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()

    rootLogger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("team.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    logger.info("Starting application ...")

    app.run(debug=True)

