

pool = ["test", "tester", "testertest", "testing", "testingtester", "testingtestering"]

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp
    
def sortStringLen(strings):
    count = len(strings)
    for i in range(count):
        minlen = i
        for j in range(i+1, count, 1):
            if (len(strings[minlen]) > len(strings[j])):
                minlen = j
        swap(strings, minlen, i)
        
    return strings             

# consider nested string match 
def isCombineString(strings, strlen, i):
    result = []
    match = strings[i]
    while(match != ""):
        for j in range(i-1, -1, -1):
            ll = strlen[j]
            if (len(match) >= ll and match[0:ll] == strings[j]):
                result.append(strings[j])
                match = match[ll:]
                continue
                
        break        
    
    return [] if (match != "") else result              
              
    
def findMaxCombine(strings):
    index = result = None
    count = len(strings)
    strlen = [len(strings[i]) for i in range(count)]
    for i in range(count-1, -1, -1):
        result = isCombineString(strings, strlen, i)
        if (len(result) != 0): 
            index = i
            break              
    return (None if (index == None) else strings[index]), result
     
sortStringLen(pool)
print(pool)
print(findMaxCombine(pool))