
#276. Paint Fence 

def fencePaint(n, k):
    if (n == 1): return k
    if (n > 1 and k == 1): return 0
    return fencePaint(n-1, k)*(k-1)

n, k = 100, 2
print("{0}=>{1}".format((n,k),fencePaint(n,k)))
n, k = 10, 3
print("{0}=>{1}".format((n,k),fencePaint(n,k)))
