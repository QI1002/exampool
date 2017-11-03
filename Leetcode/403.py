
#403. Frog Jump

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

def frogJump2(steps):
    diff = []
    for i in range(1, len(steps), 1):
        diff.append(steps[i] - steps[i-1])
    
    for i in range(1, len(diff), 1):
        if (abs(diff[i] - diff[i-1]) > 1):
            return False

    return True

def frogJump(steps):
    
    s = stack()
    s.push(steps[:2])
    while(not s.isEmpty()):
        ss = s.pop()
        oldstep = ss[-1] - ss[-2]
        for i in range(-1,2,1):
            if ((oldstep+i) == 0): continue
            si = ss[-1] + oldstep + i
            if (si in steps):
                if (si == steps[-1]):
                    #print((ss,si))
                    return True
                else:
                    sss = list(ss)
                    sss.append(si)
                    s.push(sss)

    return False

steps = [0,1,3,5,6,8,12,17]
print("{0} => {1}".format(steps, frogJump(steps)))

steps = [0,1,2,3,4,8,9,11]
print("{0} => {1}".format(steps, frogJump(steps)))

