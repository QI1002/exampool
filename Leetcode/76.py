
#76. Mininum Window Substring

def minSubstring(s, ss):
    count = len(ss)
    occur = [ [] for i in range(count) ]
    for i in range(len(s)):
        for j in range(count):
            if (s[i] == ss[j]):
                occur[j].append(i)
                break
    
    for j in range(count):
        if (len(occur[j]) == 0):
            return (len(s), len(s))
            
    minlength = len(s)
    minSubstr = (0, len(s)-1)
    
    index = [ 0 for i in range(count+1) ]
    while(index[count] == 0):
        
        min = len(s)-1
        max = 0 
        for i in range(count):
            c = occur[i][index[i]]
            if (min > c): min = c
            if (max < c): max = c
        
        if (minlength > (max-min+1)):
            minlength = (max-min+1)
            minSubstr = (min, max)
              
        index[0] += 1
        for i in range(count):
            if (index[i] >= len(occur[i])):
                index[i] = 0
                index[i+1] += 1
            else:
                break    
          
    return minSubstr
                
sample = "adobecodebanc"
template1 = "abc"
template2 = "abcd"
template3 = "abcde"
template4 = "abcdef"

t = minSubstring(sample, template1)       
print((t, sample[t[0]:t[1]+1]))

t = minSubstring(sample, template2)       
print((t, sample[t[0]:t[1]+1]))

t = minSubstring(sample, template3)       
print((t, sample[t[0]:t[1]+1]))

t = minSubstring(sample, template4)       
print((t, sample[t[0]:t[1]+1]))