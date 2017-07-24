import sys

stack = []
def subset_stack(data):
    stack.append(data)
    result = []
    while(len(stack)>0):
        data = stack.pop()
        #print(data)
        if (type(data) is int):
            more = [[data]]
            for x in result:
                t = list(x)
                t.insert(0, data)
                more.append(t)

            result.extend(more)
        else:
            if (len(data) == 1):
                result.append(data)
            else:
                stack.append(data[0])
                stack.append(data[1:])
    return result

def subset(data):
    if (len(data) == 1):
        result = []
        result.append(data)
        return result
    else:
        first = data[0]
        result = subset(data[1:])
        more = [[first]]
        #print(str(data) + " " + str(result))
        for x in result:
            t = list(x)
            t.insert(0, first)
            more.append(t)

        result.extend(more)
        return result

if (len(sys.argv) != 2 or int(sys.argv[1]) <= 0):
    print("python 8-3.py n (n>=1)")
    exit(0)

seed = list(range(1,int(sys.argv[1])+1,1))
answer = subset_stack(seed)
print("result{0}={1} with len = {2}".format(seed, answer, len(answer)))