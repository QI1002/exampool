
#282. Expression Add Operators

def myEval(expr):
    #print(expr)
    t = expr.split(" ")
    #print(t)
    for i in range(len(t)-1,-1,-1):
        if (t[i] == "*"):
            op2 = t.pop(i+1)
            t.pop(i)
            op1 = t.pop(i-1)
            r = int(op1)*int(op2)
            t.insert(i-1, r)
    #print(t) 
    while(len(t) >= 3):
        op1 = t.pop(0)
        op = t.pop(0)
        op2 = t.pop(0)
        if (op == "+"): r = int(op1)+int(op2)
        else: r = int(op1)-int(op2)
        t.insert(0, r)
    #print(r)
    return t[0]           
                
def myEval2(expr):
    rr = -1
    try:
        rr = eval(expr)
    except:
        pass    
    return rr
    
def hitExpr(s, d, e = myEval):
    count = len(s)
    if (count <= 1):
        if (str(d) == s): return [s] 
        else: return []
        
    ops = [ "", " + ", " - ", " * " ]    
    ops2 = " +-*"
    rr = 0    
    result = []    
    all = 1 << (2*(count-1))
    print(all)
    
    # 0: no op , 1: + , 2: -, 3: *
    for key in range(1, all, 1):
        sl = list(s) 
        for p in range(count-1, 0, -1):
            op = (key >> (2*p-2)) & 0x3
            if (op != 0):
                if (e == myEval): sl.insert(p, ops[op])
                if (e == myEval2): sl.insert(p, ops2[op])
                
        expr = "".join(sl)
        #print(sl, expr)
        rr = e(expr)
        if (rr == d): result.append(expr)
            
    return result
        
print(hitExpr("123", 6))
print(hitExpr("232", 8))
print(hitExpr("105", 5))
print(hitExpr("3456237490", 9191))
    