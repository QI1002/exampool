
#5. Longest Palindromic Substring

def getLongest1(src, n):
    count = len(src)
    i = 0
    while((n-i-1) >= 0 and (n+i+1) < count):
        if (src[n-i-1] != src[n+i+1]):
            break
        i += 1
    return src[n-i:n+i+1]

def getLongest2(src, n):
    count = len(src)
    if ((n+1) >= count or src[n] != src[n+1]):
        return "" 

    i = 0
    while((n-i-1) >= 0 and (n+i+2) < count):
        if (src[n-i-1] != src[n+i+2]):
            break
        i += 1
    return src[n-i:n+i+2]

def longest(src):
    count = len(src)
    n = count//2
    (n1,n2) = (n,n) if ((2*n) != count) else (n-1, n-1)
    step = 1
    maxt = ""
    n = n1
    while(n >=0 and n < count):
        skip = False
        if (step < 0 and (2*count-2*n-1) <= len(maxt)):
            skip = True
        if (step > 0 and (2*n+1) <= len(maxt)):
            skip = True
        if (skip == False):    
            t1 = getLongest1(src, n)
            if (len(maxt) < len(t1)): maxt = t1
            t2 = getLongest2(src, n)
            if (len(maxt) < len(t2)): maxt = t2
            print(n, n1, n2, step, t1, t2)
        if (step > 0): 
            n = n2 + step
            n2 = n
        else: 
            n = n1 + step 
            n1 = n
        step *= -1
   
    return maxt
    
s = "babadd"    
print("{0} => {1}".format(s, longest(s)))
s = "baabdd"
print("{0} => {1}".format(s, longest(s)))

