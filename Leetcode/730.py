
#730. Count Different Palindromic Subsequences

def countPal(s):
    if (len(s) <= 1):
        return 1

    ss = {}

    for i in range(len(s)):
        x = s[i]
        if (x in ss):
            ss[x].append(i)
        else:
            ss[x] = [i]

    print(ss)

    allpals = 0
    for k in ss:
        sk = ss[k]
        for i in range(len(sk)):
            for j in range(i, len(sk)):
                #print(s[i+1:j])
                pals = countPal(s[i+1:j])
                allpals += pals
            
    return allpals

print(countPal("bccb"))
