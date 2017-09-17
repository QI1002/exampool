
#72. Edit Distance

def editDistance(s1, s2):
    count1 = len(s1)
    count2 = len(s2)
    
    row = [ 0 for i in range(count2) ]
    matrix = [ list(row) for i in range(count1) ] 
    row = [ [] for i in range(count2) ]
    action = [ list(row) for i in range(count1) ] 
    
    for j in range(count2):
        matrix[0][j] = j
        action[0][j] = [ (i,'n') for i in range(j) ]
        
    for i in range(1, count1, 1):
        matrix[i][0] = i
        action[i][0] = [ (j, 'm') for j in range(i) ]
        for j in range(1, count2, 1):
            if (s1[i] == s2[j]):
                matrix[i][j] = matrix[i-1][j-1]
                action[i][j] = action[i-1][j-1]
            else:
                r = matrix[i-1][j-1]+1
                n = matrix[i][j-1]+1
                m = matrix[i-1][j]+1
                
                if (r < n):
                    matrix[i][j] = r
                    action[i][j] = list(action[i-1][j-1])
                    action[i][j].append(((i,j), 'r'))                    
                else:
                    matrix[i][j] = n 
                    action[i][j] = list(action[i][j-1])
                    action[i][j].append((j, 'n'))
                    
                if (matrix[i][j] > m): 
                    matrix[i][j] = m
                    action[i][j] = list(action[i-1][j])
                    action[i][j].append((i, 'm'))
                                    
    return matrix[count1-1][count2-1], action[count1-1][count2-1]
    
print(editDistance("abcdefg", "acdefgh"))                
                