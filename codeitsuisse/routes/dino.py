import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/two-dinosaurs', methods=['POST'])
def dino():
    data = request.get_json()
    types = data.get("number_of_types_of_food")

    raphcals = data.get("calories_for_each_type_for_raphael")
    r_list = list(raphcals)

    leocals = data.get("calories_for_each_type_for_leonardo")
    l_list = list(leocals)

    mergedlist = r_list + l_list

    max_diff = data.get("maximum_difference_for_calories")

    if (max_diff < 0) or (max_diff > 200000):
        end()

    if (types < 0) or (types > 200):
        end()

    k = 0
    twod_list = []
    for i in range(0, types*2):
        twod_list_two = []
        for j in range(0, 2):
            if j == 0:
                twod_list_two.append(mergedlist[k])
                k += 1
            if j == 1:
                twod_list_two.append(0)
        twod_list.append(twod_list_two)

    for i in range(0, types*2):
        for j in range(0, 2):
            if (twod_list[i][j] < 0) or (twod_list[i][j] > 2000):
                end()

    bit_string = ""
    j = """'{0:0""" + str(types) + """b}'"""
    for i in range(0, 2**types):
        bit_string += j.format(i)
        new_bit_string = bit_string.replace("'","")

    binary_list = []
    for i in str(new_bit_string):
        binary_list.append(i)

    bit_count = 0
    another_binary_list = binary_list.copy()
    another_bit_count = 0

    good = 0
    sum = 0
    sumsum = 0

    x = 0
    y = types

    counter = 2**types
    counter2 = 2**types

    while counter > 0:
        for i in range(x, types):
            sum += twod_list[i][int(binary_list[bit_count])]
            bit_count += 1

        while counter2 > 0:
            for j in range(y, types*2):
                sumsum += twod_list[j][int(another_binary_list[another_bit_count])]
                another_bit_count += 1
            if abs(sum - sumsum) <= max_diff:
                good += 1
            y = types
            sumsum = 0
            counter2 -= 1

        another_bit_count = 0
        x = 0
        sum = 0
        counter -= 1
        counter2 = 2**types

    return jsonify(good % 100000123);


