

def isUniqueStr(strValue):
    count = len(strValue)
    for i in range(count):
        v = strValue[i]
        for j in range(i+1, count, 1):
            if (strValue[j] == v):
                return False
    return True
    
value = "abc"    
print("The unique string of {0} is {1}".format(value, isUniqueStr(value)))
                
value = "dormitory"    
print("The unique string of {0} is {1}".format(value, isUniqueStr(value)))
