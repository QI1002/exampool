
#340. Longest Substring with At Most K Distinct Characters

def kDistinct(s,k):
    max = 0
    maxi = None
    j = i = 0
    d = {}
    while((i+max) < len(s)):
        while(j < len(s)):
            c = s[j]
            if (not c in d):
                if (len(d) == k): break
                d[c] = 1
            else: 
                d[c] += 1
            j += 1

        #print((i,j,d))
        if ((j-i) > max): max, maxi = j-i, (i,j-1)
        c = s[i]
        d[c] -= 1
        if (d[c] == 0): del d[c]
        i += 1

    return max, maxi    

given,k = "eceba",2
print("{0}:{1}".format((given, k), kDistinct(given, k)))
given,k = "eceba",3
print("{0}:{1}".format((given, k), kDistinct(given, k)))
given,k = "ecebaba",2
print("{0}:{1}".format((given, k), kDistinct(given, k)))


        


