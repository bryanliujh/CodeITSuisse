import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

n = 0
nn = 0

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

    '''
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
    '''


    fora = """'{0:0""" + str(types) + """b}'"""
    num_count = 0
    num_count_n = 0
    fixed = types

    good = 0
    sum = 0
    sumsum = 0

    x = 0
    y = types

    counter = 2**types
    counter2 = 2**types

    while counter > 0:
        for i in range(x, types):
            x = int(return_bit(fora)[num_count % fixed])
            sum += twod_list[i][x]
            num_count += 1
            # sum += twod_list[i][int(binary_list[bit_count])]
            # print("bit_count: %s" % bit_count)
            # bit_count += 1

        while counter2 > 0:
            for j in range(y, types*2):
                y = int(return_bit_n(fora)[num_count_n % fixed])
                sumsum += twod_list[j][y]
                num_count_n += 1
                # sumsum += twod_list[j][int(another_binary_list[another_bit_count])]
                # print("another_bit_count: %s" % another_bit_count)
                # another_bit_count += 1
            if abs(sum - sumsum) <= max_diff:
                good += 1
            y = types
            sumsum = 0
            counter2 -= 1

            global nn
            nn += 1

        # another_bit_count = 0
        num_count_n = 0
        x = 0
        sum = 0
        counter -= 1
        counter2 = 2**types
        nn = 0

        global n
        n += 1

    return jsonify({
      "result": good % 100000123
    })


def return_bit(fora):
    global n
    bit_string = fora.format(n)
    new_bit_string = bit_string.replace("'","")
    return new_bit_string


def return_bit_n(fora):
    global nn
    bit_string = fora.format(nn)
    new_bit_string = bit_string.replace("'","")
    return new_bit_string
