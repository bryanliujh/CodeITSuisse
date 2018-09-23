import logging
import math

from flask import request, jsonify

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/prime-sum', methods=['POST'])
def prime_sum():
    data = request.get_json()
    input_value = data.get("input")
    remain = input_value
    output = []
    check = 0
    if remain <= 0:
        output.append(remain)
    while remain > 0:
        if remain == 1:
            output[0] = output[0] - 1
            output.append(remain+1)
            break
        for big in range(remain, 1, -1):
            for i in range(2, int(math.sqrt(big))+1, 1):
                if big % i == 0:
                    check = 1
                    break
            if check == 0:
                output.append(big)
                remain = remain - big
                break
            else:
                check = 0
    return jsonify(output)
