
#10. Regular Expression Matching

#TODO: use * and ?
def isMatch_old(s, rexp):
  
    if (rexp == "*"):
        return True
        
    j = 0
    for i in range(len(s)):

        if (j >= len(rexp)):
            return False
              
        if (s[i] == rexp[j] or rexp[j] == "?"):
            j += 1    
            continue
            
        result = False      
        if (rexp[j] == "*"):            
            for j in range(i, len(s)+1, 1):
                if (isMatch(s[j:], rexp[j+1:])):
                    result = True
                    
        return result
    
    return (j == len(rexp))

sort1 = "aa"
sort2 = "??"
print("isMatch(\"{0}\",\"{1}\")={2}".format(sort1, sort2, isMatch(sort1, sort2)))


#isMatch("aa","a") -> false
#isMatch("aa","aa") -> true
#isMatch("aaa","aa") -> false
#isMatch("aa", "a*") -> true
#isMatch("aa", ".*") -> true
#isMatch("ab", ".*") -> true
#isMatch("aab", "c*a*b") -> true 
