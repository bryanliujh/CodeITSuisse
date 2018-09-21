import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

@app.route('/bryan', methods=['POST'])
def evaluate():


    return jsonify(username="bryan",
                   email="bryan@gmail.com",
                   id="bryan_id");



