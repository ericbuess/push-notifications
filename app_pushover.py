import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "ahyqzpz4fh1qq8pp7wccoyatns2ur2",
    "user": "ugvdnqcydgr3w6b8p9cti63jsmzp3m",
    "message": "Open the link",
    "title": "Pythonista Test",
    "url": "pythonista3://",
    "url_title": "Pythonista script",
    "priority": 0,
    "sound": "pushover"
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()