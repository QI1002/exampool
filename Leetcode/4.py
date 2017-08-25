
#4. Median of Two Sorted Arrays

def findMedian(sort1, sort2):
    count1 = len(sort1)
    count2 = len(sort2)
    max1 = sort1[count1-1]
    max2 = sort2[count2-1]
    max = max1 if (max1 > max2) else max2
    sort1.append(max+1)
    sort2.append(max+1)
    
    i = j = 0
    m1 = (count1+count2)//2
    m0 = m1-1 if (((count1+count2) & 1) == 0) else m1
    #print((m0,m1))
    for k in range(m1+1):
        left = sort1[i]
        right = sort2[j]
        if (left < right):
            i += 1
            v = left
        else:
            j += 1
            v = right
   
        if (k == m0): 
            v0 = v    
            
        if (k == m1): 
            v1 = v
            break
           
    if (m1 == m0): return v1 
    else: return (v0, v1)
      
      
data1 = [2,4,6]
data2 = [1,2,3,5,7]      
print(findMedian(data1, data2))                   
        
      