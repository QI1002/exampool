import sys

def invalid(x1,y1,x2,y2):
    cc = abs(y1 - y2)
    return ((x1 == x2) or (y1 == y2) or
           ((x1-x2) == (y1-y2)) or ((x1+y1) == (x2+y2))) 

def validall(data, x, y):
    for i in range(len(data)):
        if (invalid(i+1, data[i], x, y)):
            return False
    return True
    
def queens():
    result = []
    for i in range(1,9,1):
        base = result
        result = []
        for j in range(1,9,1):
            if (i == 1):
                result.append([j])
            else:
                for x in base:
                    if (validall(x, i, j)):
                        l = list(x)
                        l.append(j)
                        result.append(l)
    return result
     
answer = queens()     
print("8 queens result = {0} with len = {1}".format(answer, len(answer)))