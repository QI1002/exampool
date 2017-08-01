
def swap(l,i,j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    
def bubble_sort(ll):

    for j in range(0,len(ll),1):
        min = j
        for i in range(j+1,len(ll),1):
            if (ll[min] > ll[i]):
                min = i
        swap(ll,min,j)    
        
    return ll    
    
def quick_sort_better(ll):
    ll.insert(0, -1)
    quick_sort2(ll, 1, len(ll)-1)
    return ll[1:]
        
def quick_sort2(ll, l, r):
    if (l < r):
        print("({0},{1}) with {2}".format(l,r,ll))
        v = ll[r]
        i = l
        j = r-1
        while(True):
            while(ll[i] < v): i += 1
            while(ll[j] > v): j -= 1
            if (i >= j): break
            swap(ll, i, j)
                        
        swap(ll, i, r)
        quick_sort2(ll, l, i-1)
        quick_sort2(ll, i+1, r)
     
def quick_sort(ll):
    if (len(ll) <= 1):
        return ll
    else:
       anchor = ll[-1:][0]
       less = []
       more = []
       for i in range(len(ll)-1):
           if (ll[i] < anchor):
               less.append(ll[i])
           else:    
               more.append(ll[i])
               
       if (len(less) < len(more)):
           less.append(anchor)
       else:
           more.append(anchor)

       ll = list(less)
       ll.extend(more)
           
       print(str(less) + "_" + str(more) + "_" + str(ll))
       less = quick_sort(ll[0:len(less)])
       more = quick_sort(ll[len(less):])
       
       ll = list(less)
       ll.extend(more)
       
       return ll
             
def merge_sort(ll):
    if (len(ll) <= 1):
        return ll    
    else:
        hlen = len(ll)//2
        a = merge_sort(ll[0:hlen])
        b = merge_sort(ll[hlen:])
        max = a[-1:][0]
        max = b[-1:][0]+1 if b[-1:][0] > max else max+1
        a.append(max)
        b.append(max)
        
        ai = 0 
        bi = 0
        for i in range(len(ll)):
            if (a[ai] < b[bi]):
                ll[i] = a[ai]
                ai += 1
            else:
                ll[i] = b[bi]
                bi += 1    
        return ll
            
my_sort = quick_sort_better     
print(my_sort([3,5,2,4,1]))
print(my_sort([4,2,1,3,5]))