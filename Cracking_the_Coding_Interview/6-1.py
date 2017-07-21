import itertools 

#TODO: from argv/argc
op = [ '+' ,'-' ,'*' ,'/' ]
item = [3 ,1 ,3 ,6]
answer = 8 

show_all = False
op_radix = len(op)
op_exp = len(item) - 1
op_count = pow(op_radix, op_exp) 
ass_count = len(list(itertools.permutations(range(3))))

print("count of operation and association is {0} {1}".format(op_count, ass_count))

def increase_index(index,radix,exp):
    index[0] += 1
    for i in range(exp):        
        if index[i] >= radix:
            index[i+1] += 1
            index[i] = 0
    return index            
        
indexList = []        
for i in range(op_exp):
    indexList.append(0)
 
for i in range(op_count):
    if i != 0:
        indexList = increase_index(indexList, op_radix, op_exp)
    eval_str = ""        
    for j in range(len(item)):
        if j != 0:
            eval_str += str(op[indexList[j-1]])
        eval_str += str(item[j])
    result = eval(eval_str)
    
    if (result == answer) or show_all:
        print(eval_str + "={0}".format(eval(eval_str)))
        
            
    
    