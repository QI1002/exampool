
def getBits(a):
    count = 0
    while(a != 0):
        if ((a & 0x1) != 0):
            count += 1
        a >>= 1
    return count
    
def covertBits(a,b):
    return getBits(a ^ b)
    
print(covertBits(31,14))        