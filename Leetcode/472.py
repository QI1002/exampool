
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
     
#samples = ["cat", "cats", "catsdogcats", "dog", "hippopotamuses", "ratdogcatrat"]        
samples = ["a", "b", "c"]
print(concatWords(samples))