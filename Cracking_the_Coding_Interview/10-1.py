

def minus(a,b):
    return a + (-b)

def multiple(a,b):
    result = 0
        
    if (b < 0):
        minus = True 
        b = -b
    else: 
        minus = False
    for i in range(b):
        result += a
    if (minus):
        result = -result
        
    return result        
        
def divide(a,b):
    result = 0
    acc = 0
    minus = False
    if (b == 0):
        raise ValueError
    if (b < 0):
        b = -b
        if (a >= 0): 
            minus = True
        else:
            a = -a    
    else:
        if (a < 0):
            a = -a 
            minus = True
    
    while(acc < a):  
        result += 1
        acc += b        
    result -= 1
    
    if (minus):
        result = -result
    return result 
                
print("{0} multiple {1} = {2}".format(0,0,multiple(0,0)))        
print("{0} multiple {1} = {2}".format(2,3,multiple(2,3)))        
print("{0} multiple {1} = {2}".format(-2,3,multiple(-2,3)))        
print("{0} multiple {1} = {2}".format(3,-2,multiple(3,-2)))        
print("{0} multiple {1} = {2}".format(-3,-2,multiple(-3,-2)))                
    
print("{0} divide {1} = {2}".format(0,1,divide(0,1)))        
print("{0} divide {1} = {2}".format(2,3,divide(2,3)))        
print("{0} divide {1} = {2}".format(-2,3,divide(-2,3)))        
print("{0} divide {1} = {2}".format(3,-2,divide(3,-2)))        
print("{0} divide {1} = {2}".format(-3,-2,divide(-3,-2)))                
            