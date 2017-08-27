
class ChainHash:
   def __init__(self, cap = 7):
       self.cap = cap
       self.chains = [ [] for i in range(cap) ]
       
   def gethash(self, key):
       return key % self.cap
           
   def put(self, key, value, notDup = True):
       slot = self.gethash(key)
       c = self.chains[slot]
       if (notDup and self.lookup(key) == None):
           c.append((key, value))
           return True
           
       return False     
   
   def lookup(self, key):
       slot = self.gethash(key)
       c = self.chains[slot]
       for i in range(len(c)):
           if (c[i][0] == key):
               return c[i][1]
       return None
    
class LinearHash:
   def __init__(self, cap = 23, hash2 = False):
       self.cap = cap
       self.hash2 = hash2
       self.chains = [ None for i in range(cap) ]
       
   def gethash(self, key):
       return key % self.cap

   def gethash2(self, key):
       if (self.hash2):
           return 8 - (self.gethash(key) % 8)
       
       return 1
                  
   def put(self, key, value, notDup = False):
   
       if (notDup and self.lookup(key) == None):
           return False
   
       i = slot = self.gethash(key)
       while(self.chains[i] != None):
           i = (i+self.gethash2(key)) % self.cap
           if (slot == i): break
                  
       if (self.chains[i] != None):
           return False
       else:    
           self.chains[i] = (key, value)                          
           return True
   
   def lookup(self, key):
       i = slot = self.gethash(key)
       while(self.chains[i] != None):
           if (self.chains[i][0] == key):
               return self.chains[i][1]               
           i = (i+1) % self.cap
           if (slot == i): break
           
       return None

              
template = [
("a", "a1"),
("d", "d1"),
("e", "e1"),
("f", "f1"),
("l", "l1"),
("m", "m1"),
("n", "n1"),
("r", "r1"),
("s", "s1"),
("t", "t1"),
("w", "w1"),       
("y", "y1"),       
("z", "z1"),       
("B", "B1"),
("f", "f2"),
]


#myHashClass = ChainHash 
myHashClass = LinearHash
myHash = myHashClass()
for v in template:
    c = ord(v[0][0])
    myHash.put(c, v[1])

for v in template: 
    c = ord(v[0][0])
    print("map {0} to get {1}".format(v[0], myHash.lookup(c)))    

v = "D"
print("map {0} to get {1}".format(v, myHash.lookup(ord(v[0]))))