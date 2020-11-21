'''
Switchable pins: 3, 4, 17, 27, 22
'''


from bottle import route, request, run, get, static_file, response
import json
import RPi.GPIO as GPIO


from switch import *



@route('/status')
def stat(state=state):
    x = {}
    for i,j in enumerate(state):
        t='A'+str(i)
        y = {}
        y["state"] = int(j)
        updateRunningTime()
        y["time"] = running_time[i]
        
        x[t]=y
    s = json.dumps(x)
    response.content_type = 'application/json'
    print(s)
    return s


run(host = '0.0.0.0', port = '8080', server='paste')
