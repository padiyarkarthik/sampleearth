import os
from flask import Flask,redirect,render_template,request
import pypyodbc
import time
#import random
import urllib
import datetime
#import json
#import redis

app = Flask(__name__)


server = 'kpmaster.database.windows.net'
database = 'kpmaster'
username = 'kpmaster'
password = 'karu@1965'
driver= '{ODBC Driver 13 for SQL Server}'
   
def disdata():
   cnxn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
   cursor = cnxn.cursor()
   start = time.time()
   cursor.execute("SELECT TOP 10 * FROM [equake]")
   row = cursor.fetchall()
   end = time.time()
   executiontime = end - start
   return render_template('searchearth.html', ci=row, t=executiontime)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/displaydata', methods=['POST'])
def display():
    return disdata() 

if __name__ == '__main__':
  app.run()
