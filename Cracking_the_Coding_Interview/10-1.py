

def game1(p):
    return p
    
def game2(p):
    return p*p*p + 3*p*p*(1-p)
    
def findEqual():
    for i in range(1,9,1):
        p = 0.1*i
        game1_p = game1(p)
        game2_p = game2(p)
        if (game1_p >= game2_p):
            print("the possibility of game 1,2 is {0:.2f},{1:.2f} based on {2:.2f}"
                  .format(game1_p, game2_p, p))            
        
findEqual()

    
    
    
    
            
