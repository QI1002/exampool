
import math

def antsCollison(n):
    return 1 - 2.0/math.pow(2,n)
    
n = 30
print("the possibility of {0} ants conflict is {1}".format(n, antsCollison(n)))     