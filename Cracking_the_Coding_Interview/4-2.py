
class multitree:
    def __init__(self, data):
        self.data = data
        self.childs = []

    def addchild(self, child):
        if (not child in self.childs):
            self.childs.append(child)
            
def checkPath(start, links, points):
    count = len(links)
    treeFrom = []
    treeset = []
    result = []
    slevel = [ start ]
    elevel = []
    depthset = []
    depth = 0
    cycle = False
    
    for i in range(points):
        depthset.append(0xFF)
        treeFrom.append(i)
        treeset.append(multitree(i))
        
    depthset[start] = depth
    while(len(slevel) != 0):  
        print(slevel) 
        for i in range(count):
           slink = links[i][0]
           elink = links[i][1]
           if (slink in slevel):
               if (treeFrom[elink] == elink): 
                   treeFrom[elink] = slink
                   depthset[elink] = depth + 1
                   treeset[slink].addchild(elink)
                   elevel.append(elink)
               if (depthset[elink] < depthset[slink]):
                   print(slink)
                   print(elink)
                   ancestor = slink
                   while(True):
                       ancestor = treeFrom[ancestor]
                       if (ancestor == elink):
                           cycle = True
                           break
                       if (ancestor == start):
                           break
        slevel = elevel
        elevel = []
        depth += 1
           
    for i in range(points):
        if (treeFrom[i] != i): 
            result.append(i)
    result.append(start)        

    return result, cycle

def checkCycle(links, points):    
    unmark = []
    for i in range(points):
        unmark.append(i)
        
    while(len(unmark) != 0):
        print(unmark)
        result, cycle = checkPath(unmark[0], links, points)
        if (cycle): return True
        for j in range(len(result)):
            unmark.remove(result[j])
          
    return False       
    
links1 = [ (4,3), (5,4), (5,7), (4,7), (4,6), (3,6), (1,4), (1,3), (1,2), (2,4), (2,5), (7,6) ]
#links1 = [ (4,3), (5,4), (7,5), (4,7), (4,6), (3,6), (1,4), (1,3), (1,2), (2,4), (2,5), (7,6) ]
start1 = 2
end1 = 3
points1 = 8
result = checkPath(start1, links1, points1)[0]
print(result)
print("the path from {0} to {1} is {2}".format(start1, end1, end1 in result))
print("the result that there is cycle is {0}".format(checkCycle(links1, points1)))