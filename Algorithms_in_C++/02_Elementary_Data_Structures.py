

def intopost(s):
    stack = []
    result = []
    x = ""
    for c in s:
        if ord(c) >= ord('0') and ord(c) <= ord('9'): x += c
        else: 
            if (x != ""): result.append(x) 
            x = ""
        if c == ')': result.append(stack.pop())
        if c == '+' or c == '-': stack.append(c)
        if c == '*' : stack.append(c)

    if x != "": result.append(x)
    while(len(stack)): result.append(stack.pop())
    #print(result)
    
    stack = []
    while(len(result) != 0):
        c = result.pop(0)
        if c == '+': c = int(stack.pop())+int(stack.pop())
        if c == '-': c = -int(stack.pop())+int(stack.pop())
        if c == '*': c = int(stack.pop())*int(stack.pop())
        stack.append(c)

    return stack.pop(0)

expr = "5+2*3"
print("{0}={1}".format(expr, intopost(expr)))
expr = "5*(((9-8)*(4*6))+7)"
print("{0}={1}".format(expr, intopost(expr)))
expr = "5*(((19-18)*(4*26))+37)"
print("{0}={1}".format(expr, intopost(expr)))

