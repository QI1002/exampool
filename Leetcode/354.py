
#354. Russian Doll Envelopes

import copy
def dollEnv(env):
    
    count = len(env)
    path = []
    for i in range(count):
        for j in range(count):
            if (env[i][0] < env[j][0] and env[i][1] < env[j][1]):
                path.append((env[i], env[j]))

    print(path)
    result = copy.deepcopy(path)
    updated  = True
    while(updated):
        updated = False
        base = result 
        result = []
        for i in range(len(base)):    
            for j in range(len(path)):
                if (base[i][-1] == path[j][0]):
                    ll = list(base[i])
                    ll.append(path[j][1])
                    result.append(ll)
                    updated = True
  
    result = base
    #print(result)
    if (len(result) == 0):
        return None

    max = 0
    maxi = 0
    for i in range(len(result)):
        if (max < len(result[i])):
            max = len(result[i])
            maxi = i

    return result[maxi]

sample = [(5,4),(6,4),(6,7),(2,3)]
print(dollEnv(sample))

