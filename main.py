from flask import Flask, render_template, request, url_for
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html');


@app.route('/result',methods = ['POST'])
def result():
   location=request.form['location']
   url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&mode=json&APPID=ad91812895dfa17a92a11504c0718122'
   data = urlopen(url).read()
   a = json.loads(data)
   we = (a['weather'][0]['main'])

   ce = round(a['main']['temp'] - 273.15, 2)

   return render_template('result.html',we=we, ce=ce)


if __name__ == '__main__':
    app.run(host='127.0.0.2', debug = True)