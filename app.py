#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
toJayson - Sends JSON to Jayson on iOS via Pushcut

Reads from stdin

'''
import requests

# Take command line parameter but do surround by single quotes 

#myString="".join(sys.stdin.readlines())
myString="{'it':'worked!'}"
myjson={'input':myString}
#r=requests.post("https://api.pushcut.io/Iy11kn8dtEj0YOCCY7cWs/View%20JSON",json=myjson,timeout=10)
r=requests.post("https://api.pushcut.io/Iy11kn8dtEj0YOCCY7cWs/notifications/View%20JSON",json=myjson,timeout=10)

print(r.text)