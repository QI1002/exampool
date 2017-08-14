
import random 

def rand5():
    return random.randint(1,5)
    
def rand7():
    r = 25
    while(r > 21):
        r = (rand5()-1) * 5 + rand5()
        
    return (r % 7)+1    
    
for i in range(10):    
    print(rand7())    