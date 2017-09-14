
#65. Valid Number

def validNumber(s):
    eCount = 0
    sCount = 0
    for i in range(len(s)):
        if (ord(s[i]) < ord('0') or ord(s[i]) > ord('9')):
            if (ord(s[i]) == ord('e') or ord(s[i]) == ord('E')):
                eCount += 1
                sCount = 0
                if (eCount > 1): return False
            else:
                if (ord(s[i]) == ord('.')):
                    sCount += 1
                    if (sCount > 1): return False
                else: 
                    return False

    return True

v = "0"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not"))
v = "0.1"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not")) 
v = "abc"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not")) 
v = "1 a"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not")) 
v = "2e18"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not")) 
v = "2e.18"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not")) 
v = ".18"
print("{0} is{1} a number".format(v, "" if validNumber(v) else " not")) 
 
