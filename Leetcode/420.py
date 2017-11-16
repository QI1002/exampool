
#420. Strong Password Checker

def passwordChecker(p):
    stat = {}
    c3 = []
    for i in range(len(p)):
        if (not p[i] in stat): stat[p[i]] = []
        stat[p[i]].append(i)           
    
    i = 0
    while(i < (len(p)-2)):
        j = i+1
        while(j < len(p) and p[i] == p[j]): 
            j += 1
        if ((j-i) >= 2): c3.append((i,j))
        i = j
        
    print((stat, c3))

pp = "aaabbbccc"
print(passwordChecker(pp))
