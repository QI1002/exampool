

class stack:
    def __init__(self, array, start, end):
        self.array = array
        self.start = start
        self.top = start-1
        self.end = end

    def push(self,data):
        if (self.top >= self.end):
            return False
        else:
            self.top += 1
            self.array[self.top] = data
            return True

    def pop(self):
        if (self.isEmpty()):
            return None
        else:
            index = self.top
            self.top -= 1
            return self.array[index]

    def isEmpty(self):
        return (self.top < self.start)

class stackSet:
    def __init__(self, array, parts = 3):
        self.array = array
        self.occupy = 0
        self.parts = parts
        self.index = [ [] for i in range(parts) ]
        self.idset = []

    def foundEmpty(self):
        for i in range(len(self.array)):
            occupy = False
            for j in range(self.parts):
                if (i in self.index[j]):
                    occupy = True
                    break
            if (occupy == False):
                return i
        return None

    def put(self, p, data):
        if self.occupy >= len(self.array):
            return

        slot = self.foundEmpty()
        self.array[slot] = data
        self.index[p].append(slot)
        self.occupy += 1

    def get(self, p):
        if (self.isEmpty(p)):
            return None
        else:
            slot = self.index[p].pop()
            self.occupy -= 1
            return self.array[slot]

    def isEmpty(self, p):
        return (len(self.index[p]) == 0)

class stackNew:
    def __init__(self, stackset, id):
        self.stackset = stackset
        if (not id in stackset.idset):
            self.id = id
            stackset.idset.append(id)

    def push(self, data):
        self.stackset.put(self.id, data)

    def pop(self):
        return self.stackset.get(self.id)

    def isEmpty(self):
        return self.stackset.isEmpty(self.id)

arraylist = []
for i in range(30):
    arraylist.append(0)

stackClass = stack
stackClass = stackNew
if stackClass == stackNew:
    sset = stackSet(arraylist, 3)
    stack0 = stackClass(sset, 0)
    stack1 = stackClass(sset, 1)
    stack2 = stackClass(sset, 2)
else:
    stack0 = stackClass(arraylist, 0, 9)
    stack1 = stackClass(arraylist, 10, 19)
    stack2 = stackClass(arraylist, 20, 29)

for i in range(12):
    stack0.push(i)
    stack1.push(i+20)
    stack2.push(i+40)

for i in range(11):
    print(stack0.pop())
    print(stack1.pop())
    print(stack2.pop())
