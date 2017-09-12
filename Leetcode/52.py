
#52. N-Queens II

def check(x1,y1,x2,y2):
    if (x1 == x2 or y1 == y2): return True
    if ((x1+y1) == (x2+y2)): return True
    if ((x1-y1) == (x2-y2)): return True
    return False

def queens(n = 8):

    result2 = result = []

    for i in range(n):
        for j in range(n):
            if (i == 0):
                result.append([j])
                continue
            for k in range(len(result)):
                conflict = False
                for kk in range(i):
                    if (check(i,j,kk,result[k][kk]) == True):
                        conflict= True
                        break

                if (conflict == False):
                    l = list(result[k])
                    l.append(j)
                    result2.append(l) 

        result = result2
        result2 = []
        #print(len(result))
    return result

rr = queens()             
print(len(rr)) 
