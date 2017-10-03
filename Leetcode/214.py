
#214. Shortest Palindrome

def shortPal(s):
    count = len(s)
    row = [ 0 for i in range(count) ]
    m = [ list(row) for i in range(count) ] 

    for i in range(count):
        m[i][i] = 0

    for i in range(count):
        for j in range(count-i):
            start = j
            end = j + i

            if (start == end): continue
            if (s[start] == s[end]):
                m[start][end] = m[start+1][end-1] 
            else:
                if (m[start+1][end] < m[start][end-1]):
                    m[start][end] = m[start+1][end]+1
                else:
                    m[start][end] = m[start][end-1]+1
    
    #print(m)        
    return m[0][count-1]


print(shortPal("abccbd"))        
print(shortPal("abcdbd"))    
print(shortPal("abb"))    
print(shortPal("abba"))
print(shortPal("abbacd"))
print(shortPal("palindrome"))
 
