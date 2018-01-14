
#715. Range Module

class QR:
  
    def __init__(self):
        self.segs = []

    def addseg(self, a, b):
        if (a[0] <= b[0] and a[1] > b[0]):
            if (b[1] <= a[1]): return a
            else: return (a[0], b[1])
        if (b[0] <= a[0] and b[1] > a[0]):
            if (a[1] <= b[1]): return b
            else: return (b[0], a[1])
        return None

    def add(self, s):
        newsegs = []
        notOverlay = -1
        for x in self.segs:
            t = self.addseg(x, s) 
            if (t == None):
                if (x[0] >= s[1] and notOverlay == -1):
                    notOverlay = 1
                    newsegs.append(s)
                newsegs.append(x)
            else: 
                newsegs.append(t)
                notOverlay = 0
 
        if (notOverlay != 1): newsegs.append(s)
        #print((newsegs, self.segs))
        self.segs = [ newsegs[0] ] 
        for i in range(1, len(newsegs), 1):
            p = self.segs.pop()
            n = newsegs[i]
            if (p[1] == n[0]):
                self.segs.append((p[0],n[1]))
            else:
                self.segs.extend([p, n])
                      
    def removeseg(self, a, b):
        if (a[0] <= b[0] and a[1] > b[0]):            
            if (b[1] <= a[1]):
                 t = []
                 if (a[0] != b[0]): t.append((a[0], b[0]))
                 if (a[1] != b[1]): t.append((b[1], a[1]))
                 return t 
            else: 
                 return [(a[0], b[0])]
        if (b[0] <= a[0] and b[1] > a[0]):
            if (a[1] <= b[1]): return []
            else: return (b[1], a[1])
        return None
 
    def remove(self, s):
        newsegs = []
        for x in self.segs:
            t = self.removeseg(x, s) 
            if (t == None): newsegs.append(x)
            else: newsegs.extend(t)
 
        self.segs = newsegs 

    def include(sef, a, b):
        if (a[0] <= b[0] and a[1] > b[0]):
            if (b[1] <= a[1]): return True
        return False

    def query(self, s):
        for x in self.segs:
            if (self.include(x, s)):
                return True

        return False  

r = QR()
r.add((1,3))
#r.add((3,8))
r.add((8,11))
#r.add((3,8))
r.remove((3,8))
print(r.segs)

r = QR()
r.add((10,20))
r.remove((14,16))
print(r.segs)
s = (10,14)
print("query range {0} is {1}", s, r.query(s))
s = (13,15)
print("query range {0} is {1}", s, r.query(s))
s = (16,17)
print("query range {0} is {1}", s, r.query(s))

 
