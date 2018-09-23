import logging
import math

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/prime-sum', methods=['POST'])
def prime_sum():
    data = request.get_json()
    logging.info(data)
    input_value = data.get("input")
    remain = input_value
    output = []
    check = 0
    if remain == 0:
        output.append(remain)
    if remain < 0:
        remain = -remain
    while remain > 0:
        if remain == 1 and input_value > 0:
            output.append(remain)
            break
        elif remain == 1 and input_value < 0:
            output.append(-remain)
            break
        for big in range(remain, 1, -1):
            for i in range(2, int(math.sqrt(big))+1, 1):
                if big % i == 0:
                    check = 1
                    break
            if check == 0:
                if input_value > 0:
                    output.append(big)
                    remain = remain - big
                    break
                elif input_value < 0:
                    output.append(-big)
                    remain = remain - big
                    break
            else:
                check = 0
    return jsonify(output)
