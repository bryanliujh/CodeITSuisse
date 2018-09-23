import logging

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/minimum-camps', methods=['POST'])
def minimum_camps():
    data = request.get_json()
    logging.info(data)
    person_range = []
    for p in data:
        pos = p['pos']
        distance = p['distance']
        this_range = {}
        this_range['left'] = pos - distance
        this_range['right'] = pos + distance
        person_range.append(this_range)
        logging.info(person_range)
    sorted_range = sorted(person_range, key=lambda i: i['left'])
    logging.info(sorted_range)
    intersaction = []
    i = 0
    while i < len(sorted_range):
        if sorted_range[i]['right'] == sorted_range[i+1]['left']:
            intersaction.append(sorted_range[i]['right'])
        elif sorted_range[i]['right'] > sorted_range[i+1]['left']:
            for j in range(sorted_range[i+1]['left'], sorted_range[i]['right']+1):
                intersaction.append(j)
    return jsonify(1)
