from http.client import responses
import json
from operator import sub
import flask
from flask import Flask,redirect, url_for, request,render_template,send_file,jsonify
import werkzeug
from werkzeug.utils import secure_filename
from flask import Flask, Response
from flask_cors import CORS,cross_origin
from flask import send_from_directory
import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import datetime
import pathlib
import os
import requests
import pymongo
from datetime import datetime


PORT=4000
app=Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app,support_credentials=True)


myclient = pymongo.MongoClient("mongodb://shiridikumar:2002meshiridi@cluster0-shard-00-00.qozki.mongodb.net:27017,cluster0-shard-00-01.qozki.mongodb.net:27017,cluster0-shard-00-02.qozki.mongodb.net:27017/cp-map?ssl=true&replicaSet=atlas-z43jla-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = myclient["cp-map"]

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route("/signin",methods=["POST"])
@cross_origin(supports_credentials=True,origin='*')
def signin():
    data =json.loads(request.data)
    email=data["email"]
    password=data["password"]
    return 200


@app.route("/register",methods=["POST"])
@cross_origin(supports_credentials=True,origin='*')
def register():
    data =json.loads(request.data)
    email=data["email"]
    username=data["user"]
    phone=data["phone"]
    ins_name=data["ins_name"]
    dob=data["dob"]
    gender=data["gender"]
    password=data["password"]
    dt_obj= datetime.strptime(dob[2:], '%y-%m-%d')
    user={
        "username":username,
        "email":email,
        "gender":gender,
        "mobile":phone,
        "dob":dt_obj,
        "institute_name":ins_name,
        "password":password
    }
    check=mydb.users.find_one({"email":email})
    if(check==None):
        mydb.users.insert_one(user)
        print(dt_obj,type(dt_obj))
    else:
        return "500"

    return "200"





if __name__=="__main__":
    app.run(debug=True,port=4000)