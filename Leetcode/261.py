
#261. Graph Valid Tree 

def validGraph(n, edges):
    root = None
    depth = [ None for i in range(n) ]
    for a,b in edges:
        if (depth[a] == None):
            if (root == None):
                root = a
            else:
                return False

            depth[a] = 0

        if (depth[b] == None):            
            depth[b] = depth[a]+1
        else:
            return False

    return True

n, edges = 5, [[0,1],[0,2],[0,3],[1,4]]
print("{0}:{1}".format((n,edges), validGraph(n, edges)))
n, edges = 5, [[0,1],[1,2],[2,3],[1,3],[1,4]]
print("{0}:{1}".format((n,edges), validGraph(n, edges))) 
