

def intopost(s):
    #print(s)
    stack = []
    result = []
    ll = x = ""
    l = 0     
    for c in s:
        if (l > 0): 
            ll += c 
            if (c != '(' and c != ')'): continue

        if ord(c) >= ord('0') and ord(c) <= ord('9'): x += c
        else: 
            if (x != ""): 
                result.append(x) 
                if (len(stack) > 0 and stack[-1] == '*'): 
                    result.append(stack.pop())
            x = ""

        if c == '(': l += 1
        if c == ')': 
            l -= 1 
            if (l == 0):
                result.extend(intopost(ll[:-1]))
                ll = ""

        if c == '+' or c == '-': stack.append(c)
        if c == '*' : stack.append(c)

    if x != "": 
        result.append(x)
        if (len(stack) > 0 and stack[-1] == '*'): 
            result.append(stack.pop())

    while(len(stack) != 0): result.append(stack.pop())

    #print(result)
    return result

def calc(s):
   
    result = intopost(s) 
    stack = []
    while(len(result) != 0):
        c = result.pop(0)
        if c == '+': c = int(stack.pop())+int(stack.pop())
        if c == '-': c = -int(stack.pop())+int(stack.pop())
        if c == '*': c = int(stack.pop())*int(stack.pop())
        stack.append(c)

    return stack.pop(0)

expr = "(5*2)+3"
print("{0}={1}".format(expr, calc(expr)))
expr = "5*2+3"
print("{0}={1}".format(expr, calc(expr)))
expr = "(5+2)*3"
print("{0}={1}".format(expr, calc(expr)))
expr = "5+2*3"
print("{0}={1}".format(expr, calc(expr)))
expr = "5*(((9-8)*(4*6))+7)"
print("{0}={1}".format(expr, calc(expr)))
expr = "5*(((19-18)*(4*26))+37)"
print("{0}={1}".format(expr, calc(expr)))
expr = "(5*(((19-18)*(4*26))+37))"
print("{0}={1}".format(expr, calc(expr)))

