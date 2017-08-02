

def setbits(a,b,start,end):
    mask = 0
    len = end - start + 1
    for i in range(len):
        mask <<= 1
        mask |= 0x1
    mask <<= start
    b <<= start 
    b = b & mask    
    a |= mask
    
    return ((a ^ mask) | b)
    
print(bin(setbits(0b10000000000, 0b10101, 2, 6)))
print(bin(setbits(0b10011111111, 0b10101, 2, 6)))




