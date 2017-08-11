

def dooropen(n):
    doors = []
    for i in range(n+1):
        doors.append(1)     
    for i in range(1,n+1,1):
        for j in range(i,n+1,i):        	          	  
            doors[j] = 1 - doors[j]
            
    return doors
    
num = 100
doors = dooropen(num)
for i in range(len(doors)):
    if (doors[i] == 0):
        print("door {0} is opened".format(i))   