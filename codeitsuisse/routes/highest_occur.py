import logging
import json

from flask import request, jsonify;
from collections import Counter;
from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/higho', methods=['POST'])
def check():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputString = data.get("string")
    word_count = Counter(inputString)
    maxi = max(word_count.values())
    i = word_count.values().index(maxi)
    result = word_count.items()[i]
    logging.info("My result :{}".format(result))
    return jsonify(result);