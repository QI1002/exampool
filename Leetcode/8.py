
#8. String to Integer (atoi)

def atoi(ss):
    exp = None
    v = 0
    dot = 0
    for i in range(len(ss)):
        s = ss[i]

        if (s == '.'): 
            dot = 0.1
            continue

        if (s == 'E' or s == 'e'):
            exp = 0
            dot = 0
            continue

        if (s >= '0' and s <= '9'):
            d = ord(s)-ord('0')
            if (dot != 0):
                v += d * dot
                dot *= 0.1
            else:
                if (exp != None):
                    exp = exp*10+d
                else:
                    v = v*10+d

            continue

        return None

    if (exp != None):
        for i in range(exp): v *= 10
    return v

ss = "123.456"
print("{0}=>{1},{2}".format(ss, atoi(ss), float(ss)))
ss = "123.00"
print("{0}=>{1},{2}".format(ss, atoi(ss), float(ss)))
ss = "123.456"
print("{0}=>{1},{2}".format(ss, atoi(ss), float(ss)))
ss = "123.456e2"
print("{0}=>{1},{2}".format(ss, atoi(ss), float(ss)))

