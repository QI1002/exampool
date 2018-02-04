
#248. Strobogrammatic Number III

import math 
def allStro(n, lower = None, upper = None):
    if (upper == None):
        upper = int(math.pow(10, n))-1
    if (lower == None):
        lower = int(math.pow(10, n-1))
    mapping = { '1':'1', '6':'9', '8':'8', '9':'6' }
    result = []
    if (n == 0):
        return  [ "" ]
    if (n == 1):
        for key in sorted(mapping.keys()):
            if (key == mapping[key]):
                ns = int(key)
                if (ns >= lower and ns <= upper):
                    result.append(ns)
        return result

    result = []
    all2 = allStro(n-2)
    for key in sorted(mapping.keys()):
        for x in all2:
            ns = int(key+str(x)+mapping[key])
            if (ns >= lower and ns <= upper): 
                result.append(ns)
    
    return result

def findStro(lower = None, upper = None):
    nl = len(str(lower))
    nu = len(str(upper))
    result = []
    for i in range(nl, nu+1, 1):
        rr = allStro(i, lower, upper)
        result.extend(rr)
    return result

n = 4
print("{0}:{1}".format(n, findStro(70,7000)))
n = 3
print("{0}:{1}".format(n, findStro(70,700)))
n = 2
print("{0}:{1}".format(n, findStro(0,70)))
n = 1
print("{0}:{1}".format(n, findStro(0,7)))

