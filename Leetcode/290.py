
#290. Word Pattern 

def match(p, s):
    ps = {}
    sp = {}
    l = s.split(' ')
    if (len(l) != len(p)): return False
    for i in range(len(l)):
        pp, ll = p[i], l[i]
        if (not pp in ps and not ll in sp):
            ps[pp],sp[ll] = ll,pp 
        
        if (not pp in ps or ps[pp] != ll): 
            return False

        if (not ll in sp or sp[ll] != pp): 
            return False

    return True


p, s = "abba", "dog cat cat dog"
print("{0}:{1}".format((p,s),match(p,s)))
p, s = "abba", "dog cat cat fish"
print("{0}:{1}".format((p,s),match(p,s)))
p, s = "aaaa", "dog cat cat dog"
print("{0}:{1}".format((p,s),match(p,s)))
p, s = "abba", "dog dog dog dog"
print("{0}:{1}".format((p,s),match(p,s)))
