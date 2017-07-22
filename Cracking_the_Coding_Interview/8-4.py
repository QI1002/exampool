

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
           
answer = permutation(4)           
print("permutation(3)={0} and it's length={1}".format(answer, len(answer)))             