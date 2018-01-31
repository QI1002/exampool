
#6. Zigzag Coversion

def ZZconvert(src):
    count = len(src)
    row1 = [ 0 if (i % 2) == 0 else None for i in range(count) ]
    row2 = [ 0 for i in range(count) ]
    mask = [ row1, row2, list(row1) ] 
    i = j = k = 0
    while(k < count):
        print((j,i,k,mask[j][i]))
        if (mask[j][i]!= None):
            mask[j][i] = src[k]
            k += 1
        j += 1
        if (j == 3): i,j = i+1, 0

    i = j = 0
    dest = ""
    for j in range(3):
        for i in range(count):
            if (mask[j][i] == 0): break
            if (mask[j][i] != None):
                dest = dest + mask[j][i]
    return dest              

def ZZconvertFast(src):
    dest = ""
    for i in range(0,len(src),4):
        dest = dest + src[i]
    for i in range(1,len(src),2):
        dest = dest + src[i]
    for i in range(2,len(src),4):    
        dest = dest + src[i]

    return dest

s = "PAYPALISHIRING"
print("{0} => {1},{2}".format(s, ZZconvert(s), ZZconvertFast(s)))


