from bottle import route, request, run, get, static_file
import json
import time
import RPi.GPIO as GPIO

sw = [3,4,17,27,22]
state = [0,0,0,0,0]

GPIO.setmode(GPIO.BCM)
for s in sw:
    GPIO.setup(s, GPIO.OUT)
    GPIO.output(s, False)


@route('/switch')
def switch():
    return static_file('switch.html', root="")

#Controlling the appliances

@route('/action1', method='POST')
def action1():
    val = request.forms.get('strState')
    on = bool(int(val))
    state[0] = on
    GPIO.output(sw[0], on) 
@route('/action2', method='POST')
def action2():
    val = request.forms.get('strState')
    on = bool(int(val))
    state[1] = on
    GPIO.output(sw[1], on)
@route('/action3', method='POST')
def action3():
    val = request.forms.get('strState')
    on = bool(int(val))
    state[2] = on
    GPIO.output(sw[2], on)
@route('/action4', method='POST')
def action4():
    val = request.forms.get('strState')
    on = bool(int(val))
    state[3] = on
    GPIO.output(sw[4], on)
@route('/action5', method='POST')
def action5():
    val = request.forms.get('strState')
    on = bool(int(val))
    state[4] = on
    GPIO.output(sw[4], on)


#Get the status for the appliances
@route('/status')
def stat(state=state):
    x = {}
    for i,j in enumerate(state):
        t='A'+str(i)
        x[t]=str(int(j))
    s = json.dumps(x)
    return s


run(host = '0.0.0.0', port = '8080', server='paste')
