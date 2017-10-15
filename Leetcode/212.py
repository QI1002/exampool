
#212. Word Search II

def match(s, words):
    for i in range(len(words)):
        count = len(s)
        if (len(words[i]) >= count and words[i][:count] == s):
            return 2 if (len(words[i]) == count) else 1
    return 0

def wordSearch(data,words):

    rowc = len(data)
    colc = len(data[0])
    row = [0 for i in range(colc)]
    t1 = [ list(row) for i in range(rowc)]
    t2 = [ list(row) for i in range(rowc)]
    t3 = [ list(row) for i in range(rowc)]
    t4 = [ list(row) for i in range(rowc)]
    for j in range(rowc):
        for i in range(colc):
            t1[j][i] = [data[j][i]]
            t3[j][i] = [[(j,i)]]

    depth = 0
    for w in words:
        if (len(w)> depth): depth = len(w)

    result = []
    for k in range(1,depth,1):
        for j in range(rowc):
            for i in range(colc):
                next = []
                path = []
                c = data[j][i]
                if (j != 0):
                    next.extend(t1[j-1][i])
                    path.extend(t3[j-1][i])
                if (i != 0):
                    next.extend(t1[j][i-1])
                    path.extend(t3[j][i-1])
                if (j != (rowc-1)):
                    next.extend(t1[j+1][i])
                    path.extend(t3[j+1][i])
                if (i != (colc-1)):
                    next.extend(t1[j][i+1])
                    path.extend(t3[j][i+1])

                #print((next, path))
                for n in range(len(next)-1,-1,-1):
                    path[n] = list(path[n])
                    path[n].append((j,i))
                    next[n] += c
                    r = match(next[n], words)
                    if (r == 0):
                        next.pop(n)
                        path.pop(n)
                    if (r == 2):
                        result.append((next[n], path[n]))

                t2[j][i] = next
                t4[j][i] = path

        #print((k, t2, result))
        tmp = t2
        t2 = t1
        t1 = tmp
        tmp = t4
        t4 = t3
        t3 = tmp

    return result

board = [ ["o", "a", "a", "n"],
          ["e", "t", "a", "e"],
          ["i", "h", "k", "r"],
          ["i", "f", "l", "v"] ]
words = ["oath", "pea", "eat", "rain"]
print(wordSearch(board, words))