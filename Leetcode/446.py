
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
            if (checkSlices(lll)):  result.append(lll)

    return result

def allSlices2(data):
    pass

samples = [2,4,6,8,10]
print(allSlices(samples))
print(allSlices2(samples))


