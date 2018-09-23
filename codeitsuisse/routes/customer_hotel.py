import logging
import json

from flask import request, jsonify

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/customers-and-hotel/minimum-distance', methods=['POST'])
def customer_hotel_dist():
    data = request.get_json()
    my_array = data
    my_sorted_array = sorted(my_array)
    min_diff = my_sorted_array[1] - my_sorted_array[0]
    for i in range(2,len(my_sorted_array)):
        min_diff = min(min_diff, my_sorted_array[i]-my_sorted_array[i-1])

    my_dic = {"answer": min_diff}

    return jsonify(my_dic)





