
#732. My Calendar III

class bookK:
    def __init__(self):
        self.segslist = [ [] ]

    def overlay(self, a, b):
        if (a[0] <= b[0] and b[0] < a[1]):
            if (b[1] <= a[1]): return b 
            else: return (b[0], a[1])
        if (b[0] <= a[0] and a[0] < b[1]):
            if (a[1] <= b[1]): return a 
            else: return (a[0], b[1])
        return None

    def book(self, s):
        count = len(self.segslist)
        for i in range(count-1,-1,-1):
            for x in self.segslist[i]:
                t = self.overlay(x, s)
                #print((t,x,s))
                if (t == None): continue
                if (len(self.segslist) == (i+1)):
                    self.segslist.append([])
                self.segslist[i+1].append(t)
 
        self.segslist[0].append(s)
        #print(self.segslist)
        return len(self.segslist)

bk = bookK()
print(bk.book((10,20)))
print(bk.book((50,60)))
print(bk.book((10,40)))
print(bk.book((5,15)))
print(bk.book((5,10)))
print(bk.book((25,55)))

