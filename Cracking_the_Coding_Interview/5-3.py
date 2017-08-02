
def getBits(a):
    count = 0
    while(a != 0):
        if ((a & 0x1) != 0):
            count += 1
        a >>= 1
    return count
         
def nextBitNum(a):
    if (a == 0xFFFFFFFF):
        return a
    bits = getBits(a)
    for i in range(a+1, 0xFFFFFFFF, 1):
        if (getBits(i) == bits):
            return i
    return a


def previousBitNum(a):
    bits = getBits(a)
    for i in range(a-1, -1, -1):
        if (getBits(i) == bits):
            return i
    return a

print(bin(nextBitNum(0xa5)))
print(bin(0xa5))
print(bin(previousBitNum(0xa5)))