
#639. Decode Ways II 

def decode(s):

    if (len(s) == 1 and s != "*"): return 1

    if (s[0] == "*"):
        count = 0
        ss = list(s)
        for i in range(1,10,1):
            ss[0] = chr(ord('0')+i)  
            count += decode("".join(ss))
        return count 

    if (s[1] == "*"):
        count = 0
        ss = list(s) 
        for i in range(1,10,1):
            ss[1] = chr(ord('0')+i)
            count += decode("".join(ss))
        return count

    if (int(s[:2]) <= 26):
        if (len(s) == 2): 
            return 1+decode(s[1:])
        else:
            return decode(s[2:])+decode(s[1:])
    else:
        return decode(s[1:])
                                 

print(decode("1**"))

count = 0 
for i in range(1,10,1):
    for j in range(1,10,1):
        ss = ['1', 0, 0] 
        ss[1] = chr(ord('0') + i)
        ss[2] = chr(ord('0') + j)
        t = decode("".join(ss))
        print("".join(ss), t)
        count += t
 
print(count) 
