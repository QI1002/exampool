
#Input: DAMP, LIKE
#Output: DAMP -> LAMP -> LIMP -> LIME -> LIKE
#     ['DAMP', 'LIKE', 'DAME', 'DIKE', 'LAKE', 'DIME', 'LIME', 'LAME', 'DIMP', 'LIMP', 'LAMP']
#All: ['DAMP', 'LIKE', 'DAME', 'DAKE', 'DIKE', 'LAKE', 'DIME', 'LIME', 'LAME', 'DAKP', 'DIKP', 'LIKP', 'LAKP', 'DIMP', 'LIMP', 'LAMP']

import copy

myDict = ['DAMP', 'LIKE', 'DAME', 'DIKE', 'LAKE', 'DIME', 'LIME', 'LAME', 'DIMP', 'LIMP', 'LAMP']

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
        
def strReplace(source, i, c):
    data = list(source)        
    data[i] = c
    return "".join(data)
    
def showAllTransforms(word1, word2):
    
    result = [word1, word2]
    if (len(word1) != len(word2)):
        return result
    
    ss = stack()
    ss.push(word1)
    count = len(word1)    
    while(not ss.isEmpty()):
        v = ss.pop()  
            
        if (not v in result):
            result.append(v)
          
        for i in range(count):
            if (v[i] != word2[i]):
                vv = strReplace(v, i, word2[i])
                if (vv != word2):
                    ss.push(vv)
                    
    return result        
            
def dictTransform(word1, word2, checkDict):
  
    result = []
    if (len(word1) != len(word2)):
        return result
    
    ss = stack()
    ss.push([word1])
    count = len(word1)    
    while(not ss.isEmpty()):
        track = ss.pop()  
        v = track.pop()
        track.append(v)
        for i in range(count):
            if (v[i] != word2[i]):
                vv = strReplace(v, i, word2[i])
                if (vv in checkDict):
                    newtrack = list(track)                    
                    newtrack.append(vv)
                    if (vv == word2):
                        result.append(newtrack)
                    else:
                        ss.push(newtrack)

    return result     
        
        
#print(showAllTransforms("DAMP", "LIKE"))
alls = dictTransform("DAMP", "LIKE", myDict)
for i in range(len(alls)):
    print(alls[i])