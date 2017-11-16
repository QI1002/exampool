
#420. Strong Password Checker

def max(a, b):
    return a if a > b else b

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
        if ((j-i) >= 2): c3.append((i,j-1))
        i = j

    #print((stat, c3))
    
    dec = 0
    for c in c3:
        if ((c[1]-c[0]+1) >= 3):
            dec += (c[1]-c[0]-1)
    
    upper = False
    lower = False
    digit = False
    for x in stat:
        if (ord(x) >= ord('A') and ord(x) <= ('Z')): 
            upper = True
        if (ord(x) >= ord('a') and ord(x) <= ('z')): 
            upper = True
        if (ord(x) >= ord('0') and ord(x) <= ('9')): 
            upper = True
   
    inc = 0 
    if (upper == False): inc += 1
    if (lower == False): inc += 1
    if (digit == False): inc += 1

    #print((inc, dec))
    update = inc - dec
    if ((len(p)+update) < 6): 
              return max(inc, dec)+ (6-len(p)-update)
    else: 
          if ((len(p)+update) > 20):
              return max(inc, dec) + (len(p)+update-20)
          else: 
              return max(inc, dec)                 

pp = "aaaa"
print(passwordChecker(pp))
      
pp = "aaabbbccc"
print(passwordChecker(pp))
