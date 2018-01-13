
#689. Maximum Sum of 3 Non-Overlapping Subarrays

def max3(data, k):
    ss = []
    sss = []
    sl = []
    sr = []
    s = 0
    for i in range(k):
        s += data[i]

    ss.append(s)
    for i in range(k, len(data), 1):            
        s -= data[i-k]
        s += data[i]
        ss.append(s)

    #print(ss)

    sl.append(0)
    for i in range(1, len(ss), 1):
        prev = sl[-1]        
        sl.append(i if (ss[i] > ss[prev]) else prev) 
    #print(sl)

    sr.append(len(ss)-1)
    for i in range(len(ss)-2, -1, -1):
        prev = sr[0]
        sr.insert(0, i if (ss[i] > ss[prev]) else prev)
    #print(sr)

    for i in range(k, len(data)-2*k+1, 1):
        l = sl[i-k]
        r = sr[i+k]
        all3 = ss[l]+ss[r]+ss[i]
        sss.append((all3, l, i, r)) 
    #print(sss)

    if (len(sss) == 0): return []

    max = 0 
    for s, l, m ,r in sss:
        if (s > max): rr, max = (l,m,r), s

    return rr   

sample = [1,2,1,2,6,7,5,1]
print(max3(sample, 2))
sample = [1,2,1,2,6,7,5,1,4]
print(max3(sample, 3))

