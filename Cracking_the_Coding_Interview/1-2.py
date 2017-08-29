

def swap(ll,i,j):
    tmp = ll[i]
    ll[i] = ll[j]
    ll[j] = tmp

def reverseStr(strValue):
    strValue = list(strValue)
    count = 0
    while(strValue[count] != '\0'):
        count += 1

    for i in range(count//2):
        swap(strValue, i, count-i-1)

    result = ""
    for i in range(count):
        result = result+ strValue[i]

    return result

def appendZero(strValue):
    return strValue + '\0'

value = appendZero("abc")
print("The reverse string of {0} is {1}".format(value, reverseStr(value)))

value = appendZero("dormitory")
print("The reserve string of {0} is {1}".format(value, reverseStr(value)))