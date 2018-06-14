from flask import Flask,redirect,render_template,request
import pypyodbc
import time
import random
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
   cnxn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
   cursor = cnxn.cursor()
   start = time.time()
   for i in range(0,int(num)):
       magnitude = round(random.uniform(rangfro,rangto),2)
       sqlNum = "SELECT * FROM [earth_data] where mag="+str(magnitude)
       cursor.execute(sqlNum)
   end = time.time()
   executiontime = end - start
   return render_template('count.html',t=executiontime)

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
