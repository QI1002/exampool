

def grid_walk(x,y):
    if (x == 1 or y == 1):
        if (x == 1):
            return [[ 'D' for i in range(y-1) ]]
        else:
            return [[ 'R' for i in range(x-1) ]]
    else:
        result = []

        resultx = grid_walk(x-1, y)
        resulty = grid_walk(x, y-1)
        print(resultx)
        print(resulty)
        for x in resultx:
            l = list(x)
            l.insert(0, 'R')
            result.append(l)

        for y in resulty:
            l = list(y)
            l.insert(0, 'D')
            result.append(l)

        return result

walks = grid_walk(5, 5)
print("all walks = {0} with length = {1}".format(walks, len(walks)))