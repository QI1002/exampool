

template = ["William Shakespeare", "dormitory", "I am a weakish speller", "Madam Curie", "dirtry room", "Radium came"]

def getStatistics(string):
    result = []
    for i in range(26):
        result.append(0)
    for i in range(len(string)):
        c = string[i]
        if (c >= 'A' and c <= 'Z'): result[ord(c)-ord('A')] += 1
        if (c >= 'a' and c <= 'z'): result[ord(c)-ord('a')] += 1
    return result
   
def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

# 1 means st[i]>st[j] otherwise 0    
def compare(st, i, j):
    for k in range(len(st[i])):
        if (st[i][k]<st[j][k]): return 0
        if (st[i][k]>st[j][k]): return 1
    return 0
       
def anagram_sort(ll, st):
    for i in range(len(ll)):
        min = i
        for j in range(i+1,len(ll),1):
            if (compare(st, min, j) == 1):
                min = j
        #print(str(min) + " " +str(i))        
        swap(st, min, i)
        swap(ll, min, i)            
               
def anagram(ll):
    st = []
    for i in range(len(ll)):
        st.append(getStatistics(ll[i]))
    print(st)    
    anagram_sort(ll, st)
    
tt = list(template)
anagram(template)    
print("anagram sort of {0} = {1}".format(tt, template))          