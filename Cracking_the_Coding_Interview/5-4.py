

def isPower2(n):
    return ((n & n-1) == 0)
    
for i in range(2000):    
    if (isPower2(i)):
        print("{0} is Power2".format(i))