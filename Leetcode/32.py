
#32. Longest Valid Parentheses

def updateMax(maxstart, maxend, start, end):
    if (maxend - maxstart) < (end-start):
        maxstart = start
        maxend = end
    return maxstart, maxend 

def pValid1(p):
    count = len(p)
    depth = 0
    maxstart = maxend = 0
    end = start = 0
    for i in range(count):

        if (p[i] != '(' and p[i] != ')'):
            depth = -1
            continue

        if (depth < 0):
            depth = 0
            start = i

        if (p[i] == '('): depth += 1
        if (p[i] == ')'):
            depth -= 1
            if (depth == 0):
                end = i
                maxstart, maxend = updateMax(maxstart, maxend, start, end)

        #print((i,maxstart, maxend, depth,start))
        
    return maxstart, maxend
  
def pValid2(p):
    count = len(p)
    depth = 0
    maxstart = maxend = 0
    end = start = count-1
    for i in range(count-1,-1,-1):

        if (p[i] != '(' and p[i] != ')'):
            depth = -1
            continue

        if (depth < 0):
            depth = 0
            end = i

        if (p[i] == ')'): depth += 1
        if (p[i] == '('):
            depth -= 1
            if (depth == 0):
                start = i
                maxstart, maxend = updateMax(maxstart, maxend, start, end)

        #print((i,maxstart, maxend, depth, end))

    return maxstart, maxend

def pValid(p):
    maxstart, maxend = pValid1(p)
    start, end = pValid2(p)
    return updateMax(maxstart, maxend, start, end)

value = "(()"
print("the max valid parentheses of {0} is {1}".format(value, pValid(value)))

value = "(()(())("
print("the max valid parentheses of {0} is {1}".format(value, pValid(value)))

value = ")()(()))"
print("the max valid parentheses of {0} is {1}".format(value, pValid(value)))

value = "(()(()))"
print("the max valid parentheses of {0} is {1}".format(value, pValid(value)))

value = ")()(())("
print("the max valid parentheses of {0} is {1}".format(value, pValid(value)))

value = "()(())"
print("the max valid parentheses of {0} is {1}".format(value, pValid(value)))
