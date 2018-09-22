import logging
import numpy as np

from flask import request, jsonify

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/machine-learning/question-1', methods=['POST'])
def kk():
    data = request.get_json()
    i = data.get("input")
    o = data.get("output")
    q = data.get("question")

    A = np.array([[i[0][0], i[0][1], i[0][2]],
                  [i[1][0], i[1][1], i[1][2]],
                  [i[2][0], i[2][1], i[2][2]],
                  [i[3][0], i[3][1], i[3][2]],
                  [i[4][0], i[4][1], i[4][2]]])

    B = np.array([o[0], o[1], o[2], o[3], o[4]])

    C = np.linalg.lstsq(A, B)[0]

    result = 0

    for i in range(0, 3):
        result += C[i] * q[i]

    return jsonify({
      "answers": result
    })