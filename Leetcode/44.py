
#44. Wildcard Matching

def wildcard(data, pattern):

   if (len(data) == 0 and len(pattern) == 0):
       return True

   if (pattern == "*"):
       return True     
       
   j = 0   
   for i in range(len(pattern)):
        if (pattern[i] == '*'):
            for k in range(j, len(data)+1):
                if (wildcard(data[k:], pattern[i+1:])):
                    return True
            return False
        else:
            if (j >= len(data)): return False
            if (pattern[i] == data[j] or pattern[i] == '?'):
                j += 1
            else:
                return False    
   
   return (j == len(data))
   
print(wildcard("abc", "abc"))   
print(wildcard("abc", "ab"))
print(wildcard("abc", "abcd"))
print(wildcard("abc", "abc?"))
print(wildcard("abc", "?abc"))
print(wildcard("abc", "?bc"))
print(wildcard("abc", "ab?"))
print(wildcard("abc", "ab*"))
print(wildcard("abc", "*ab"))
print(wildcard("abc", "a*c"))
print(wildcard("abc", "*a*b*"))
print(wildcard("abc", "*a*b*c"))
print(wildcard("abc", "*a*c*b"))
print(wildcard("abc", "*a*?*b"))