
#254. Factor Combinations 

def factorCombine(f):
    for x in f:
        for y in x:
            yield y

f = [[1,2],[3],[4,5,6]]
t = factorCombine(f)
print("{0}:{1}".format(f, list(t)))            
