
#466. Count The Repetitions

def repStr(s, n):
    return s*n
    
def countMatch(s1, s2):
    count = 0
    j = 0
    for i in range(len(s1)):
        if (s1[i] == s2[j]): j += 1 
        if (j == len(s2)): 
            count += 1 
            j = 0             
    return count
                
print(countMatch(repStr("acb", 4), repStr("ab", 2)))    
print(countMatch(repStr("aaa", 3), repStr("aa", 2)))

  