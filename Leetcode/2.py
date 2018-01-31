
#2. Add Two Numbers

def add(s1,s2):
    c = i = 0
    s = []
    while(i < len(s1) or i <len(s2)):
        d1 = 0 if (i >= len(s1)) else s1[i]
        d2 = 0 if (i >= len(s2)) else s2[i] 
        d = d1 + d2 + c  
        c = 0
        if (d >= 10): c,d = 1,d-10
        s.append(d)
        i += 1

    if (c > 0): s.append(c)    
    return s

s1,s2 = [2,4,3], [5,6,4]
print("{0}+{1}={2}".format(s1,s2,add(s1,s2)))

s1,s2 = [1,0,1], [9,9,9]
print("{0}+{1}={2}".format(s1,s2,add(s1,s2)))

s1,s2 = [1,0,1], [9,9]
print("{0}+{1}={2}".format(s1,s2,add(s1,s2)))

