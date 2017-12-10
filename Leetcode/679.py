
#679. 24 Game 

import itertools

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if (b == 0): 
        return None
    return a//b

def game24(data):

    order = [ p for p in itertools.permutations([1,2,3]) ]
    result = []
    op = [add, sub, mul, div]
    ops = ['+','-','*','/']

    for i in range(len(order)):
        for j in range(64):
            g = [ ii for ii in range(4) ]
            t = [ None for ii in range(4) ]
            opp = ""
            for k in order[i]:
                opi = (j >> (2*k-2)) & 0x3
                opp = opp + ops[opi]
                op1 = data[k-1] if (t[k-1] == None) else t[k-1]
                op2 = data[k] if (t[k] == None) else t[k]
                r = op[opi](op1, op2)
                if (r == None): break
                g1, g2 = g[k-1], g[k]
                for kk in range(len(g)):
                    if (g[kk] == g2): g[kk] = g[k-1]
                for kk in range(len(g)):
                    if (g[kk] == g1): t[kk] = r
                #print((opi, op1, op2, g, t))
            if (r == 24): result.append((order[i], opp))
            #print((order[i], bin(j), r))

    return result

def game24All(data):
    alldata = [ p for p in itertools.permutations(data) ]
    result = [] 
    for d in alldata:
        r = game24(d)
        if (len(r) != 0):
            result.append((d, r))
            print((d,r))
 
    return result
 
#game24All([1,2,3,4])
game24All([1,4,8,7])
#game24([1,2,1,2])
                
                
                




            
