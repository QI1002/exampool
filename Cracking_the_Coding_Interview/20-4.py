
import math

def calTwoSingle(n, digit):
    level0 = int(math.pow(10, digit))
    level1 = int(math.pow(10, digit+1))
    
    upper = n // level1
    middle = n - (n // level1)*level1
    lower = n - (n//level0)*level0
    #print(str(upper) + " " + str(middle) + " " + str(lower))
    
    count = upper * level0
    if (middle >= (3*level0)):
        count += level0
    else:   
        if (middle >= (2*level0)):
            count += (lower+1)
              
    return count
    
def calTwo(n):
    count = 0
    digits = math.ceil(math.log(n, 10))
    for i in range(0, digits+1, 1):
        count += calTwoSingle(n, i)
    return count
    
def calTwoExhaust(n):
    count = 0
    for i in range(1, n+1, 1):
        ss = str(i)
        for j in range(len(ss)):
            if (ss[j] == '2'):
                count += 1
    return count                

value = 2222
print(calTwoExhaust(value))  
print(calTwo(value))
  