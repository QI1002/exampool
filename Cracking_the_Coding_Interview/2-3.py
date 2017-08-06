
class node:
    def __init__(self, data, next = 0):
        self.data = data
        self.next = next

def linklist(ll):
    ll = ll[::-1]
    count = len(ll)
    head = 0
    for i in range(count):
        n = node(ll[i], head)
        head = n
    return head

def printlist(head):
    n = head
    while(n != 0):
        print(n.data)
        n = n.next

def deletelistbyPrev(prev):
    if (prev.next != 0):
        prev.next = prev.next.next

def deletelistbyNode(head, node):
    prev = n = head
    while(n != 0):
        if (n == node):
            if (head == node):
                head = head.next
            else:
                deletelistbyPrev(prev)     
        prev = n
        n = prev.next
    return head
    
def countlist(head):
    count = 0
    n = head
    while(n != 0):
        count += 1
        n = n.next
    return count
    
# head => 2 => 3 => 0 , so index 0 => 2 , index 1 => 3           
def findHeadK(head, k):
    count = 0
    n = head
    while(n != 0):
        if (count == k):
            return n
        count += 1
        n = n.next
    return 0
     
def findTailK(head, k):
    count = countlist(head)
    if (k >= count):
        return 0
    else:
        return findHeadK(head, count-1-k)    
    
values = [ 3, 5, 2, 1, 4 ]
linkhead = linklist(values)
printlist(linkhead)
print("====================")
index = 1
khead = findTailK(linkhead, index)
print("the tail index {0} = {1}".format(index, "NULL" if khead == 0 else khead.data))        
print("====================")
linkhead = deletelistbyNode(linkhead, 0)
printlist(linkhead)
print("====================")
linkhead = deletelistbyNode(linkhead, khead)
printlist(linkhead)
print("====================")
index = 0
khead = findHeadK(linkhead, index)
print("the head index {0} = {1}".format(index, "NULL" if khead == 0 else khead.data))        
print("====================")
linkhead = deletelistbyNode(linkhead, khead) 
printlist(linkhead)
