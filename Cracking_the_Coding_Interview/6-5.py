
import math

def dropTwoEggsStep(n, step):
    prev = 0
    for i in range(1,n+1, 1):
        current = i*step + i - i*(i+1)/2         
        #current = prev + 1 - i + step
        total = current - prev -1 + i
        #print("stage {0} to floor {1} with {2} steps".format(i, current, total))
        
        if (current > n):
            return True
        if (prev > current):
            print("this step {0} is not feasible for {1}".format(step, n))
            return False
                    
        prev = current    
        
    return False
                
def dropTwoEggs(n):
    ## 0.5 = 1/2 (2 eggs)
    start = int(math.pow(n, 0.5)) 
    while(True):
        if (dropTwoEggsStep(n, start)):
            break  
        start += 1
      
    return start

floor_num = 1000
print("the floor {0} has min steps of {1}".format(floor_num, dropTwoEggs(floor_num)))


