

def removeDuplicateStr(strValue):
    strValue = list(strValue)
    count = len(strValue)
    for i in range(count):
        v = strValue[i]
        if (v == '\0'):
            continue
        for j in range(i+1, count, 1):
            if (strValue[j] == v):
                strValue[j] = '\0'

    result = ""
    for i in range(count):
        if (strValue[i] != '\0'):
            result = result + strValue[i]

    return result

value = "abc"
print("The remove duplicate string of {0} is {1}".format(value, removeDuplicateStr(value)))

value = "dormitory"
print("The remove duplicate string of {0} is {1}".format(value, removeDuplicateStr(value)))