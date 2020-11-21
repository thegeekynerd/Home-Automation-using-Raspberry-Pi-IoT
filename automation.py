from bottle import route, request, run, get, static_file
import json
import time
import RPi.GPIO as GPIO

sw = [3,4,17,27,22]
state = [0,0,0,0,0]
running=[0,0,0,0,0]
running_time = [0,0,0,0,0]

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
    
    if on is True:
        running[0]=time.time()
    else:
        running[0]=0
        
    GPIO.output(sw[0], on) 
@route('/action2', method='POST')
def action2():
    val = request.forms.get('strState')
    on = bool(int(val))

    if on is True:
        running[1]=time.time()
    else:
        running[1]=0
    
    state[1] = on
    GPIO.output(sw[1], on)
@route('/action3', method='POST')
def action3():
    val = request.forms.get('strState')
    on = bool(int(val))

    if on is True:
        running[2]=time.time()
    else:
        running[2]=0
        
    state[2] = on
    GPIO.output(sw[2], on)
@route('/action4', method='POST')
def action4():
    val = request.forms.get('strState')
    on = bool(int(val))

    if on is True:
        running[3]=time.time()
    else:
        running[3]=0
        
    state[3] = on
    GPIO.output(sw[4], on)
@route('/action5', method='POST')
def action5():
    val = request.forms.get('strState')
    on = bool(int(val))

    if on is True:
        running[4]=time.time()
    else:
        running[4]=0
        
    state[4] = on
    GPIO.output(sw[4], on)


#Get the status for the appliances

def updateRunningTime():
    x = []
    global running_time
    for run in running:
        a = time.time() - run
        if run == 0:
            a=0
        x.append(a)
    for i,j in enumerate(x):
        running_time[i]+=j

@route('/status')
def stat(state=state):
    x = {}
    for i,j in enumerate(state):
        t='A'+str(i)
        y = {}
        y["state"] = int(j)
        updateRunningTime()
        y["time"] = running_time[i]
        y = json.dumps(y)
        x[t]=y
    s = json.dumps(x)
    return s


run(host = '0.0.0.0', port = '8080', server='paste')
