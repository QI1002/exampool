
#294. Flip Game II

MUSTWIN = 1
MUSTLOST = 0
NOTSURE = 2

def allFlip(s):    
    result = []
    for i in range(1, len(s)):
        if (s[i-1] == '+' and s[i] == '+'):
            result.append(s[:i-1]+"--"+s[i+1:])

    return result

gFlip = [ None, None, None ]
def winFlip(s, first = True):
    rr = allFlip(s)
    if (len(rr) == 0): return MUSTLOST
    if (len(s) < len(gFlip) and s == "+"*len(s)): 
        return gFlip[len(s)] 

    notSure = False
    for r in rr:
        rw = winFlip(r, not first)
        if (rw == MUSTLOST): return MUSTWIN
        if (rw != MUSTWIN): notSure = True 

    if (notSure): return NOTSURE
    return MUSTLOST
            
for i in range(3,25):
    given = "+"*i
    result = winFlip(given)
    gFlip.append(result)
    print("{0}:{1}".format(given, result))
