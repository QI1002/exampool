

import random

class node:
    def __init__(self, data, next = 0):
        self.data = data
        self.next = next

def genlist(n, min = 1, max = 10):
    result = []
    for i in range(n):
        c = random.randint(min, max)
        result.append(c)
    return result

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

def removeDuplicate(head):
    n1 = head
    while(n1 != 0):
        v = n1.data
        n2 = n1.next
        prev = n1
        while(n2 != 0):
            if (n2.data == v):
                prev.next = n2.next
            else:
                prev = n2
            n2 = prev.next
        n1 = n1.next

    return head

def removeDuplicateNew(head):
    n = head
    values = []
    while(n != 0):
        if (not n.data in values):
            values.append(n.data)
            prev = n
        else:
            prev.next = n.next

        n = n.next

    return head

#method = removeDuplicate
method = removeDuplicateNew

#values = [ 2, 2, 2, 3, 5, 2, 1, 4, 5, 2 ]
values = genlist(10, 1, 5)
linkhead = linklist(values)
printlist(linkhead)
print("====================")
newhead = method(linkhead)
printlist(newhead)
