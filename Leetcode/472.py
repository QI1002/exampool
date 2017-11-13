
#472. Concatenated Words 

def generateStr(inputs, indexes):
    result = ""
    for i in range(len(indexes)):
        result += inputs[indexes[i]]
    return result
        
def concatWords(inputs):
    next = [ [i] for i in range(len(inputs)) ]
    indexes = []
    for i in range(1, len(inputs)):
        base = next
        next = []
        for x in base:
            for j in range(len(inputs)):
                if (j in x): continue                    
                xx = list(x)
                xx.append(j)
                next.append(xx)
                indexes.append(xx)
                
    result = []            
    for x in indexes:
        s = generateStr(inputs, x)
        if (s not in result): result.append(s)
        
    return result

samples = ["a", "b", "c"]
print(concatWords(samples))
     
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
     
def findConcatWords(inputs, s):
    ss = stack()
    ss.push((s, []))
    while(not ss.isEmpty()):
        t = ss.pop()
        if (len(t[0]) == 0):
            if (len(t[1]) > 1): return t[1]
            else: continue
        for x in inputs:
            if (len(t[0]) >= len(x) and t[0][:len(x)] == x):
                y = list(t[1])
                y.append(x)
                ss.push((t[0][len(x):], y)) 
                     
    return None
                     
inputs = ["cat", "cats", "catsdogcats", "dog", "hippopotamuses", "rat", "ratdogcatrat"]        
outputs = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
for s in outputs:
    print("{0}:{1}".format(s, findConcatWords(inputs, s)))