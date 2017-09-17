
#84. Largest Rectangle in Histogram

def largestRect(data):
    s = sorted(data)
    maxRect = (0, len(data)-1), s[0]
    maxArea = len(data) * s[0]
     
    for i in range(1, len(s), 1):
        start = -1
        for j in range(len(data)):
            if (data[j] >= s[i]):    
                if (start == -1):
                    start = j
            else:
                if (start != -1):
                    area = (j - start)*s[i]
                    if (area > maxArea):
                        maxArea = area
                        maxRect = (start, j-1), s[i]  
                start = -1                       
    
        if (start != -1):
            area = (len(data)-start)*s[i]
            if (area > maxArea):
                maxArea = area
                maxRect = (start, len(data)-1), s[i]

    return maxRect 
     
sample = [2, 1, 5, 6, 2, 3]

t = largestRect(sample)
print(t)