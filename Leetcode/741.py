
#741. Cherry Pickup

def cherryPickup(data):
    rowc = len(data)
    colc = len(data[0])
    row = [ 0 for i in range(colc) ]

    dp1 = [ list(row) for i in range(rowc) ]
    # left = 0, top = 1
    dpp1 = [ list(row) for i in range(rowc) ] 

    for k in range(1, rowc+colc-1, 1):
        for kc in range(k+1):
            kr = k - kc  
            if (kc >= colc or kr >= rowc or kr < 0):
                continue
            if (data[kr][kc] == -1): 
                dp1[kr][kc] = -1
                continue
            if (kr == 0 or dp1[kr-1][kc] == -1):
                if (dp1[kr][kc-1] == -1): 
                    dp1[kr][kc] = -1
                else:
                    dp1[kr][kc] = data[kr][kc] + dp1[kr][kc-1]                       
            else: 
                if (kc == 0 or dp1[kr][kc-1] == -1):
                    if (dp1[kr-1][kc] == -1):
                        dp1[kr][kc] = -1 
                    else:
                        dpp1[kr][kc] = 1
                        dp1[kr][kc] = data[kr][kc] + dp1[kr-1][kc]
                else:
                    if (dp1[kr][kc-1] >= dp1[kr-1][kc]):
                        dp1[kr][kc] = data[kr][kc] + dp1[kr][kc-1]
                    else:  
                        dpp1[kr][kc] = 1
                        dp1[kr][kc] = data[kr][kc] + dp1[kr-1][kc]

    print((dp1, dpp1))
    if (dp1[-1][-1] == -1): return -1 

    kr = rowc -1
    kc = colc -1 
    data[kr][kc] = 0
    while(kr != 0 or kc != 0):
        if (dpp1[kr][kc] == 1):
            kr -= 1
        else:
            kc -= 1 
        data[kr][kc] = 0

    print(data)
   
    dp2 = [ list(row) for i in range(rowc) ]
    # right = 0, bottom = 1
    dpp2 = [ list(row) for i in range(rowc) ] 

    for k in range(rowc+colc-3, -1, -1):
        for kc in range(k+1):
            kr = k - kc  
            if (kc >= colc or kr >= rowc or kr < 0):
                continue
            if (data[kr][kc] == -1): 
                dp2[kr][kc] = -1
                continue
            if (kr == (rowc-1) or dp2[kr+1][kc] == -1):
                if (dp2[kr][kc+1] == -1): 
                    dp2[kr][kc] = -1
                else:
                    dp2[kr][kc] = data[kr][kc] + dp2[kr][kc+1]                       
            else: 
                if (kc == (colc-1) or dp2[kr][kc+1] == -1):
                    if (dp2[kr+1][kc] == -1):
                        dp2[kr][kc] = -1 
                    else:
                        dpp2[kr][kc] = 1
                        dp2[kr][kc] = data[kr][kc] + dp2[kr-1][kc]
                else:
                    if (dp2[kr][kc+1] >= dp2[kr+1][kc]):
                        dp2[kr][kc] = data[kr][kc] + dp2[kr][kc+1]
                    else:  
                        dpp2[kr][kc] = 1
                        dp2[kr][kc] = data[kr][kc] + dp2[kr+1][kc]

    print((dp2, dpp2))
    if (dp2[-1][-1] == -1): return -1
 
    return dp1[-1][-1] + dp2[0][0] 
      
grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
print(cherryPickup(grid)) 

grid = [[0, 1, -1], [1, -1, -1], [-1, 1, 1]]
print(cherryPickup(grid)) 

