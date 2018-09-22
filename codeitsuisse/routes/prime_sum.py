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
    while remain > 0:
        if remain == 1:
            output.append(remain)
            break
        for big in range(remain, 1, -1):
            logging.info(math.sqrt(big))
            for i in range(2, int(math.sqrt(big))+1, 1):
                logging.info(i)
                if big % i == 0:
                    logging.info("yes")
                    check = 1
                    logging.info(check)
                    break
            logging.info(check)
            if check == 0:
                logging.info("big is  prime")
                output.append(big)
                remain = remain - big
                break
            else:
                logging.info("big is not prime")
                check = 0
    return jsonify(output)
