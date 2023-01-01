numX = 0
numY = 0
action = ''
result = 0

def get_numX():
    global numX
    return numX

def get_numY():
    global numY
    return numY

def get_action():
    global action
    return action

def get_result():
    global result
    return result

def set_numX(value):
    global numX
    numX = value

def set_numY(value):
    global numY
    numY = value

def set_action(act):
    global action
    action = act

def sum():
    global numX
    global numY
    global result
    result = numX + numY

def diff():
    global numX
    global numY
    global result
    result = numX - numY

def divis():
    global numX
    global numY
    global result
    result = numX / numY
    if result == int(result):
        result = int(result)

def multy():
    global numX
    global numY
    global result
    result = numX * numY
