

def swap_xor(a,b):
    a = a ^ b
    b = a ^ b 
    a = a ^ b
    return (a,b)
    
pairs = (30, 22)    
print("swap {0} to be {1}".format(pairs, swap_xor(pairs[0],pairs[1])))
