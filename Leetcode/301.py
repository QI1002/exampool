
#301 Remove Invalid Parentheses

import copy
def removeInvalidP(s):
    count = len(s)
    row = [ 0 for i in range(count) ]
    m = [ list(row) for i in range(count) ]

    for i in range(count):
        for j in range(count):
            m[i][j] = [""]

    for i in range(count):
        for j in range(count-i):
            start = j
            end = j + i
            if (i == 0):
                m[start][end] = [""]
            else:
                if (i == 1):
                    if (s[start] == "(" and s[end] == ")"):
                        m[start][end] = ["()"]
                else:
                    if (s[start] == ")"):
                        m[start][end] = list(m[start+1][end])
                    else:
                        if (s[start+1] == ")"):
                            m1 = [ "()"+x for x in m[start+2][end] ]
                        else:
                            m1 = list(m[start+1][end])

                        if (s[end] == ")"):
                            m2 = [ "("+x+")" for x in m[start+1][end-1] ]
                            if (s[end-1] == "("):
                                m3 = [ x + "()" for x in m[start][end-2] ]
                                if (len(m2) < len(m3)): m2 = m3
                                if (len(m2) == len(m3)):
                                    for x in m3:
                                        if (not x in m2): m2.append(x)
                        else:
                            m2 = list(m[start][end-1])

                        if (len(m1[0]) == len(m2[0])):
                            for x in m2:
                                if (not x in m1): m1.append(x)
                            m[start][end] = m1
                        else:
                            m[start][end] = m1 if (len(m1[0]) > len(m2[0])) else m2

    #for i in range(count): print(m[i])
    return m[0][count-1]

def removeInvalidP2(s):
    ss = ""
    for i in range(len(s)):
        if (s[i] == ")" or s[i] == "("): ss += s[i]

    result = []
    result2 = removeInvalidP(ss)
    for r in result2:
        sr = ""
        k = 0
        for i in range(len(s)):
            if (s[i] != ")" and s[i] != "("):
                sr += s[i]
            else:
                if (k < len(r) and s[i] == r[k]):
                    sr += s[i]
                    k += 1
        result.append(sr)
    return result

sample = ")("
print("{0} => {1}".format(sample, removeInvalidP2(sample)))

sample = "(()"
print("{0} => {1}".format(sample, removeInvalidP2(sample)))

sample = "())()"
print("{0} => {1}".format(sample, removeInvalidP2(sample)))

sample = "()())()"
print("{0} => {1}".format(sample, removeInvalidP2(sample)))

sample = "()()())"
print("{0} => {1}".format(sample, removeInvalidP2(sample)))

sample = "(a)())()"
print("{0} => {1}".format(sample, removeInvalidP2(sample)))
