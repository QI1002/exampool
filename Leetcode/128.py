

#128. Longest Consecutive Sequence

def findSeq(data):
    union = {}
    count = len(data)
    maxSeq = []    
    for i in range(count):
        self = data[i]
        if (not self in union):
            union[self] = [self]
            
        minus = self - 1    
        if (minus in union):
            union[self].extend(union[minus])
            
        plus = self + 1    
        if (plus in union):
            union[self].extend(union[plus])
         
        for c in union[self]:
            union[c] = union[self]
                                       
    for key in union:
        if (len(maxSeq) < len(union[key])):
            maxSeq = union[key]
    
    #print(union)
    return maxSeq
    
print(findSeq([5, 100, 4, 200, 1, 3, 2, 0]))                