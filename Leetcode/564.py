
#564. Find the Cloest Palindrome

def isPal(num):
    s = str(num)
    for i in range(len(s)//2):
        if (s[i] != s[len(s)-i-1]): 
            return False
            
    return True
    
# if the same length with smallest update    
def makePal_(num):
    s = str(num)
    ss = list(s)
    for i in range(len(ss)):
        if (ss[i] != ss[len(s)-i-1]): 
            ss[len(s)-i-1] = ss[i]
    
    return int("".join(ss))
        
# with the absolutate min        
def makePal(num):
    if (isPal(num)): return num
    less = more = num
    while(isPal(more) == False):
        more += 1
    while(isPal(less) == False):
        less -= 1
    if ((more-num) < (num-less)):
        return more
    else:
        return less        
            
# check the pal rules
def checkPal(k):
    more = False
    c = 10
    cc = 1
    for i in range(10, k+1):
        if (isPal(i)):
            more = not more 
            continue
        if (cc < (len(str(i))//2)):
            cc,c = cc+1, c*10
        if ((i%c) == 0):
            more = not more   
        p = makePal_(i)
        if (p > i):
            if (more == False): print((p, i))
        else:
            if (more == True): print((p, i))
        
def makePal2(num):
    if (isPal(num)): return num
    p = makePal_(num)
    c = 1 
    for i in range(len(str(num))//2): 
        c *= 10
        
    n = num % c
    if (p > num):
        more = p
        less = makePal_(num-n-1)
    else:
        less = p
        more = makePal_(num + (0 if (n == 0) else (c - n)))
    
    #print((num, n, c, p, more, less))
    if ((more-num) < (num-less)):
        return more
    else:
        return less        
                                        
#checkPal(100000000)            
print(makePal2(123))
print(makePal2(100))
#for i in range(100000):     
#   c1 = makePal(i)
#   c2 = makePal2(i)
#   if (c1 != c2): print((i, c1, c2))