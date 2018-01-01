
#630. Course Schedule III

def overlay(s1, s2):
    if (s1[0] <= s2[0] and s2[0] < s1[1]):
        return True
    if (s2[0] <= s1[0] and s1[0] < s2[1]):
        return True

    return False

  
def schedule(s):
    actions = [ i for i in range(len(s)) ]
    conflict = [ [] for i in range(len(s)) ]
    for i in range(len(s)):
        for j in range(i+1, len(s), 1):
            if (overlay(s[i], s[j])):
                conflict[i].append(j)
                conflict[j].append(i)

    #print(conflict)
    while(True):
        maxi = -1  
        for i in range(len(conflict)):
            if (maxi == -1 or len(conflict[maxi]) < len(conflict[i])):
                maxi = i
     
        if (maxi == -1 or len(conflict[maxi]) == 0): break     
        actions.remove(maxi)

        for k in conflict[maxi]: conflict[k].remove(maxi)
        conflict[maxi] = []

    return [ s[i] for i in actions]

schedule1 = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print(schedule(schedule1))

schedule2 = [[100, 200], [200, 1000], [1000, 1250], [2000, 3200]]
print(schedule(schedule2))

schedule3 = [[100, 200], [150, 1200], [1000, 2250], [2000, 3200]]
print(schedule(schedule3))

