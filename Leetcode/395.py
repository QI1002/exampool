

#395. Longest Substring with At Least K Repeating Characters

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
        
def strFreq(s1):
    freq = {}
    for i in range(len(s1)):
        c = s1[i]
        if (not c in freq):
            freq[c] = 1
        else:
            freq[c] += 1
    
    return freq
          
def strReplace(s1, index, c):
    data = list(s1)
    data[index] = c
    return "".join(data)
                  
def moreK(s1, k):
  
    candidate = stack()
    candidate.push(s1)
    maxStr = ""
    while (not candidate.isEmpty()):
        v = candidate.pop()
        freq = strFreq(v)
        noReplace = True
        for i in range(len(v)):
            c = v[i]
            if (freq[c] < k):
                v = strReplace(v, i, " ")
                noReplace = False
                
        if (noReplace):
            if (len(v) > len(maxStr)):
                maxStr = v  
            continue
        
        splits = v.split()
        
        for i in range(len(splits)):
            candidate.push(splits[i])  
            
    return maxStr
                
print(moreK("aabbeabc", 2))                       