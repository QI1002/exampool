import sys

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

def fibonacci_stack2(n):
    stack.append(n)
    while(len(stack) > 0):
        now = stack.pop()
        if (now == '+'):
            result.append(result.pop()+result.pop())
        else:
            if (now <= 1):
                result.append(1)
            else:
                stack.append('+')
                stack.append(now-1)
                stack.append(now-2)
    return result.pop()

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if (len(sys.argv) != 2 or int(sys.argv[1]) <= 0):
    print("python 8-1.py n (n>=1)")
    exit(0)

seed = int(sys.argv[1])
print("fibonacci({0})={1}".format(seed, fibonacci_stack2(seed)))
