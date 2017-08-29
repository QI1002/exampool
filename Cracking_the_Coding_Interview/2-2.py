
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

def findTailKNew(head, k):
    p1 = p2 = head
    for j in range(k+1):
        if (p2 == 0): return 0
        p2 = p2.next

    while (p2 != 0):
        p2 = p2.next
        p1 = p1.next

    return p1

#method = findTailK
method = findTailKNew

values = [ 3, 5, 2, 1, 4 ]
linkhead = linklist(values)
printlist(linkhead)
print("====================")
for i in range(10):
    khead = method(linkhead, i)
    print("the tail index {0} = {1}".format(i, "NULL" if khead == 0 else khead.data))

