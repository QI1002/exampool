
#249. Group Shifted Strings

def groupStr(ss):

    if ((len(ss)) == 0): 
        return []

    group = [[ss[0]]]
    for j in range(1, len(ss)):
        s = ss[j]    
  
        match = False 
        for g in group:
            if (len(s) != len(g[0])):
                continue
            d = ord(s[0]) - ord(g[0][0])
            for i in range(1,len(s)):
                if (d != (ord(s[i]) - ord(g[0][i]))):
                    continue

            g.append(s)
            match = True
            break

        if (match == False):
            group.append([s])

    return group

given = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print("{0}:{1}".format(given, groupStr(given)))

