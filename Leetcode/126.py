
#126. Word Ladder II

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
        
def connect(s1, s2):
    if (len(s1) != len(s2)):
        return False
    
    diff = 0    
    for i in range(len(s1)):
        if (s1[i] != s2[i]): diff += 1
        
    return (diff == 1)
                
def ladder(s1, s2, di):
    if (len(s1) != len(s2)):
        return []
    
    s = stack()
    s.push([])
    s.push(s1) 
    while(not s.isEmpty()):
        n = s.pop()
        history = s.pop()
        history.append(n)
        if (connect(n, s2)):
            history.append(s2)
            return history                 
        for i in range(len(di)-1,-1,-1):
            if (connect(n, di[i])):
                s.push(history)
                s.push(di.pop(i))
                
    return []

dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladder("hit", "cog", dictionary))

                   
    