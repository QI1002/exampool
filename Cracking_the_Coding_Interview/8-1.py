
stack = []
result = []
def fibonacci_stack(n):
    stack.append(n)
    while(len(stack) > 0):
        now = stack.pop()
        if (now <= 1):
            result.append(1)
            if len(result) >= 2:
               result.append(result.pop()+result.pop()) 
        else:
            stack.append(now-1)
            stack.append(now-2)
    return result.pop()
    
def fibonacci(n):
    if n <= 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print("fibonacci(3)={0}".format(fibonacci_stack(10)))      
       