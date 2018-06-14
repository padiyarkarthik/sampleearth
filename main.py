import os
import ibm_db
from flask import Flask,redirect,render_template,request
import urllib
import datetime
import json
import pypyodbc
import time
	
app = Flask(__name__)

def disdata():
   server = 'sham05.database.windows.net'
   database = 'sqldb'
   username = 'sham05'
   password = '1qaz!QAZ'
   driver= '{ODBC Driver 13 for SQL Server}'
   cnxn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
   cursor = cnxn.cursor()
   start = time.time()
   cursor.execute("SELECT TOP 10000 * FROM [earth_data]")
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
