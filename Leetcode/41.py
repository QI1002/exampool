
#41. First Missing Positive
# don't consider the case with duplicated items

import random
def findLossPositive(data, count = 10):
    minvalue = maxvalue = 0
    slots = [ 0 in range(count) ]

    for i in data:
        if (i > 0 and maxvalue < i): maxvalue = i

    while(True):

        slots = [ 0 for i in range(count) ]
        p = (maxvalue - minvalue + count - 1) // count

        print((p, minvalue, maxvalue))
        for i in data:
            if (i <= minvalue or i > maxvalue): continue
            index = (i-minvalue-1)/p
            slots[index] += 1

        print(slots)
        if (p == 1):
            for i in range(maxvalue-minvalue):
                if (slots[i] == 0): return (i+1)+minvalue

        for j in range(count):
            if (slots[j] == 0): return (j*p+1)
            if (j == count-1):
                if (slots[j] == (maxvalue - j*p)):
                    return maxvalue + 1
                # maxvalue keep the same
                minvalue += j*p
                break
            else:
                if (slots[j] != p):
                    minvalue += j*p
                    maxvalue = minvalue + p
                    break

def generate(n, m):

    remain = [i for i in range(n)]
    result = []
    for i in range(n-1,0,-1):
        index = random.randint(0, i)
        result.append(remain.pop(index))
    for i in range(n):
        index = random.randint(0, n-1)
        result.insert(index, random.randint(n, n+100))

    return result, remain[0]

sample0 = [3,4,-1,6,-2,1]
sample1 = [3,4,-1,6,-2,1,12,7,8,9,2,5]
sample2 = [3,4,-1,6,-2,1,8,9,7,-3,-4,2,5,10,333]
sample, answer = generate(66, 7)
print((sample, answer))
print(findLossPositive(sample))
