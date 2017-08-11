
template = [15,16,19,20,25,1,3,4,5,7,10,12]
	
def getdata(ll, index, bias):
    index += bias
    if (index >= len(ll)):
        index -= len(ll)
    return ll[index]    

def search(ll, l, r, bias, v, exact = False):
    while((l+1) < r):
        m = (l + r)//2
        vv = getdata(ll, m, bias)
        if (vv == v):
            return m       
        if (vv < v):
            l = m
        else:
            r = m
         
    vv = getdata(ll, l, bias)            
    if (v == vv):
        return l
    
    vv = getdata(ll, r, bias)    
    if (v == vv):
        return r
                         
    if (exact):
        return None
             
    vv = getdata(ll, l, bias)            
    if (v < vv):
        return l
    
    vv = getdata(ll, r, bias)    
    if (v > vv):
        return r+1
    else:
        return r
       
def search_bias(ll, v, exact = False): 
    bias = 0
    for i in range(len(ll)-1):
        if (ll[i] > ll[i+1]):
            bias = i+1
    result = search(ll, 0, len(ll)-1, bias, v, exact)
    if (result == None):
        return result
          
    result += bias
    if (result >= len(ll)):
        result -= len(ll)
    return result        

print("search {0} in {1} = {2}".format(18, template, search_bias(template, 18)))
print("search {0} in {1} = {2}".format(30, template, search_bias(template, 30)))
print("search {0} in {1} = {2}".format(0, template, search_bias(template, 0)))
print("search {0} in {1} = {2}".format(13, template, search_bias(template, 13)))

print("===============================")
for i in template:
    print("search {0} in {1} = {2}".format(i, template, search_bias(template, i, True)))    
