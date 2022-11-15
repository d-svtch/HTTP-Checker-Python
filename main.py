import requests

req = requests.get('<a href="http://www.edureka.co/">http://www.edureka.co/</a>')

req.encoding  # returns 'utf-8'
req.status_code  # returns 200
req.elapsed  # returns datetime.timedelta(0, 1, 666890)
req.url  # returns '<a href="https://edureka.co/">https://edureka.co/</a>'

req.history

req.headers['Content-Type']
# returns 'text/html; charset=utf-8'