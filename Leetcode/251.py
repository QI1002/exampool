
#251. Flatten 2D Vector 

def flatten(f):
    result = []
    for x in f:
        for y in x:
            result.append(y)
    return result

f = [[1,2],[3],[4,5,6]]
print("{0}:{1}".format(f, flatten(f)))            
