
#301 Remove Invalid Parentheses

import copy
def removeInvalidP(s):
    count = len(s)
    row = [ 0 for i in range(count) ] 
    m = [ list(row) for i in range(count) ] 
    
    for i in range(count):
        for j in range(count):
            m[i][j] = [[]]
            
    for i in range(count):
        for j in range(count-i):
            start = j
            end = j + i 
            if (i == 0):
                m[start][end] = [[start]]
            else: 
                if (i == 1):
                    if (s[start] != "(" or s[end] != ")"):
                        m[start][end] = [[start, end]]
                else: 
                    if (s[start] == ")"):
                        m[start][end] = []
                        for x in m[start+1][end]:
                            y = list(x)
                            y.insert(0, start)
                            m[start][end].append(y)
                    else:
                        if (s[start+1] == ")"):
                            m1 = copy.deepcopy(m[start+2][end])
                        else:
                            m1 = []
                            for x in m[start+1][end]:
                                y = list(x)
                                y.insert(0, start)
                                m1.append(y)

                        if (s[end] == ")"):
                            m2 = copy.deepcopy(m[start+1][end-1])
                        else:
                            m2 = []
                            for x in m[start][end-1]:
                                y = list(x)
                                y.append(end)
                                m2.append(y)
                                           
                        if (len(m1[0]) == len(m2[0])):
                            #print((start, end, m1, m2))
                            m[start][end] = m1
                            m[start][end].extend(m2)
                        else:                        
                            m[start][end] = copy.deepcopy(m2) if (len(m1[0]) > len(m2[0])) else copy.deepcopy(m1)
 
    for i in range(count):
        print(m[i])
                               
    return m[0][count-1]
        
                        
#print(removeInvalidP("(()"))
print(removeInvalidP("())()"))
#print(removeInvalidP("()())()"))
#print(removeInvalidP("()()())"))