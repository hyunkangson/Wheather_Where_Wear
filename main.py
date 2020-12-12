from flask import Flask, render_template, request, url_for
from flask import request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from urllib.request import urlopen
import json, sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html');

@app.route('/userpage',methods=['POST'])
def userpage():
    request.form['bbtn']
    return  render_template('userpage.html');

@app.route('/DataAddition',methods=['POST'])
def DataAddition():
    request.form['ddata']
    return  render_template('DataAddition.html');

@app.route('/result',methods = ['POST'])
def result():
    #weather api
   location=request.form['location']
   url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&mode=json&APPID=ad91812895dfa17a92a11504c0718122'
   data = urlopen(url).read()
   a = json.loads(data)
   we = (a['weather'][0]['main'])
   ce = round(a['main']['temp'] - 273.15,1)
   icon = a['weather'][0]['icon']

   #database
   con=sqlite3.connect("cloth.db")
   cursor = con.cursor()
   if ce >= 27:
        query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=1 and is'
   elif ce >= 23 and ce <= 26:
        query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=2'
   elif ce >= 20 and ce <= 22:
       query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=3'
   elif ce >= 17 and ce <= 19:
       query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=4'
   elif ce >= 12 and ce <= 16:
       query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=5'
   elif ce >= 10 and ce <= 11:
       query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=6'
   elif ce >= 6 and ce <= 9:
       query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=7'
   else: query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=8'
   item = cursor.execute(query).fetchall()

   return render_template('result.html',we=we, ce=ce, icon=icon,location=location,item=item)


if __name__ == '__main__':
    app.run(host='127.0.0.2', debug = True)