
#483. Smallest Good Base

import math

def getDividePrime(k):
    result = []
    divide = [k]
    update = True
    while(update):
        update = False
        base = divide
        divide = []
        #print((base, result))
        for kk in base:
            h = int(math.floor(math.pow(kk,0.5)))
            prime = True
            for i in range(2, h+1, 1): 
                if ((kk % i) == 0):
                     divide.append(i)
                     divide.append(kk/i)
                     update = True
                     prime = False
                     break
            if (prime and not kk in result): result.append(kk)

    return sorted(result)

def getDivideAll(k):
    result = []
    divide = [k]
    update = True
    while(update):
        update = False
        base = divide
        divide = []
        #print((base, result))
        for kk in base:
            h = int(math.floor(math.pow(kk,0.5)))
            prime = True
            for i in range(2, h+1, 1): 
                if ((kk % i) == 0):
                     divide.append(i)
                     divide.append(kk/i)
                     update = True
                     prime = False
                     break
            if (prime): result.append(kk)

    allresult = []
    allnum = 1 << len(result)
    for i in range(1, allnum-1, 1):
        r = 1
        for j in range(len(result)):
            if (i & (1 << j)) != 0:
                r *= result[j]
        if (not r in allresult): allresult.append(r)
 
    return sorted(allresult)
         
def goodBase(k, df):

    min = k-1
    kd = df(k-1)
    #print(kd)
    for x in kd:
        xx = x
        kk = k-1
        while(kk != 0):            
            if ((kk % xx) != 0):
                break
            kk -= xx
            xx *= x

        if (kk == 0 and min > x):
            min = x

    return min
  
def goodBasePrime(k, df=getDividePrime):
    goodBase(k, df)

def goodBaseAll(k, df=getDivideAll):
    goodBase(k, df)

#print(getDivideAll(9999))
#print(getDividePrime(9999))

for i in range(4,10000,1):
    g1 = goodBasePrime(i)
    g2 = goodBaseAll(i)
    if (g1 != g2): 
        print((i, g1, g2))
