import logging

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/airtrafficcontroller', methods=['POST'])
def air_traffic_controller():
    data = request.get_json()
    logging.info(data)
    flights = data.get("Flights")
    logging.info(flights)
    static = data.get("Static")
    logging.info(static)
    reserve_time = static['ReserveTime']
    if len(static) == 2:
        runways = static['Runways']
        logging.info(runways)
    logging.info(reserve_time)
    reserve_minute = int(reserve_time) / 60
    sorted_flights = sorted(flights, key=lambda i: i['Time'])
    logging.info(sorted_flights)
    i = 0
    while i < len(sorted_flights):
        hour_i = str(sorted_flights[i]["Time"])[0:2]
        minute_i = str(sorted_flights[i]["Time"])[2:]
        limit_minute = int(minute_i) + reserve_minute
        limit_hour = int(hour_i)
        if limit_minute > 60:
            limit_minute = limit_minute - 60
            limit_hour = limit_hour + 1
        if limit_hour < 10:
            limit_hour_str = '0' + str(limit_hour)
        else:
            limit_hour_str = str(limit_hour)
        if limit_minute < 10:
            limit_minute_str = '0' + str(limit_minute)
        else:
            limit_minute_str = str(limit_minute)
        limit_time = limit_hour_str + limit_minute_str
        j = i + 1
        while j < len(sorted_flights):
            if str(sorted_flights[j]["Time"]) < limit_time:
                sorted_flights[j]["Time"] = limit_time
            else:
                break
        i = i + 1
    logging.info(sorted_flights)
    output = {"Flights": sorted_flights}

    return jsonify(output)
