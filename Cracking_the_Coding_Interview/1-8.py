

def isSubStr(srcstr, substr):
    count = len(srcstr)
    subcount = len(substr)
    for i in range(count-subcount):
        if (srcstr[i:subcount+i] == substr):
            return i 
    return -1

def isRotateStr(srcstr, rotatestr):
    if (len(srcstr) != len(rotatestr)):
        return False
    checkstr = rotatestr + rotatestr
    
    if (isSubStr(checkstr, srcstr) == -1):
        return False
    else:
        return True
        
str1 = "waterbottle"
str2 = "erbottlewat"
str3 = "erbottlewater"
str4 = "erbottleway"

print("The rotate string of {0} and {1} is {2}".format(str1, str2, isRotateStr(str1, str2)))
print("The rotate string of {0} and {1} is {2}".format(str1, str3, isRotateStr(str1, str3)))
print("The rotate string of {0} and {1} is {2}".format(str1, str4, isRotateStr(str1, str4)))
            
