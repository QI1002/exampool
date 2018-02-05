
#266. Palindrome Permutation

def palPerm(ss):
    freq = {}
    for i in range(len(ss)):
        s = ss[i]
        if (not s in freq):
            freq[s] = 1
        else:
            freq[s] += 1
        
    odd = None    
    for k in freq.keys():
        f = freq[k]
        if ((f % 2) == 1):
            if (odd == None):
                odd = k
            else:
                return False

    return True

sample = "code"
print("{0}=>{1}".format(sample, palPerm(sample)))
sample = "aab"
print("{0}=>{1}".format(sample, palPerm(sample)))
sample = "carerac"
print("{0}=>{1}".format(sample, palPerm(sample)))

