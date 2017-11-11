from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

# google maps api key AIzaSyDuEPbNheH4vFOMikIk4jFsD5g75UDzdzY
@app.route("/")
def root():
    gurl= "https://www.google.com/maps/embed/v1/search?key=AIzaSyDuEPbNheH4vFOMikIk4jFsD5g75UDzdzY&q=Stuyvesant+High+School,New+York,NY"
    return render_template('gmap.html',url=gurl)

'''
def NASA_root():
    apod = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=1HbGn9RGplzF9EfsWk4vPWh6T24qOzYFbSbDu0Gi')
    apod_dict = json.loads(apod.read())
    return render_template('apod.html', apod_img=apod_dict['url'], apod_title=apod_dict["title"], apod_desc=apod_dict["explanation"])
'''
if __name__ == '__main__':
  app.debug = True
  app.run()
