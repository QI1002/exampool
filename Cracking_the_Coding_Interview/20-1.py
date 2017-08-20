
#   a  b  c  ans1 ans2 
#   0  0  0  0     0
#   1  0  0  1     0
#   0  1  0  1     0
#   0  0  1  1     0
#   1  1  0  0     1
#   0  1  1  0     1
#   1  0  1  0     1
#   1  1  1  1     1 

def bitadd(a,b):
    result = 0
    abits = a
    bbits = b
    bits = 0
    result = 0
    c = 0
    
    while(abits != 0 or bbits != 0 or c != 0):
        av = abits & 1
        bv = bbits & 1
        v = av ^ bv ^ c
        c = (av & bv) | (av & c) | (bv & c)          
        result |= (v << bits)
        
        bits += 1
        abits >>= 1
        bbits >>= 1
    
    return result
    
print(bitadd(183,125))        
            
        