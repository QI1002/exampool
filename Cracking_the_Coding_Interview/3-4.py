
class stack:
    def __init__(self, name):
        self.body = []
        self.name = name

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def haoniTower(tower, n):
    for i in range(n,0,-1):
        tower.push(i)

step = 0
stackA = stack("A")
stackB = stack("B")
stackC = stack("C")

def checkTower(tower):
    if (len(tower.body) <= 1):
        return

    for i in range(len(tower.body)-1):
        if (tower.body[i] <= tower.body[i+1]):
            raise ValueError

def printStacks():
    print("stack A:{0} B:{1} C:{2}".format(stackA.body, stackB.body, stackC.body))
    checkTower(stackA)
    checkTower(stackB)
    checkTower(stackC)

def printStep(v, stack0, stack1):
    global step
    step += 1
    print("{0}:move {1} from {2} to {3}".format(step, v, stack0.name, stack1.name))

def moveHaoniTower(n, stack0, stack1, stack2):
    if (n == 1):
        v = stack0.pop()
        stack1.push(v)
        printStep(v, stack0, stack1)
        printStacks()
    else:
        moveHaoniTower(n-1, stack0, stack2, stack1)
        v = stack0.pop()
        stack1.push(v)
        printStep(v, stack0, stack1)
        printStacks()
        moveHaoniTower(n-1, stack2, stack1, stack0)

def moveHaoniTower2(n, stack0, stack1, stack2):
    if (n == 0):
        return

    moveHaoniTower2(n-1, stack0, stack2, stack1)
    v = stack0.pop()
    stack1.push(v)
    printStep(v, stack0, stack1)
    printStacks()
    moveHaoniTower2(n-1, stack2, stack1, stack0)

number = 4
haoniTower(stackA, number)
printStacks()
moveHaoniTower2(number, stackA, stackB, stackC)

