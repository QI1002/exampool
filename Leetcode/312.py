
#312. Burst Balloons

def allPermutations(k):
    result = [ [i] for i in range(k) ]
    for i in range(1, k, 1):
        base = result
        result = []
        for b in base:
            for j in range(k):
                if (not j in b):
                    bb = list(b)
                    bb.append(j)
                    result.append(bb)
        
    return result

def allPermutations2(k):
    result = [ [i+1] for i in range(k) ]
    for i in range(1, k, 1):
        base = result
        result = []
        for b in base:
            for j in range(1,k-i+1,1):
                bb = list(b)
                bb.append(j)
                result.append(bb)
        
    return result

def burstBalloons2(b, order = None):
    count = len(b)
    if (order == None):
        a = allPermutations2(count)
    else:
        a = [order]    
    maxcoin = 0
    maxindex = 0
    for i in range(len(a)):
        bb = list(b)
        bb.insert(0, 1)
        bb.append(1)
        coin = 0
        for j in range(count):
            t = a[i][j]
            coin += bb[t]*bb[t-1]*bb[t+1]
            bb.pop(t)
        if (maxcoin < coin): 
            maxcoin = coin
            maxindex = i
            
    am = [ i-1 for i in a[maxindex] ]        
    return maxcoin, am          
                    
def burstBalloons(b):
    count = len(b)
    bb = list(b)
    bb.insert(0, 1)
    bb.append(1)
    h = []
    coin = 0    
    for i in range(count):
        maxN = 0
        maxi = 0
        for j in range(1,count-i+1,1):
            n = bb[j-1]*bb[j+1]
            if (maxN < n):
                maxN = n
                maxi = j
        h.append(maxi)
        coin += bb[maxi-1]*bb[maxi]*bb[maxi+1]        
        bb.pop(maxi)
        
    am = [ i-1 for i in h ]        
    return coin, am         
        
sample = [3,1,5,8]
print(burstBalloons(sample))
print(burstBalloons2(sample))

sample = [3,1,9,5,5,8]
print(burstBalloons(sample))
print(burstBalloons2(sample))


sample = [2,2,4,8,16,2]
print(burstBalloons(sample))
print(burstBalloons2(sample))
print(burstBalloons2(sample, [2,2,2,2,1,1]))

#(784, [3, 2, 1, 0, 1, 0]) -> 
#(406, [1, 1, 1, 1, 0, 0]) -> 2*2*4+2*4*8+2*8*16+2*16*2+1*2*2+1*2*1 = 
