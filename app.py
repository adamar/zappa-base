#!/usr/bin/python

import logging
from flask import Flask, request, jsonify, render_template, redirect
from zappa.async import task

import os
import pprint

import json
import slib
import time
import datetime
import boto3


app = Flask(__name__, static_url_path='/static')
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



@app.route('/', methods=['GET'])
def main_route():

    return render_template('index.html')


@app.route('/', methods=['POST'])
def main_post_route():

    print request.form['url']
    return redirect("/", code=302)

    
if __name__ == '__main__':
    #if LOCAL == True:
    #    print "Litetninng oin port 8080"
    #    app.run(host='0.0.0.0', port=8080, debug=True)
    #else:
    #    app.run(debug=True)
    app.run(debug=True)
