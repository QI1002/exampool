
def replaceSpace(strValue):
    count = len(strValue)
    result = ""
    for i in range(count):
        if (strValue[i] == ' '):
            result = result + "%20"
        else:
            result = result + strValue[i]
    return result

value = "this is just a example"
print("The replace string of {0} is {1}".format(value, replaceSpace(value)))
