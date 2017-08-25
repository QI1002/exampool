
# 87. Scramble String

def allScramble(s1):
  
    if (len(s1) == 1): 
        return [s1]

    count = len(s1)
    left = allScramble(s1[0:count//2])
    right = allScramble(s1[count//2:])

    result = []
    for i in range(len(left)):
        for j in range(len(right)):
            result.append(left[i]+right[j])
            result.append(right[j]+left[i])
            
    return result        
      
def isScramble(s1, s2):
    return s2 in allScramble(s1)
    
s1 = "great"
s2 = "rgtae"
s3 = "tgaer"
print("'{1}' is {2}the scramble string of '{0}'".format(s1, s2, "" if isScramble(s1, s2) else "not "))
print("'{1}' is {2}the scramble string of '{0}'".format(s1, s3, "" if isScramble(s1, s3) else "not "))
    
    