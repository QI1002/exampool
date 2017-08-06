
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

def sortStepStack(source):
    result = True
    convert = None
    local = stack()
    v = prev = None
    while(not source.isEmpty()):
        v = source.pop() 
        if (prev != None and v < prev):
            convert = v
            result = False
            break
        prev = v
        local.push(v)
        
    #print(local.body)
    #print(convert)
    
    while(not local.isEmpty()):
        v = local.pop() 
        if (convert != None and convert > v):
            source.push(convert)
            convert = None
        source.push(v)
            
    if (convert != None):
        source.push(convert)
                
    #print(source.body)
    #print("=======")
    return result
        
def sortStack(source):
    result = False
    while(result == False):
        result = sortStepStack(source)
            
#values = []    
#values = [0]             
#values = [3 ,2 ,1 ,0]
#values = [0 ,1 ,2 ,3]
#values = [ 3, 5, 2, 1, 4 ]
values = [ 3, 5, 2, 6, 1, 4 ]
mystack = stack()
for i in range(len(values)):
    mystack.push(values[i])

sortStack(mystack)    
for i in range(len(values)):
    print(mystack.pop())