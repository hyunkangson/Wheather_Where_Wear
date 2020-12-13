from flask import Flask, render_template, request, url_for
from flask import request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from urllib.request import urlopen
import json, sqlite3, re

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html');

@app.route('/userpage',methods=['POST'])
def userpage():
    request.form['bbtn']
    return  render_template('userpage.html');

@app.route('/userpage_result',methods=['POST'])
def userpage_result():

    l1 = request.form['location']
    l2 = request.form['location2']

    location = l2
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&mode=json&APPID=ad91812895dfa17a92a11504c0718122'
    data = urlopen(url).read()
    a = json.loads(data)
    we = (a['weather'][0]['main'])
    ce = round(a['main']['temp'] - 273.15, 1)
    icon = a['weather'][0]['icon']

    con = sqlite3.connect('user_data.db')
    c = con.cursor()
    lc = c.execute("SELECT loc FROM "+l1+" WHERE loc='"+l2+"' and tno=1").fetchone()

    if lc==None:
        return render_template('userpage_result.html',l1=l1,l2=l2)
    else:
        if ce >= 27:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=1 AND loc='" + l2 + "'")
        elif ce >= 23 and ce <= 26:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=2 AND loc='" + l2 + "'")
        elif ce >= 20 and ce <= 22:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=3 AND loc='" + l2 + "'")
        elif ce >= 17 and ce <= 19:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=4 AND loc='" + l2 + "'")
        elif ce >= 12 and ce <= 16:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=5 AND loc='" + l2 + "'")
        elif ce >= 10 and ce <= 11:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=6 AND loc='" + l2 + "'")
        elif ce >= 6 and ce <= 9:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=7 AND loc='" + l2 + "'")
        else:
            query = ("SELECT outer0, top, bottom, etc FROM " + l1 + "WHERE tno=8 AND loc='" + l2 + "'")
        item = c.execute(query).fetchall()
        item = ', '.join(item)
        c.close()
        return render_template('result.html', we=we, ce=ce, icon=icon, location=location, item=item)

@app.route('/DataAddition',methods=['POST'])
def DataAddition():
    request.form['ddata']
    return  render_template('DataAddition.html');

@app.route('/createTable',methods=['POST'])
def createTable():
    table=request.form['table']
    con = sqlite3.connect('user_data.db')
    c = con.cursor()
    c.execute("CREATE TABLE " + table + " (loc varchar(30), tno INT, outer0 varchar(30), top varchar(30), bottom varchar(30), etc varchar(30))")
    c.commit()
    c.close()
    return render_template('DataAddition.html');

@app.route('/tableAdd',methods=['POST'])
def sqlAdd():
    tb_=request.form['lc']
    loc=request.form['lc2']
    con = sqlite3.connect('user_data.db')
    c = con.cursor()

    o_1=request.form['o_1']; t_1=request.form['t_1']; b_1=request.form['b_1']; e_1=request.form['e_1']
    o_2=request.form['o_2']; t_2=request.form['t_2']; b_2=request.form['b_2']; e_2=request.form['e_2']
    o_3=request.form['o_3']; t_3=request.form['t_3']; b_3=request.form['b_3']; e_3=request.form['e_3']
    o_4=request.form['o_4']; t_4=request.form['t_4']; b_4=request.form['b_4']; e_4=request.form['e_4']
    o_5=request.form['o_5']; t_5=request.form['t_5']; b_5=request.form['b_5']; e_5=request.form['e_5']
    o_6=request.form['o_6']; t_6=request.form['t_6']; b_6=request.form['b_6']; e_6=request.form['e_6']
    o_7=request.form['o_7']; t_7=request.form['t_7']; b_7=request.form['b_7']; e_7=request.form['e_7']
    o_8=request.form['o_8']; t_8=request.form['t_8']; b_8=request.form['b_8']; e_8=request.form['e_8']
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',1,'" + o_1 + "','" + t_1 + "','" + b_1 + "','" + e_1 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',2,'" + o_2 + "','" + t_2 + "','" + b_2 + "','" + e_2 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',3,'" + o_3 + "','" + t_3 + "','" + b_3 + "','" + e_3 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',4,'" + o_4 + "','" + t_4 + "','" + b_4 + "','" + e_4 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',5,'" + o_5 + "','" + t_5 + "','" + b_5 + "','" + e_5 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',6,'" + o_6 + "','" + t_6 + "','" + b_6 + "','" + e_6 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',7,'" + o_7 + "','" + t_7 + "','" + b_7 + "','" + e_7 + "')")
    c.execute("INSERT INTO " + tb_ + " VALUES ('"+loc+"',8,'" + o_8 + "','" + t_8 + "','" + b_8 + "','" + e_8 + "')")
    con.commit()
    con.close()
    return render_template('DataAddition.html');


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
        query='SELECT outer0, top, bottom, etc FROM cloth WHERE tno=1'
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
   item = cursor.execute(query).fetchone()
   item=', '.join(item)
   con.close()
   return render_template('result.html',we=we, ce=ce, icon=icon,location=location,item=item)

if __name__ == '__main__':
    app.run(host='127.0.0.2', debug = True)