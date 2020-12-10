from flask import Flask, render_template, request
import urllib.request
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html');


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
