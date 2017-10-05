
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
    
sample = 11
print(count1Exhaust(sample))
print(count1(sample))
