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
    result = inputString
    word_count = Counter(inputString)
    maxi = max(word_count.values())
    for k, v in word_count.items():
        if v == maxi:
            result = k
            break
    logging.info("My result :{}".format(result))
    return json.dumps(word_count);