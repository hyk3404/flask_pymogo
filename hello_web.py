#!flask/bin/python
from flask import Flask,url_for,request
import requests
import json
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NFCdata"]

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route ('/user1') 
def  user1 ():
    timelist = []
    count = 0
    user1_col = mydb["user1"]
    for x in user1_col.find() :
        count += 1
        timelist.append(x['time'])
    
    print(json.dumps(timelist))
    return json.dumps(timelist)

@app.route ('/user2') 
def  user2 ():
    timelist = []
    count = 0
    user2_col = mydb["user2"]
    for x in user2_col.find() :
        count += 1
        timelist.append(x['time'])
    
    print(json.dumps(timelist))
    return json.dumps(timelist)

@app.route ('/user3') 
def  user3 ():
    timelist = []
    count = 0
    user3_col = mydb["user3"]
    for x in user3_col.find() :
        count += 1
        timelist.append(x['time'])
    
    print(json.dumps(timelist))
    return json.dumps(timelist)

@app.route('/test_dashboard')
def test():
    r = requests.get("http://127.0.0.1:5000/user1")
    # data = r.json()
    # a = json.dumps(data)
    b = json.loads(r.text)
    print("===============")
    print(b)
    print("===============")
    return r.text

if __name__ == '__main__':
    app.run(host='127.0.0.1')

