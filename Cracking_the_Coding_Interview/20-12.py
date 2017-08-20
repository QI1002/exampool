
import random 

def printMatrix(matrix):
    count = len(matrix)
    for i in range(count):
        print(matrix[i])
        
def genRandomMatrix(m,n,min,max):
    matrix = []
    for y in range(n):
        matrix.append([])
        for x in range(m):
            matrix[y].append(random.randint(min,max))
    return matrix        
      
def findMaxSum2D_min(data):    
    
    maxStart = 0
    maxEnd = 0    
    sumdata = []
    minsumdata = []
    
    for j in range(len(data)):
        data[j].insert(0, 0)
        count = len(data[j])
        maxValue = data[0][0]  
        minValue = 0 
        sumrow = [0]
        minsumrow = [0]
        sumdata.append([0])
        minsumdata.append([(0,0)])
        for i in range(1, count, 1):
            sumrow.append(data[j][i] + sumrow[i-1])
            sumdata[j].append(sumrow[i] if (j == 0) else (sumrow[i]+sumdata[j-1][i]))
            v = sumdata[j][i] - sumdata[j][minsumdata[j][i-1][1]]
            
            if (maxValue < v):
                maxValue = v
                maxStart = minsumdata[j][i-1]
                maxEnd = (j, i)
                
            if (minValue > sumdata[j][i]):
                minValue = sumdata[j][i]
                minsumrow.append(i)
            else:
                minsumrow.append(minsumrow[i-1])
            
            if (j != 0 and minValue > sumdata[minsumdata[j-1][i][0]][minsumdata[j-1][i][1]]):
                minsumdata[j].append(minsumdata[j-1][i])
            else:
                minsumdata[j].append((j,minsumrow[i]))
                
        data[j].pop(0)
        
    return (maxValue, maxStart, (maxEnd[0], maxEnd[1]-1), sumdata, minsumdata)
    
#TODO: it works well in boundary ?    
def findMaxSum2D_exhaust(data):    
    
    maxStart = 0
    maxEnd = 0          
    maxValue = data[0][0]
    sumdata = []
    
    for j in range(len(data)):
        data[j].insert(0, 0)
        count = len(data[j])
        sumrow = [0]
        sumdata.append([0])        
        for i in range(1, count, 1):
            sumrow.append(data[j][i] + sumrow[i-1])
            sumdata[j].append(sumrow[i] if (j == 0) else (sumrow[i]+sumdata[j-1][i]))
                   
            for y in range(j+1):
                for x in range(1,i+1,1):
                    if (j == y or i == x):
                        v = sumdata[j][i] - sumdata[y][x]  
                    else:  
                        v = sumdata[j][i] - sumdata[y][i] - sumdata[j][x] + sumdata[y][x]
                        
                    if (maxValue < v):                        
                        maxValue = v
                        if (j == y): 
                                maxStart = (0, x)
                        else:
                            if (i == x):
                                maxStart = (y+1, 0)                        
                            else:
                                maxStart = (y+1, x)
                                
                        maxEnd = (j, i)
                        print((v, (y,x), maxEnd))
                
        data[j].pop(0)
        
    return (maxValue, maxStart, (maxEnd[0], maxEnd[1]-1), sumdata, sumdata)
        
findMaxSum2D = findMaxSum2D_exhaust
#template = [[-3, 2, -4, 6], [9, 10, -4, -1], [0, 10, -5, -5], [4, -1, 2, 8]]
template = [[3, -8, 7, -5], [4, 2, 3, 2], [-7, -4, 5, 5], [-7, 8, 7, 0]] 
#template = genRandomMatrix(4,4,-10, 10)
#print(mat)
printMatrix(template)
m1,m2,m3,m4,m5 = findMaxSum2D(template)
print("the max sum of {0} is {1} from {2} to {3}".format(template, m1, m2, m3))
print("========")
printMatrix(m4)
print("========")
printMatrix(m5)


template = [2, -8, 3, -2, 4, -10]
m1,m2,m3,m4,m5 = findMaxSum2D([template])
print("the max sum of {0} is {1} from {2} to {3}".format(template, m1, m2, m3))
template = [2, -8, -3, -2, -4, 10]
m1,m2,m3,m4,m5 = findMaxSum2D([template])
print("the max sum of {0} is {1} from {2} to {3}".format(template, m1, m2, m3))