
#311. Sparse Matrix Multiplication 


def MatrixMutiple(mA, mB):
    rowA, colA, v = mA.pop(0)
    rowB, colB, v = mB.pop(0)
    r = [ 0 for i in range(colB) ]
    rr = [ list(r) for i in range(rowA) ]
    
    rA = [ {} for i in range(rowA) ] 
    cB = [ {} for i in range(colB) ]

    for y,x,v in mA: rA[y][x] = v 
    for y,x,v in mB: cB[x][y] = v

    print((rA,cB))
    for j in range(rowA):
        for i in range(colB):
            sA = set(rA[j])
            sB = set(cB[i])
            sC = sA.intersection(sB)
            t = 0
            for s in sC: t += rA[j][s] * cB[i][s]
            rr[j][i] = t

    return rr 

giveA = [(2,3,None),(0,0,-1),(1,0,-1),(1,2,3)]
giveB = [(3,3,None),(0,0,7),(2,2,1)]
print(MatrixMutiple(giveA, giveB))
giveA = [(2,3,None),(0,0,-1),(1,0,-1),(1,2,3)]
giveB = [(3,3,None),(0,0,7),(2,2,1),(1,0,-1),(1,1,1)]
print(MatrixMutiple(giveA, giveB))

