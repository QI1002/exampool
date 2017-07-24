
import sys

stack = []
def permutation_stack(n):
    result = []
    stack.append(-n)
    stack.append(n)
    while(len(stack)>0):
        n = stack.pop()
        if (n >= 0):
            if (n == 0):
                result = [[]]
            else:
                stack.append(1-n)
                stack.append(n-1)
        else:
            print(stack)
            more = []
            for x in result:
                for i in range(len(x)+1):
                    y = list(x)
                    y.insert(i, -n)
                    more.append(y)
            result = more
    return result


def permutation_loop(n):
    result = []
    for j in range(1,n+1,1):
        if (j == 1):
            result.append([1])
        else:
            more = []
            for x in result:
                for i in range(len(x)+1):
                    y = list(x)
                    y.insert(i, j)
                    more.append(y)
            result = more
    return result

def permutation(n):
    if (n == 1):
        return [[1]]
    else:
       result = []
       base = permutation(n-1)
       for x in base:
           for i in range(len(x)+1):
               y = list(x)
               y.insert(i, n)
               result.append(y)
       return result

if (len(sys.argv) != 2 or int(sys.argv[1]) <= 0):
    print("python 8-4.py n (n>=1)")
    exit(0)

answer = permutation_stack(int(sys.argv[1]))
print("permutation{0}={1} and it's length={2}".format(sys.argv[1], answer, len(answer)))