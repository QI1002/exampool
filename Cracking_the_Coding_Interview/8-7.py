
import sys

org_coins = [25, 10, 5, 1]

def coins_combine(coins, n):
       
    if (len(coins) == 1):
        if (coins[0] != 1):
            raise ValueError
        else:    
            return [[n]]
    else:
        result = []
        a = n // coins[0]     
        for i in range(0, a+1, 1):
            all = coins_combine(coins[1:], n - i*coins[0])
            for m in all:
                l = list(m)
                l.insert(0, i)
                result.append(l)
        return result
        
if (len(sys.argv) != 2 or int(sys.argv[1]) <= 0):
    print("python 8-7.py n (n>=1)")
    exit(0)

seed = int(sys.argv[1])
answer = coins_combine(org_coins, seed)
print("the combination of {0} = {1} with len = {2}".format(seed, answer, len(answer)))