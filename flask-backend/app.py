import os
import functools
from flask import Flask, flash, session, redirect, url_for, request, render_template, current_app, jsonify, send_file
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from flask_restplus import Api, Resource, fields

import json
import logging

from similarity_function import *

def file_cmp(a, b):
  mod_a = a.split('_')
  mod_b = b.split('_')
  if int(mod_a[1]) <= int(mod_b[1]):
    return -1
  else:
    return 1


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
api = Api(app=app)
ns = api.namespace('vbs', description='design vbs web')

client = MongoClient('mongo', 27017)
db = client.testdb
col = db.video

root_dir = '/flask-backend'
data_dir = '/keyframes/'

@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
@ns.route("/")
class indexClass(Resource):
  def post(self):
    _items = col.find()
    items = [item for item in _items]
    #return render_template('index.html', items=items)
    return current_app.logger.info(items)
 
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
@ns.route("/getData")
class getDataClass(Resource):
  def post(self):
    current_app.logger.info("getData called with data")
    returnList = {"data": []}
    if os.path.isdir(data_dir):
      current_app.logger.info("Image dir exists and it is %s" % data_dir)
    else:
      current_app.logger.info("Image dir does not exists")
    import glob

    # for filename in glob.iglob(data_dir + '**/*', recursive=True):
    #     print(filename)
    # for root, subFolders, files in os.walk(data_dir):
    #   current_app.logger.info("Hi")
    #   current_app.logger.info(subFolders)
    folder_list = os.listdir(data_dir)
    folder_list.sort()
    current_app.logger.info(folder_list)

    fileList = []
    template_file_element = {"path": '', "similarity": 0, "isLast": True}
    for subFolder in folder_list:
      absoluteSubFolder = data_dir + subFolder + '/'
      tmpfileList = os.listdir(absoluteSubFolder)
      tmpfileList = sorted(tmpfileList, key=functools.cmp_to_key(file_cmp))
      tmpfileList = [{"path": absoluteSubFolder + s, "similarity": 0, "isLast": True, "isRepresentative": False} for s in tmpfileList]
      fileList = fileList + tmpfileList
    
    fileList = fileList[0:1000]
    # Measure similarity
    for i in range (len(fileList) - 1):
      # Check if current keyFrame is Last frame in video
      curFrameVideo = fileList[i]["path"].split('/')[2]
      nextFrameVideo = fileList[i+1]["path"].split('/')[2]
      if curFrameVideo != nextFrameVideo:
        # current_app.logger.info("Different folder (video) (%s vs %s)" % (curFrameVideo, nextFrameVideo))
        continue
      
      
      # Check similarity between two frames
      similarity = mse_grayscale(fileList[i]["path"], fileList[i+1]["path"])
      fileList[i]["similarity"] = similarity
      fileList[i]["isLast"] = False

      if i % 100 == 0:
        current_app.logger.info("Processing: (%d/%d) done" % (i, len(fileList)))
    
    # Change name for react
    # fileList = [{"path": '../..' + s["path"], "similarity": s["similarity"], "isLast": s["isLast"], "isRepresentative": s["isRepresentative"]} for s in fileList]
      

    # current_app.logger.info(fileList)
    # returnList["data"] = fileList
    # response = jsonify(returnList)
    response = jsonify(fileList)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response




if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
