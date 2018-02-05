
#266. Palindrome Permutation II

import copy
class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def getPerm(freq):
    result = []
    count = 0
    for k in freq.keys(): count += freq[k]
    s = stack()
    s.push(("",{}))
    while(not s.isEmpty()):
        sp, p = s.pop()
        if (len(sp) == count):
            result.append(sp)
            continue
        for k in freq:
            f = freq[k]
            if (k in p): f -= p[k]
            if (f <= 0): continue
            pp = copy.copy(p)
            if (not k in pp): pp[k] = 1
            else: pp[k] += 1
            s.push((sp+k,pp))
            
    return result       

def allPalPerm(ss):
    freq = {}
    for i in range(len(ss)):
        s = ss[i]
        if (not s in freq):
            freq[s] = 1
        else:
            freq[s] += 1
        
    odd = ""
    for k in freq.keys():
        f = freq[k]
        if ((f % 2) == 1):
            if (odd == ""):
                odd = k
            else:
                return []

    if (odd != ""): del freq[odd]
    for k in freq.keys():
        freq[k] //= 2

    #print(freq)
    ssl = getPerm(freq)
    result = [ sl+odd+sl[::-1] for sl in ssl ]     
    return result

sample = "code"
print("{0}=>{1}".format(sample, allPalPerm(sample)))
sample = "aab"
print("{0}=>{1}".format(sample, allPalPerm(sample)))
sample = "carerac"
print("{0}=>{1}".format(sample, allPalPerm(sample)))
sample = "ccaaeaacc"
print("{0}=>{1}".format(sample, allPalPerm(sample)))

