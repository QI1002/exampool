
#25. Reverse Nodes in k-Group
#I1: condition in reverseK shall use "and" but not "or"

class Node:
    def __init__(self, v, n = 0):
        self.v = v
        self.n = n
        
def getList(data):
    head = 0
    for i in range(len(data)-1, -1, -1):
        n = Node(data[i], head)
        head = n
        
    return head
    
def printList(head):
    result = []
    while(head != 0):
        result.append(head.v) 
        head = head.n
    return result
    
def reverseK(target, k):
    head = target
    reverse = 0
    while(head != 0 and k != 0):        
        r = reverse
        reverse = head
        head = head.n
        reverse.n = r
        if (r == 0): rr = reverse
        k -= 1
    
    rr.n = head
    return reverse
                
head = getList(list(range(1,6,1)))
rev = reverseK(head, 3)
print(printList(rev))
