
#726. Number of Atoms

def between(c, smax, smin):
    return ord(c) >= ord(smin) and ord(c) <= ord(smax)

def atoms(s):
    result = {}
    if (len(s) == 0): 
        return result

    np = 0
    ii = 0
    i = 0
    r = a = None
    while(i < len(s)):

        if (s[i] == '('):
            if (np == 0): ii = i
            np += 1
        if (s[i] == ')'):
            np -= 1
            if (np == 0):
                r = atoms(s[ii+1:i])
                i += 1
                continue

        if (np > 0): 
            i += 1
            continue

        if i < len(s) and between(s[i], 'Z', 'A'):
            ii = i
            i += 1
            while(i < len(s) and between(s[i], 'z', 'a')):
                i += 1
            r = { s[ii:i]: 1 } 

        if i < len(s) and between(s[i], '9', '0'):
            ii = i
            i += 1
            while(i < len(s) and between(s[i], '9', '1')):
                i += 1
            #print((r, s[ii:i]))
            for k in r: 
                r[k] = r[k]*int(s[ii:i])

        #print((r, i))
        if (r != None):
            for k in r: 
                if (k in result): result[k] += r[k]
                else: result[k] = r[k]
            r = None
   
    if (r != None):
        for k in r: 
            if (k in result): result[k] += r[k]
            else: result[k] = r[k]
        r = None
           
    return result

print(atoms("(C(H2O)2)3"))
print(atoms("Mg(OH)2"))
print(atoms("K4(ON(SO3)2)2"))   
print(atoms("K4(ON(SO3)2)"))    
print(atoms("K4(ON(S03)2)2"))     
 
