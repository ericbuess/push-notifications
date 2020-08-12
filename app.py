#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Sends JSON to Pushcut on iOS via a notification which can be used to trigger an automation

Reads from stdin

'''
import requests, json, os

##PUSHCUT_SECRET = os.getenv('PUSHCUT_SECRET')
# Take command line parameter but do surround by single quotes 
print('hi')
#myString="".join(sys.stdin.readlines())

##results={'title':'Covid 19','text':'Bell: 600\nSmith: 300','input':[{'bell':{'total':'600'}}]}
#results=json.dumps(results)
##r=requests.post("https://api.pushcut.io/" + PUSHCUT_SECRET + "/notifications/covid",json=results,timeout=10)

#print('covid notification result: ', r.text)
