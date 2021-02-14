def NOT(a):
    return not a

def OR(a,b):
    return a or b
    
def AND(a,b):
    return a and b

def NAND(a,b):
    return NOT(AND(a,b))

def NOR(a,b):
    return NOT(OR(a,b))

def XOR(a,b):
    return OR(AND(NOT(a),b),AND(a,NOT(b)))

def XNOR(a,b):
    return NOT(XOR)

def tobool(a):
    if a == 1 or a == '1':
        return True
    elif a == 0 or a == '0':
        return False

def toint(a):
    if a == True:
        return 1
    elif a == False:
        return 0