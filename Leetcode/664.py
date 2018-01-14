
#664. Strange Printer

def sp(data):
    count = len(data)
    row = [ 0 for i in range(count+1) ]
    p = [ list(row) for i in range(count+1) ]

    for i in range(count): p[i][i] = 1
    for i in range(1, count, 1):
        for j in range(count):
            if ((j+i) >= count): continue
            m = 1 + p[j+1][j+i]
            #print((m, j, j+i)) 
            for k in range(j+1,j+i+1,1):
                if (data[k] != data[j]): continue
                mm = p[j][k-1] + p[k+1][j+i]
                if (mm < m): m = mm
            p[j][j+i] = m

    #print(p)
    return p[0][count-1]

print(sp("a"))
print(sp("ab"))
print(sp("aba"))
print(sp("abab"))
print(sp("abba"))
print(sp("abcba"))
print(sp("abccba"))
print(sp("abcbcba"))

                    
            
