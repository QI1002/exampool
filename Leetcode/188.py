
#188. Best Tune to Buy and Sell Stock IV

def getExtra(data):
    state = [ 0 for i in range(len(data)) ]    
    prev = 0
    for i in range(1, len(data), 1):
        if (data[i-1] == data[i]):
            state[i] = prev
        else:
            state[i] = 1 if (data[i-1] < data[i]) else -1
            prev = state[i] 
    
    if (state[0] == 0):
        prev = 0
        for i in range(len(data)-1, -1, -1):
            if (state[i] == 0): state[i] = prev * -1
            else: prev = state[i]
        if (state[0] == 0):
            state = [ 1 for i in range(len(data)) ]                     

    #print(state)    
    extra = []
    minmax = -1
    for i in range(len(data)):
        if (minmax == -1):  
            minmax = data[i]
        else:            
            if (state[i] == 1): 
                if (data[i] > minmax): minmax = data[i]
            else: 
                if (data[i] < minmax): minmax = data[i]           
        
        if ((i+1) == len(data) or state[i+1] != state[i]):
            extra.append(minmax)
            minmax = -1
                
    return extra
    
def bestBuy(data):

    extra = getExtra(data)
    profit = 0    
    for i in range(1, len(extra), 1):
        if (extra[i-1] < extra[i]):
            profit += (extra[i] - extra[i-1]) 
        
    return extra, profit
    
def bestBuyK(data, k = 3):

    extra = getExtra(data)
    profit = 0
    profits = []    
    for i in range(1, len(extra), 1):
        if (extra[i-1] < extra[i]):
            profits.append(extra[i] - extra[i-1]) 
    
    profits = sorted(profits)
    profits = profits[::-1]
    if (k > len(profits)): k = len(profits)
    for i in range(k): profit += profits[i]
                
    return profit
    
stockprice = [ 2,2,2,2,1,1 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 1,1,2,2,2,2 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 1,1,2,2,2,2,1,1 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [2,2,2,2]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 1,1,1,1,2,2 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 2,2,1,1,1,1 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 2,2,1,1,1,1,2,2 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))

stockprice = [ 1,2,3,4,2,1 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 1,2,4,3,2,1 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))

stockprice = [ 4,3,2,1,2,3 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 3,2,1,2,3,4 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))
stockprice = [ 3,2,1,2,3,4,1,2,3 ]
print("{0}=>{1}".format(stockprice, bestBuyK(stockprice)))