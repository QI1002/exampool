
#600. Non-negative Integers without Consecutive Ones

def isIL(n):
    s = bin(n)
    for i in range(3, len(s), 1):
        if (s[i] == s[i-1]): 
            return False

    return True

def genIL(d):
    s = ""
    c = c1 = "1"
    c0 = "0"
    for i in range(d):
        s += c
        c = c0 if (c == c1) else c1

    return int(s, 2)          

  
def smallIL(n):

    if isIL(n):  
        return n

    d = len(bin(n))-2
    nn = genIL(d)
    if (nn > n): 
        return genIL(d-1)
    return nn    

def smallIL2(n):

    if (isIL(n)):
        return n

    for i in range(n, 1, -1):
        if (isIL(i)):
            return i 
   
for n in range(8192, -1, -1):
    il1 = smallIL(n)
    il2 = smallIL2(n)
    if (il1 != il2):
        print("{0} get different answers, i.e. {1},{2}".format(n, smallIL(n), smallIL2(n)))

