
#339. Nested List Weight Sum 

def nestedSum(data):
    l = data.split(',')
    d = 0
    s = 0
    #print(l)
    for x in l:
        xx = x
        dd = d
        if '[' in x:
            while(len(xx) > 0 and '[' == xx[0]):
                xx = xx[1:]
                d += 1
            dd = d  

        if ']' in x:
            while(len(xx)>0 and ']' == xx[-1]):
                xx = xx[:-1]
                d -= 1

        if (len(xx) != 0): s += int(xx)*dd

    return s

print(nestedSum("[[1,1],2,[1,1]]"))
print(nestedSum("[1,[4,[6]]]"))    
print(nestedSum("[1,[4,[]]]"))    

