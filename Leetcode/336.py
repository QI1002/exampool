
#336. Palindrome Pairs

def isPal(s):
    count = len(s) 
    for i in range(count//2):
        if (s[i] != s[count-1-i]):
            return False
    return True
            
def pairPal(words):
    count = len(words)
    result = []
    for i in range(count):
        for j in range(count):
            if (i == j): continue
            s = words[i] + words[j]
            if (isPal(s)): result.append((i,j,s))
            
    return result
            
words = ["bat", "tab", "cat"]
print(pairPal(words))            

words = ["abcd", "dcba", "lls", "s", "sssll"]
print(pairPal(words))            