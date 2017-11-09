from flask import Flask
import urllib2
import json

app = Flask(__name__)

#https://api.nasa.gov/planetary/apod?api_key=1HbGn9RGplzF9EfsWk4vPWh6T24qOzYFbSbDu0Gi

@app.route("/")
def root():
    apod = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=1HbGn9RGplzF9EfsWk4vPWh6T24qOzYFbSbDu0Gi')
    json = urllib.read(apod)
    dict = json.load(json)
    return render_template('apod.html', pic=dict['url'], explain=dict['explanation'])

if __name__ == '__main__':
  app.debug = True
  app.run()
