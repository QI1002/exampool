

def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
def swapBits(a):
    odd = a & 0xaaaaaaaa
    even = a & 0x55555555
    odd >>= 1    
    even <<= 1 
    return (odd | even)

a = 0x5aa5
print("{0} swap bits = {1}".format(bin(a), bin(swapBits(a))))
