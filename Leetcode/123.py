
#15. Best Time to Buy and Sell Stock II

def overlay(a, b):
    if (a[0] <= b[0] and b[0] <= a[1]): return True
    if (b[0] <= a[0] and a[0] <= b[1]): return True
    return None 

def bestBuy(data):
    minx = []
    profits = []
    min = 0
    for i in range(len(data)):
        if (data[i] < data[min]):  min = i
        minx.append(min)
        profits.append(data[i]-data[min])
    
#find the max profits for single transaction
    max = 0
    for i in range(len(data)):      
        if (profits[i] > profits[max]):
            max = i

    max1 = 0
    max2 = 1

#find the max profits for pair transactions        
    for i in range(len(data)):
        for j in range(i+1, len(data), 1):
            if (overlay((minx[i], i), (minx[j], j)) == None):
                if ((profits[i] + profits[j]) > (profits[max1] + profits[max2])):
                    max1 = i
                    max2 = j

    if ((profits[max1]+profits[max2]) > profits[max]):
        return (minx[max1], max1, profits[max1]), (minx[max2], max2, profits[max2])
    else: 
        return (minx[max], max, profits[max])

sample = [ 120, 130, 140, 145, 135, 125, 115, 155]
print(bestBuy(sample))  

