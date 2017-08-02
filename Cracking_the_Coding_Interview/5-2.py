import math

def trim_zero(str_value):

   tail = -1
   for i in range(len(str_value)-1,-1,-1):
       if (str_value[i] == '0'):
           tail = i
       else:
           break
                
   if (tail != -1):
       return str_value[0:tail]
   else:
       return str_value
                   
def binary_string(str_value):
    tail = -1
    dot = -1
    for i in range(len(str_value)-1,-1,-1):
        if (str_value[i] != '0' and str_value[i] != '.' and tail == -1):
            tail = i
        if (str_value[i] == '.' and dot == -1):
            dot = i
        
    value = float(str_value)    
    #print(str(tail) + ":" + str(dot))
    if (tail == -1 or dot > tail):
        value = int(value)
        result = bin(value)
    else:    
        frag = dot - tail
        binfrag = - math.floor(math.log(math.pow(10, frag), 2))        
        testvalue = value * math.pow(2,binfrag)
        #print(testvalue)
        if (int(testvalue) != testvalue):
            return "ERROR"
        else:
            result = bin(int(testvalue))
            #print(result)
            result = result[0:-binfrag] + '.' + result[-binfrag:]
            result = trim_zero(result)
            
    return result

print(binary_string("2.2500"))
#print(binary_string("2."))