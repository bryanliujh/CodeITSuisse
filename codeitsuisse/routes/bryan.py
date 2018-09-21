import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

@app.route('/bryan', methods=['GET'])
def bryanliu():


    return jsonify(username="bryan",
                   email="bryan@gmail.com",
                   id="bryan_id");



