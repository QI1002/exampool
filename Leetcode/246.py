
#246. Strobogrammatic Number

def stroNum(ss):
    mapping = { '8':'8', '9':'6', '6':'9', '1':'1' }
    count = len(ss)
    for i in range(count):
        j = count - i - 1
        if not ss[i] in mapping:
            return False
        if mapping[ss[i]] != ss[j]:
            return False
    return True

ss = "88"
print("{0}:{1}".format(ss, stroNum(ss)))
ss = "69"
print("{0}:{1}".format(ss, stroNum(ss)))
ss = "818"
print("{0}:{1}".format(ss, stroNum(ss)))
ss = "828"
print("{0}:{1}".format(ss, stroNum(ss)))

