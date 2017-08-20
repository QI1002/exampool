

def getTailZero(n):
    count = 0
    five = 5
    while(n >= five):
        n = n // five
        count += n
        
    return count
    
def factorial(n):
    count = 1
    for i in range(1,n+1,1):
        count *= i
    return count
        
n = 100        
print("return tailZero of {0} is {1} with {2}".format(n, getTailZero(n), factorial(n)))
        