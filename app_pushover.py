import http.client, urllib, os
PUSHOVER_TOKEN = os.getenv('PUSHOVER_TOKEN')
PUSHOVER_USER = os.getenv('PUSHOVER_USER')
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": PUSHOVER_TOKEN,
    "user": PUSHOVER_USER,
    "message": "Open the link",
    "title": "Pythonista Test",
    "url": "pythonista3://",
    "url_title": "Pythonista script",
    "priority": 0,
    "sound": "pushover"
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()