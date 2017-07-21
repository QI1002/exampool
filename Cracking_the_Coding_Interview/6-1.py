import sys
import itertools 

#TODO: from argv/argc
#TODO: not use eval
#TODO: use permutations

op = [ '+' ,'-' ,'*' ,'/' ]
item = [3 ,1 ,3 ,6, 2]
answer = 8 

show_all = False
op_radix = len(op)
op_exp = len(item) - 1
op_count = pow(op_radix, op_exp) 

associations = list(itertools.permutations(range(op_exp)))
ass_count = len(associations)

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

    for j in range(ass_count):
        assocList = [str(x) for x in item]
        for k in range(op_exp):
            kk = associations[j][k] 
            eval_str = ""
            eval_str += str(assocList[kk])
            eval_str += str(op[indexList[kk]])
            eval_str += str(assocList[kk+1])
            eval_str = "(" + eval_str + ")"                        
            for l in range(kk,0,-1):
                if not ')' in assocList[l]:
                    break
                assocList[l] = eval_str
            for l in range(kk+1,op_exp,1):
                if not ')' in assocList[l]:
                    break
                assocList[l] = eval_str               
            assocList[kk] = assocList[kk+1] = eval_str    
            #print(str(k)+str(assocList))
        #print(str(associations[j]) + " " +eval_str)
    
        try:
            result = eval(eval_str)
            if (result == answer) or show_all:
                print(eval_str + "={0}".format(result))            
        except:
            print(eval_str + "={0}".format(sys.exc_info()[0]))
            
        
            
    
    