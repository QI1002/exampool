
#691. Stickers to Spell Word

import copy
import math
def analyze(s, ts = None):
    sd = {}
    for c in s:
        if (ts != None and not c in ts): 
            continue
        if (not c in sd):
            sd[c] = 1
        else:
            sd[c] += 1
    return sd

def collect(sds, tc):
    ass = {}
    for i in range(len(sds)):
        if (tc[i] == 0): continue
        for k in sds[i]:
            if (not k in ass):
                ass[k] = sds[i][k]*tc[i]
            else:
                ass[k] += sds[i][k]*tc[i]
    return ass 
 
def sticker(ss, t):

    sds = []
    ts = analyze(t)
    th = copy.copy(ts) 
    tc = [ 0 for i in range(len(ss)) ] 
    tcs = {}

    for i in range(len(ss)):
        sds.append(analyze(ss[i], ts))

    for k in ts:
        th[k] = []
        for i in range(len(sds)):
            if (k in sds[i]): th[k].append(i)  
   
    #print(ts, sds)
 
    for k in ts:
        if (k in tcs and tcs[k] >= ts[k]):
            continue
        if (len(th[k]) == 0):
            reutrn -1
        if (len(th[k]) == 1):
            i = th[k][0] 
            tc[i] += ts[k] 
            tcs = collect(sds, tc)

    #print((tc, th, tcs))

    rcs = {}
    for k in ts: 
        if (not k in tcs):
            rcs[k] = ts[k]
        else:
            if (tcs[k] < ts[k]):
                rcs[k] = (ts[k] - tcs[k])

    if (len(rcs) == 0):
        return tc
    else:
        #print((rcs, sds, th))
        ac = stickerAll(rcs, sds, th)
        for i in range(len(sds)):
            ac[i] += tc[i]
        return ac

def stickerAll(rcs, sds, th, ac = None):

    #print((rcs, sds, th))
    if (ac == None):
        ac = [ 0 for i in range(len(sds)) ]

    kk = [ k for k in rcs ]
    if (len(kk) == 0): return ac
 
    k = kk[0]
    min = 0
    mac = None
    for i in th[k]:
        ac2 = copy.deepcopy(ac)
        rcs2 = copy.deepcopy(rcs)
        ac2[i] += int(math.ceil(float(rcs[k])/sds[i][k]))
        tcs = collect(sds, ac2)
        for key in tcs: 
            if (not key in rcs2): continue
            if (tcs[key] >= rcs2[key]):
                del rcs2[key]
            else: 
                rcs2[key]-= tcs[key]
        acc = stickerAll(rcs2, sds, th, ac2)
        #print((i, acc, ac2, rcs[k], sds[i][k]))
        if (mac == None or sum(acc) < min):
            min = sum(acc)
            mac = acc
 
    return mac

print(sticker(["with", "example", "science"], "thehat"))
print(sticker(["with", "example", "sciencee"], "theeehat"))
print(sticker(["with", "example", "scienceaa"], "theeehat"))
print(sticker(["with", "example", "scienceaa"], "theehaat"))

