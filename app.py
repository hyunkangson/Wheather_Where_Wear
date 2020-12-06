from flask import Flask, render_template
import urllib.request
import urllib.parse

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

REST_API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId': '108'
}
params = urllib.parse.urlencode(values)

url = REST_API + "?" + params

data = urllib.request.urlopen(url).read()

text = data.decode("UTF-8")
print(text)

if __name__ == '__main__':
    app.run(debug=True)