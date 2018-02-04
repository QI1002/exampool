
#247. Strobogrammatic Number II

def allStro(n):
    mapping1 = { '8':'8', '1':'1' }
    mapping2 = { '9':'6', '6':'9' }
    if (n == 0):
        return  [ "" ]
    if (n == 1):
        return [ key for key in mapping1.keys()]

    result = []
    all2 = allStro(n-2)
    for x in all2: 
        for key in mapping2.keys():
            result.append(key+x+mapping2[key])
        for key in mapping1.keys():
            result.append(key+x+key)
    
    return result

n = 4
print("{0}:{1}".format(n, allStro(n)))
n = 3
print("{0}:{1}".format(n, allStro(n)))
n = 2
print("{0}:{1}".format(n, allStro(n)))
n = 1
print("{0}:{1}".format(n, allStro(n)))

