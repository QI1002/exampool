
class node:
    def __init__(self, data, next = 0):
        self.data = data
        self.next = next

def numTolist(a):
    result = []
    while(a != 0):
        result.append(a % 10)
        a = a // 10
    return result

def printlist(head):
    n = head
    while(n != 0):
        print(n.data)
        n = n.next
        
def linklist(ll):
    ll = ll[::-1]
    count = len(ll)
    head = 0
    for i in range(count):
        n = node(ll[i], head)
        head = n
    return head

def sumList(numlist1, numlist2):
    n1 = numlist1
    n2 = numlist2
    result = []

    carrier = 0
    while(n1 != 0 or n2 != 0):
        value1 = 0 if n1 == 0 else n1.data
        value2 = 0 if n2 == 0 else n2.data
        if (n1 != 0): n1 = n1.next
        if (n2 != 0): n2 = n2.next
        value = value1 + value2 + carrier
        if (value >= 10):
            result.append(value - 10)
            carrier = 1
        else:
            result.append(value)
            carrier = 0

    return linklist(result)

numlist1 = linklist(numTolist(514))
numlist2 = linklist(numTolist(1295))
printlist(sumList(numlist1, numlist2))