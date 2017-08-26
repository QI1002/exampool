
#10. Regular Expression Matching

def makePattern(rexp):
    result  = []
    count = len(rexp)
    i = 0
    while(i < count):
        if ((i+1) < count and rexp[i+1] == "*"):
            result.append((rexp[i], True))
            i += 2
        else:
            result.append((rexp[i], False))
            i += 1
    return result

def isMatchInternal(s, pattern):
    
    #print((s, pattern))
    if (len(pattern) == 0):
        return len(s) == 0

    if (len(s) == 0):
        for j in range(len(pattern)):
            if (pattern[j][0] == False):
                return False
        return True

    c = s[0]    
    if (c == pattern[0][0] or pattern[0][0] == '.'):
        if (pattern[0][1] == True):
            if (isMatchInternal(s[1:], pattern)):
                return True
            return (isMatchInternal(s, pattern[1:]))
        else:
            return (isMatchInternal(s[1:], pattern[1:]))
    else:
        if (pattern[0][1] == False):
            return False
        return (isMatchInternal(s, pattern[1:]))

def isMatchInternalnew(s, pattern):

    i = 0
    j = 0
    while(i < len(s)):
        c = s[i]
        for j in range(len(pattern)):
            if (c == pattern[j][0] or pattern[j][0] == '.'):
                if (pattern[j][1] == True):
                    if (isMatchInternalnew(s[i+1:], pattern[j:])):
                        return True
                else:
                    i += 1
                    if (i >= len(s)):
                        break                             
            else:
                if (pattern[j][1] == False):
                    return False
                    
        return len(s[i:]) == 0

    for k in range(len(pattern[j:])):
        if (pattern[k][0] == False):
            return False
    return True

def isMatch(s, rexp):
    pattern = makePattern(rexp)
    #print(pattern)
    return isMatchInternal(s, pattern)

def isMatchnew(s, rexp):
    pattern = makePattern(rexp)
    #print(pattern)
    return isMatchInternalnew(s, pattern)

#use * and ?
def isMatch2(s, rexp):

    if (rexp == "*"):
        return True

    j = 0
    for i in range(len(s)):

        if (j >= len(rexp)):
            return False

        if (s[i] == rexp[j] or rexp[j] == "?"):
            j += 1
            continue

        result = False
        if (rexp[j] == "*"):
            for j in range(i, len(s)+1, 1):
                if (isMatch2(s[j:], rexp[j+1:])):
                    result = True

        return result

    return (j == len(rexp))

template = [
("aa", "a"),
("aa", "aa"),
("aaa", "aa"),
("aa", "a*"),
("aa", ".*"),
("ab", ".*"),
("bc", "b*"),
("abc", "a*"),
("abc", "a*.*"),
("aab", "c*a*b*"),
("abc", "c*a*b*"),
("aaa", "c*a*b*"),
]

for i in range(len(template)):
    sort1 = template[i][0]
    sort2 = template[i][1]
    print("isMatch(\"{0}\",\"{1}\")={2}".format(sort1, sort2, isMatch(sort1, sort2)))
    print("isMatchnew(\"{0}\",\"{1}\")={2}".format(sort1, sort2, isMatchnew(sort1, sort2)))
