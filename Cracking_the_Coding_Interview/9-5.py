
template1 = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
template2 = ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""]
	
def search(ll, l, r, v):
    while((l+1) < r):
        m = (l + r)//2
        vv = ll[m]
        if (vv == v):
            return m       
        if (vv < v):
            l = m
        else:
            r = m
         
    vv = ll[l]
    if (v == vv):
        return l
    
    vv = ll[r]
    if (v == vv):
        return r
                         
    return None

       
def search_remap(ll, v): 
    compact = []
    remap = []
    for i in range(len(ll)):
        if (ll[i] == ""):
            continue
        compact.append(ll[i])
        remap.append(i)      
        
    #print(compact)
    
    result = search(compact, 0, len(compact)-1, v)
    if (result == None):
        return result
          
    return remap[result]

for i in template1:
    print("search {0} in {1} = {2}".format(i, template1, search_remap(template1, i)))    
print("=============================================================================================")
for i in template2:
    print("search {0} in {1} = {2}".format(i, template2, search_remap(template2, i)))    

i = "ballcar"
print("search {0} in {1} = {2}".format(i, template2, search_remap(template2, i))) 