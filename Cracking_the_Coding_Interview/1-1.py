

def isUniqueStr(strValue):
    count = len(strValue)
    for i in range(count):
        v = strValue[i]
        for j in range(i+1, count, 1):
            if (strValue[j] == v):
                return False
    return True

def isUniqueStrNew(strValue):
    count = len(strValue)
    mask = 0
    for i in range(count):
        c = ord(strValue[i]) - ord('a')
        if ((mask >> c) & 0x1) == 0:
            mask |= (1 << c)
        else:
            return False
    return True

method = isUniqueStrNew
#method = isUniqueStr

value = "abc"
print("The unique string of {0} is {1}".format(value, method(value)))

value = "dormitory"
print("The unique string of {0} is {1}".format(value, method(value)))
