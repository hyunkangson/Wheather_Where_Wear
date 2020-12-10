from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html');


@app.route('/result',methods = ['POST'])
def result():
   location=request.form['location']
   return render_template('result.html', location=location)


if __name__ == '__main__':
    app.run(host='127.0.0.2', debug = True)
