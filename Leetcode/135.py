
#135. Candy


def candy2(data):
    children = list(data)
    upper = []
    lower = []
    start = 0
    end = len(children)-1
    grad = 0
    endgrad = 0
    for i in range(1, len(children), 1):
        if (children[i-1] != children[i]):
            t = 1 if (children[i-1] < children[i]) else -1
        else:  
            t = 0
        
        if (i == 1):
            grad = t
            continue
            
        if ((grad * t) > 0):  grad += t
        else:
            if (t != 0):
                newstart = i if (children[start] == children[i-1]) else i-1
                if (children[start] < children[newstart]): 
                    lower.append(start)
                    endgrad = 1
                else: 
                    upper.append(start)
                    endgrad = 0
                start = newstart
                grad = t
   
    t = children[len(children)-1] 
    if (grad != 0 and endgrad == 1): 
        upper.append(start)
        tt = t+1 if (children[start] > t) else t-1
        children.append(tt)
        lower.append(end+1)
    if (grad != 0 and endgrad == 0): 
        lower.append(start)
        tt = t+1 if (children[start] > t) else t-1
        children.append(tt)
        upper.append(end+1)
        
    print((upper, lower))
    
    result = [1 for i in range(len(children))]
    if (grad == 0): 
        return sum(result), result
    
    i = j = 0    
    inc = 0 in lower 
    while(True):
        c = 1
        if (inc):
            for k in range(lower[i]+1, upper[j]+1, 1):
                if (children[k] > children[k-1]): c += 1
                result[k] = c
            if (upper[j] >= end): break                            
            i += 1
        else: 
            t = result[upper[j]]
            for k in range(lower[i]-1, upper[j]-1, -1):
                if (children[k+1] < children[k]): c += 1
                result[k] = c                
            if (t > result[upper[j]]): result[upper[j]] = t
            if (lower[i] >= end): break            
            j += 1

        inc = not inc            
     
    #return sum(result), result       
    return sum(result[0:-1]), result[0:-1]
    
def candy(children):

    state = [ 0 for i in range(len(children)) ]
    prev = 0
    for i in range(1, len(children), 1):
        if (children[i-1] != children[i]):
            state[i] = 1 if (children[i-1] < children[i]) else -1
            prev = state[i]
        else:  
            state[i] = prev
            
    if (state[0] == 0):
        prev = 0
        for i in range(len(children)-1, -1, -1):
            if (state[i] != 0): prev = state[i]
            else: state[i] = prev * -1
        if (prev == 0): 
            return [ 1 for i in range(len(children)) ]    
                         
    state.append(state[len(children)-1]* -1)                  
    #print(state)

    result = [ 1 for i in range(len(children)) ] 
    for i in range(len(children)):
        if (state[i] == -1 and state[i+1] == 1):
            start = i
            c = 1
            for j in range(start-1, -1, -1):
                if (state[j] != -1): break
                if (children[j] > children[j+1]): c += 1 
                result[j] = c
                
            if (start != 0 and state[j] == 1):
                c += 1
                if (result[j] < c): result[j] = c
                for k in range(j-1, -1, -1):
                    if (result[k] == 1 and state[k] == 1):
                        result[k] = c
                
            c = 1    
            for j in range(start+1, len(children), 1):
                if (state[j] != 1): break 
                if (children[j] > children[j-1]): c += 1
                result[j] = c 
                    
    return result   
            
children = [ 2,2,2,2,1,1 ]
print("{0}=>{1}".format(children, candy(children)))
children = [ 1,1,2,2,2,2 ]
print("{0}=>{1}".format(children, candy(children)))
children = [ 1,1,2,2,2,2,1,1 ]
print("{0}=>{1}".format(children, candy(children)))
children = [2,2,2,2]
print("{0}=>{1}".format(children, candy(children)))
children = [ 1,1,1,1,2,2 ]
print("{0}=>{1}".format(children, candy(children)))
children = [ 2,2,1,1,1,1 ]
print("{0}=>{1}".format(children, candy(children)))
children = [ 2,2,1,1,1,1,2,2 ]
print("{0}=>{1}".format(children, candy(children)))

children = [ 1,2,3,4,2,1 ]
print("{0}=>{1}".format(children, candy(children)))
children = [ 1,2,4,3,2,1 ]
print("{0}=>{1}".format(children, candy(children)))

children = [ 4,3,2,1,2,3 ]
print("{0}=>{1}".format(children, candy(children)))
children = [ 3,2,1,2,3,4 ]
print("{0}=>{1}".format(children, candy(children)))

