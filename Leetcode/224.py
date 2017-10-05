
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

def calc(f):

    r = [f]
    check = 0
    while(True):
        for i in range(check, len(r), 1):
            if ('+' in r[i] or '-' in r[i]): 
                if (len(r[i]) == 1): check += 1
                else: break
            else: check += 1

        #print((check, r))          
        if (check >= len(r)): break
 
        rend = r[check+1:]
        r = r[:check+1]
        ff = r.pop(check)           
        end = len(ff)
        p = 0
        token = None
        for i in range(len(ff)-1,-1,-1):
            if (ff[i] == ')'): p += 1
            if (p > 0):
                if (ff[i] != "("): continue
                p -= 1
                if (p == 0): token = ff[i+1:end-1]

            if (ff[i] == '+' or ff[i] == '-'):
                r.append(ff[i])
                if (token != None): r.append(token)
                else: r.append(ff[i+1:end])
                token = None
                end = i

        if (end != 0): 
            if (token != None): r.append(token)
            else: r.append(ff[:end])

        r.extend(rend)

    s = stack()
    t = stack()
    s.body = r 
    while(len(s.body) != 0 or len(t.body) != 1):
        op = s.pop()
        if (op != '+' and op != '-'): t.push(int(op))
        else:
            #print((s.body,t.body))
            op2 = t.pop()
            op1 = t.pop()
            if (op == '-'): t.push(op1-op2)
            if (op == '+'): t.push(op1+op2)

    #print((s.body,t.body)) 
    return t.pop()

print(calc("1-2+3-4+5"))
print(calc("1-((2+3)-(4+5))"))
print(calc("1-(2)+3-4+5"))
print(calc("22-((33)+(5-4))"))
