
# 42. Trapping Rain Water

def findPeak(data):

    count = len(data)
    m = flag = 0
    peak = []
    for i in range(1, count, 1):
        m = 0
        if (data[i] < data[i-1]): m = -1
        if (data[i] > data[i-1]): m = 1
        
        if (flag == 0 and m == -1):
            peak.append(i-1)
            flag = 1

        if (flag == 1 and m == 1):
            flag = 0

    if (flag == 0 and m == 1):
        peak.append(i)

    return peak

def findVolume(data):
    peaks = findPeak(data)
    print(peaks)
    count = len(peaks)
    vol = 0
    for i in range(1, count, 1):
        a = data[peaks[i-1]]
        b = data[peaks[i]]
        min = b if (a > b) else a
        for j in range(peaks[i-1]+1, peaks[i], 1):
           vol += (min - data[j])
    return vol
        
sample0 = [0,1,0,2,1,0,1,3,2,1,2,1,2]
print(findVolume(sample0))
sample1 = [1,0,1,0,1]
print(findVolume(sample1))
          
          
