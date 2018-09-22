import logging
import math
import json

from flask import request, jsonify

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/airtrafficcontroller', methods=['POST'])
def air_traffic_controller():
    data = request.get_json()
    flights = data.get("Flights")
    logging.info(flights)
    static = data.get("Static")
    logging.info(static)
    reserve_time = static['ReserveTime']
    logging.info(reserve_time)
    reserve_minute = reserve_time / 600
    flights_time = []
    i = 0
    for f in flights:
        flights_time[i] = f['Time']
        i = i + 1
    flights_time.sort()
    j = 0
    sorted_flights = {}

    return jsonify(1)
