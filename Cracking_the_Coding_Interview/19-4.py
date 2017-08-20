

def max(a, b):

   for i in range(31,-1,-1):
       mask = (1 << i)       
       abits = a & mask 
       bbits = b & mask
       if (abits != 0 and bbits == 0):
           return a 
       if (bbits != 0 and abits == 0):
           return b
           
   return a        
            
a = 5
b = 10         
print("the max of {0} and {1} is {2}".format(a,b,max(a,b)))        