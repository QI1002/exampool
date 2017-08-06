
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
         
def removeDuplicate(head):
    n1 = head
    while(n1 != 0):
        v = n1.data
        n2 = n1.next
        prev = n1
        while(n2 != 0):
            if (n2.data == v):
                deletelistbyPrev(prev)
            else:     
                prev = n2    
            n2 = prev.next
        n1 = n1.next
    return head    
        
values = [ 2, 3, 5, 2, 1, 4, 5, 2 ]
linkhead = linklist(values)
printlist(linkhead)
print("====================")
newhead = removeDuplicate(linkhead)
printlist(newhead)