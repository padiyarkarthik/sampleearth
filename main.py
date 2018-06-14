import os
from flask import Flask,redirect,render_template,request
import pypyodbc
import time
import random
import urllib
import datetime
import json

app = Flask(__name__)


server = 'sham05.database.windows.net'
database = 'sqldb'
username = 'sham05'
password = '1qaz!QAZ'
driver= '{ODBC Driver 13 for SQL Server}'
   
def disdata():
   cnxn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
   cursor = cnxn.cursor()
   start = time.time()
   cursor.execute("SELECT TOP 10000 * FROM [earth_data]")
   row = cursor.fetchall()
   end = time.time()
   executiontime = end - start
   return render_template('searchearth.html', ci=row, t=executiontime)

def randrange(rangfro=None,rangto=None,num=None):
    dbconn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()
    start = time.time()
    for i in range(0,int(num)):
    	mag= round(random.uniform(rangfro, rangto),2)
    	success="SELECT * from [earth_data] where mag>'"+str(mag)+"'"
    	cursor.execute(success)
    end = time.time()
    exectime = end - start
    return render_template('count.html', t=exectime)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/displaydata', methods=['POST'])
def display():
    return disdata() 

@app.route('/multiplerun', methods=['GET'])
def randquery():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    return randrange(rangfro,rangto,num) 	

if __name__ == '__main__':
  app.run()
