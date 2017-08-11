
def isEven(x,y):
    return (abs(x-y) & 1) == 0

def checkdomino(size, exclude):
    countOdd = 0
    countEven = 0
    for i in range(size):
        for j in range(size): 
        	  if ((i,j) in exclude):
        	      continue
        	  if (isEven(i,j)):
        	      countOdd += 1	
        	  else: 	    
        	      countEven += 1
        	      
    return countEven == countOdd
    
checkboard_size = 32    
exclude = [(0,0), (7,7)]
print("checkdomino (size={0}) result is {1}".format(checkboard_size, checkdomino(checkboard_size, exclude)))
        	      	