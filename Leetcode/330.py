
#330. Patching Array

def patch(data, n):
    tm = sorted(data)
    r = []
    m = n
    tl = []
    
    if (len(tm) > 0 and tm[0] == 1):
        tl.append(tm[0])
        tm.pop(0)
        while(len(tm) > 0 and tm[0] <= (2* tl[-1])):
            tl.append(tm.pop(0))                 
    
    ss = sum(tl)
    
    while(len(tm) != 0):    
        max = tm.pop()
        m -= max
     
    #print((m, ss, tl, tm)) 
    while(m > ss):
        h = (m+1) // 2
        r.append(h)
        m -= h

    return r
    
nums, n = [1,3], 6
print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            

nums, n = [1,5,10], 20
print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            

nums, n = [1,2,2], 5
print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            

 
for n in range(1,8,1):
    nums = []
    print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            
    nums = [1]
    print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            
    nums = [1,2]
    print("{0}, {1} => {2}".format(nums, n, patch(nums, n)))            
           
