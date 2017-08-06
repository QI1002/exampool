

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

def attachTail(head, tail):
    prev = n = head
    while(n != 0):
        prev = n
        n = prev.next
    prev.next = tail

def findFirstCycle(head):
    n = head
    result = []
    while(n != 0):
        if (n in result):
            return n
        result.append(n)
        n = n.next
    return 0

def isCycle(head):
    n2 = n1 = head
    while(n1 != 0 and n2 != 0):
        n1 = n1.next
        n2 = n2.next
        n2 = 0 if n2 == 0 else n2.next
        if (n2 != 0 and n1 == n2):
            return n1
    return 0

values = [ 1, 2, 3, 4, 5, 6, 7 ]
for i in range(len(values)):
    linkhead = linklist(values)
    printlist(linkhead)
    print("====================")
    index = i
    khead = findTailK(linkhead, index)
    print("the tail index {0} = {1}".format(index, "NULL" if khead == 0 else khead.data))
    print("====================")
    #khead = 0
    attachTail(linkhead, khead)
    cyclehead = isCycle(linkhead)
    print("the cycle node = {0}".format("NULL" if cyclehead == 0 else cyclehead.data))
    cyclehead = findFirstCycle(linkhead)
    print("the first cycle node = {0}".format("NULL" if cyclehead == 0 else cyclehead.data))
    print("====================")
