
#233. Number of Digit One

def count1Exhaust(n):
    count = 0
    for i in range(1,n+1,1):
        s = str(i)
        for c in s:
            if (c == '1'): count += 1

    return count

def count1(n):

    count = 0
    uu = 10 
    u = 1 
    d = 0

    while(n > u):
        a = n % uu 
        if (a >= u):
            if (a >= 2*u): 
                count += u 
            else:
                count += (a-u+1)

            count += ((a//u)*u/10 * d)
        d += 1
        print((n,uu,u,a,count,d))
        u = uu
        uu *= 10

    return count

def countkExhaust(n, k):
    count = 0
    for i in range(1,n+1,1):
        s = str(i)
        for c in s:
            if (ord(c) == (ord('0')+k)): count += 1

    return count

def countk(n, k):
    digits = 0
    bound = 1
    while(bound <= n):
        digits += 1        
        bound *= 10    
    
    count = 0
    bound1 = 1
    bound2 = 10
    for i in range(digits):        
        n1 = n // bound2   
        n2 = (n - n1*bound2)//bound1
        n3 = n - n1*bound2 - n2 * bound1
                
        count += n1*bound1
        if (k == 0 and n1 > 0): count -= bound1
                
        if (n2 > k): 
            if (not (k == 0 and n1 == 0)): count += bound1
        else: 
            if (n2 == k): count += (n3+1)

        #print((i, n1, n2, n3, bound1, bound2, count))    
        bound1 *= 10
        bound2 *= 10
        
    return count

for i in range(1000): #10000 ok also
    for k in range(0, 10, 1):
        c1 = countk(i, k)
        c2 = countkExhaust(i, k)
        if (c1 != c2): print((i, k, c1, c2))