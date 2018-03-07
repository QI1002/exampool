
#323. Number of Connected Components in an Undirected Graph 

def connected2(n, con):
    
    group = [ i for i in range(n) ] 

    for x,y in con:
        gx,gy = group[x],group[y]
        min = gx if gx < gy else gy
        max = gy if gx < gy else gx
        for j in range(n):
            if (group[j] == max): group[j] = min

    result = []
    for j in range(n):
        if (not group[j] in result):
            result.append(group[j])

    return len(result), group

def connected(n, con):
    
    group = [ i for i in range(n) ] 
    member = [ [i] for i in range(n) ]

    for x,y in con:
        gx,gy = group[x],group[y]
        min = gx if gx < gy else gy
        max = gy if gx < gy else gx
        for c in member[max]:
            member[min].append(c)
            group[c] = min
        member[max] = []

    result = []
    for j in range(n):
        if (not group[j] in result):
            result.append(group[j])

    return len(result), group

given = 5, [(0,1),(1,2),(3,4)]
print("{0}:{1}".format(given, connected(*given)))
given = 5, [(0,1),(1,2),(2,3),(3,4)]
print("{0}:{1}".format(given, connected(*given)))


