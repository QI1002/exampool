

# 382. Linked List Random Node

import random 

class Node:
    def __init__(self, data = 0, step = 0):
        self.data = data
        self.next = step
        

def getListLength(head):
    count = 0
    while(head != 0):
        head = head.next
        count += 1
        
    return count    
        
def toList(head):
    result = []
    count = 0
    while(head != 0):
        result.append(head.data)
        head = head.next
        
    return result
    
def generateList(data):
    head = 0
    while(len(data) > 0):        
        node = Node(data.pop(), head)
        head = node
        
    return head
    
def getRandom(target):
    count = getListLength(target)
    index = random.randint(0, count-1)
    for i in range(index):
        target = target.next
    
    return target.data      
    
root =  generateList(list("4176"))
print(toList(root))
print(getRandom(root))             