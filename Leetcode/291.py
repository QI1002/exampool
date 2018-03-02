
#291. Word Pattern II 

def getLens(p, d, kk, count):
    cc = count
    k = kk[-1]
    kc = 0
    for c in p: 
        if (c == k): kc += 1
        else: cc -= d[c]

    if (cc != 0 and cc == kc * (cc//kc)): 
        d[k] = cc//kc
        return True
    else:
        return False

def nextLens(p, count):
    d = {}
    for c in p: 
        if (not c in d): d[c] = 1
    kk = sorted(d.keys())
    kl = len(kk)-1

    if (kl == 0):
        r = getLens(p, d, kk, count)
        if (r): yield d
        return

    j = 0
    while(True):
        r = getLens(p, d, kk, count)
        if (r == False):
            j += 1
            while(r == False):                
                if (j >= kl): break 
                d[kk[j]] += 1
                for i in range(j): d[kk[i]] = 1
                r = getLens(p, d, kk, count)
                if (r == False): j += 1
                else: j = 0                
            if (j >= kl): break 
        else: 
            yield dict(d)
            d[kk[j]] += 1

    #print("end")        

def match(p, s, d):

    ps = {}
    sp = {}
    l = []
    i = 0
    for c in p: 
        j = i+d[c]
        l.append(s[i:j])
        i = j

    if (i != len(s)): raise ValueError("assert") 
    for i in range(len(l)):
        pp, ll = p[i], l[i]
        if (not pp in ps and not ll in sp):
            ps[pp],sp[ll] = ll,pp 
        
        if (not pp in ps or ps[pp] != ll): 
            return False

        if (not ll in sp or sp[ll] != pp): 
            return False

    return True

def matchAll(p, s):
    it = nextLens(p, len(s))
    #it2 = nextLens(p, len(s))
    #print(list(it2))
    while(True):
        try: d = it.next()
        except StopIteration: break
        #print(d)
        r = match(p, s, d)
        if (r): return True
    return False    
    
print(matchAll("abab", "redblueredblue"))
print(matchAll("abcabc", "redblueredblue"))
print(matchAll("aaaa", "asdasdasdasd"))
print(matchAll("abba", "redbluebluered"))
print(matchAll("aabb", "xyzabcxzyabc"))

