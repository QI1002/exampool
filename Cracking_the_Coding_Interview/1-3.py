

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

def removeDuplicateStrNew(strValue):
    strValue = list(strValue)
    mask = 0
    count = len(strValue)
    result = []
    for i in range(count):
        c = ord(strValue[i]) - ord('a')
        if ((mask >> c) & 0x1) == 0:
            result.append(strValue[i])
            mask |= (1 << c)

    return "".join(result)

method = removeDuplicateStrNew
#method = removeDuplicateStr

value = "abc"
print("The remove duplicate string of {0} is {1}".format(value, method(value)))

value = "aaaaa"
print("The remove duplicate string of {0} is {1}".format(value, method(value)))

value = "dormitory"
print("The remove duplicate string of {0} is {1}".format(value, method(value)))
