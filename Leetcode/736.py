
#736. Parse Lisp Expression

class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def add_op(op1, op2, var):
    if (op1 in var): op1 = var[op1]
    if (op2 in var): op2 = var[op2]
    return int(op1)+int(op2)

def mul_op(op1, op2, var):
    if (op1 in var): op1 = var[op1]
    if (op2 in var): op2 = var[op2]
    return int(op1)*int(op2)

def let_op(op1, op2, var):
    var[op1] = op2
    return None
    
def expr_div(s):
    result = []
    ii = i = 0
    np = 0
    while(i < len(s)):
        if (s[i] == "("):
            np += 1
        if (s[i] == ")"):
            np -= 1
 
        if (np == 0 and s[i] == " "):
            result.append(s[ii:i])
            i += 1
            ii = i
            continue

        i += 1
 
    result.append(s[ii:]) 
    return result
     
def lisp(expr, var = {}):
    s = stack()
    t = stack()
    s.push(expr)
    op1 = op2 = None

    while(not s.isEmpty()):
        expr = s.pop()
        #print(expr)
        if (expr[0] == "("):
            action = expr[1:4]
            r = expr_div(expr[5:-1])
            #print(r)

            if (action == "add" or action == "mul"):
                if (len(r) != 2): raise ValueError(expr[5:-1])
                s.push(dict(var))
                s.push(action)
                s.push(r[0])
                s.push(r[1])
                continue

            if (action == "let"):
                if (r[-1][0] != "("): s.push("("+r[-1]+")")
                else: s.push(r[-1])
                for i in range(len(r)-2,-1, -2):
                    #s.push(dict(var))
                    s.push("let")
                    s.push(r[i-1])
                    s.push(r[i])
                continue

            key = expr[1:-1]
            if (key in var): t.push(var[key])
            else: t.push(None)
            #print((key, var))                        
            continue

        if (expr == "add"):
            var = s.pop()
            op1 = t.pop()
            op2 = t.pop()
            rr = add_op(op1, op2, var)
            op1 = op2 = None
            s.push(str(rr))
            continue
               
        if (expr == "mul"):
            var = s.pop()
            op1 = t.pop()
            op2 = t.pop()
            rr = mul_op(op1, op2, var)
            op1 = op2 = None
            s.push(str(rr))
            continue 

        if (expr == "let"):
            #var = s.pop()
            op1 = t.pop()
            op2 = t.pop()
            let_op(op1, op2, var)
            op1 = op2 = None
            continue

        t.push(expr)
    
    return t.pop()

#print(expr_div("add 4 (mul 2 3) ((a b c) d)"))
print(lisp("(add 1 2)"))      
print(lisp("(mul 3 (add 2 3))"))
print(lisp("(mul (add 2 3) 3)"))
print(lisp("(let x 2 (mul x 5))"))
print(lisp("(let x 2 (mul x (let x 3 y 4 (add x y))))"))
print(lisp("(let x 3 x 2 x)"))
print(lisp("(let x 1 y 2 x (add x y) (add x y))"))
print(lisp("(let x 2 (add (let x 3 (let x 4 x)) x))"))
print(lisp("(let a1 3 b2 (add a1 1) b2)"))
