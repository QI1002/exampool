
#30. Substring with Concatenation of All Words
#I1. typo due to change variables
#I2. findString can't consider 1 item case
#I3. getConcatStrings is wrong to find substring way 

def findString(target, samples):
    l = 0
    r = len(samples)-1
    while (r >= l):
        m = (r+l)//2        
        if (samples[m] == target):
            return m
            
        if (m == l):
            if (target < samples[l]):
                return l
            else:
                return (r if (target <= samples[r]) else r+1)
        else:                
            if (samples[m] > target):
                r = m
            else:        
                l = m    
             
def getConcatStrings(source, samples):
    
    sorted_samples = sorted(samples)
    result = []
    for i in range(len(source)):
        check = list(sorted_samples)
        ii = i
        while(len(check) > 0):          
            j = findString(source[ii:], check)
            print((i, ii, j))
            if (j < len(check) and check[j] == source[ii:ii+len(check[j])]):
                ii += len(check[j])
                check.pop(j)
                continue
            if (j > 0 and check[j-1] == source[ii:ii+len(check[j-1])]):                
                print((i, ii, j, check))
                ii += len(check[j-1])
                check.pop(j-1)                
                continue
            break
            
        if (len(check) == 0): result.append(i)    
    
    return result
    
target = "barxxfoothefooxyzbarman"
samples = ["bar", "foo", "xyz"]
print("find concat strings from {0} by {1} are {2}".format(target, samples, getConcatStrings(target, samples)))
    
