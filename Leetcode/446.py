
#def Arthmetic Slices II Subsequence

def checkSlices(data):
    c = data[1] - data[0]
    for i in range(2, len(data)):
        if ((data[i] - data[i-1]) != c):
            return False

    return True

def allSlices(data):
    result = []
    power = (1 << len(data))

    for c in range(power):
        ll = []
        for i in range(len(data)):
            if ((c & (1<<i)) != 0): 
                ll.append(i)
        if (len(ll) > 2):
            lll = [ data[j] for j in ll ]
            if (checkSlices(lll) and not lll in result):  
                result.append(lll)

    return sorted(result)

def allSlices2(data):

    if (len(data) <= 2):
        return []
        
    c = data[-1]    
    t = allSlices2(data[:-1])
    tt = [ list(x) for x in t ] 
    for x in t:
        if ((c-x[-1]) == (x[1]-x[0])):
            xx = list(x)
            xx.append(c)
            if (not xx in tt): tt.append(xx)
            
    for j in range(len(data)-1,-1,-1):
        cc = 2*data[j] - c 
        if (cc in data[:j]):
            yy = [cc, data[j], c]
            if (not yy in tt): tt.append(yy)
            
    return sorted(tt)               
            

samples = [2,4,6,8,10]
print(allSlices(samples))
print(allSlices2(samples))

samples = [7,7,7,7,7]
print(allSlices(samples))
print(allSlices2(samples))

