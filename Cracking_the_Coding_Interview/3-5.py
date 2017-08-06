
class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

class queue:
    def __init__(self):
        self.stackA = stack()
        self.stackB = stack()

    def put(self, data):
        self.stackA.push(data)

    def get(self):
        if (self.stackA.isEmpty()):
            return None

        while(not self.stackA.isEmpty()):
            v = self.stackA.pop()
            self.stackB.push(v)

        result = self.stackB.pop()
        while(not self.stackB.isEmpty()):
            v = self.stackB.pop()
            self.stackA.push(v)

        return result

values = [ 3, 5, 2, 1, 4 ]
myqueue = queue()
for i in range(len(values)):
    myqueue.put(values[i])
    print("after put {0}".format(values[i]))

for i in range(len(values)):
    v = myqueue.get()
    print("after get {0}".format(v))

