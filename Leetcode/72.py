
#72. Edit Distance

def editDistance(s1, s2):
    count1 = len(s1)
    count2 = len(s2)
    
    row = [ 0 for i in range(count2+1) ]
    matrix = [ list(row) for i in range(count1+1) ] 
    row = [ [] for i in range(count2+1) ]
    action = [ list(row) for i in range(count1+1) ] 
    #track = [ list(row) for i in range(count1+1) ]
 
    for j in range(count2+1):
        matrix[0][j] = j
        action[0][j] = [ (i,'insert') for i in range(j) ]
         
    for i in range(1, count1+1, 1):
        matrix[i][0] = i
        action[i][0] = [ (j, 'remove') for j in range(i) ]
        for j in range(1, count2+1, 1):
            if (s1[i-1] == s2[j-1]):
                matrix[i][j] = matrix[i-1][j-1]
                action[i][j] = action[i-1][j-1]
                #track[i][j] = list(track[i-1][j-1])
                #track[i][j].append((i-1,j-1))
            else:
                r = matrix[i-1][j-1]+1
                n = matrix[i][j-1]+1
                m = matrix[i-1][j]+1
                
                if (r < n):
                    matrix[i][j] = r
                    action[i][j] = list(action[i-1][j-1])
                    action[i][j].append(((i-1,j-1), 'replace'))
                    #track[i][j] = list(track[i-1][j-1])
                    #track[i][j].append((i-1,j-1))
                else:
                    matrix[i][j] = n 
                    action[i][j] = list(action[i][j-1])
                    action[i][j].append((j-1, 'insert'))
                    #track[i][j] = list(track[i][j-1])
                    #track[i][j].append((i,j-1))
                    
                if (matrix[i][j] > m): 
                    matrix[i][j] = m
                    action[i][j] = list(action[i-1][j])
                    action[i][j].append((i-1, 'remove'))
                    #track[i][j] = list(track[i-1][j])
                    #track[i][j].append((i-1,j))
  
    #track[count1][count2].append((count1, count2)) 
    #print(track[count1][count2])                                
    return matrix[count1][count2], action[count1][count2]
    
print(editDistance("abcdefg", "acdefgh"))                
print(editDistance("abcdefg", "bcdefgh"))
print(editDistance("abcdefg", "zabcdef"))
print(editDistance("abcdefg", "azbcdef"))                
