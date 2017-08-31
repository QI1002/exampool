
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

    def peek(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body[len(self.body)-1]

    def isEmpty(self):
        return True if len(self.body) == 0 else False


class extraStack:
    def __init__(self):
        self.body = []

    def push(self, data):
        minValue = self.min()
        if (minValue == None or data < minValue):
            minValue = data
        self.body.append((data, minValue))

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()[0]

    def min(self):
        if (len(self.body) == 0):
            return None
        else:
            v = self.body.pop()
            self.body.append(v)
            return v[1]

class extraStackNew:
    def __init__(self):
        self.body = []
        self.minstack = stack()

    def push(self, data):
        minValue = self.min()
        if (minValue == None or data <= minValue):
            minValue = data
            self.minstack.push(minValue)
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            minValue = self.min()
            v = self.body.pop()
            if (minValue == v):
                self.minstack.pop()
            return v

    def min(self):
        if (self.minstack.isEmpty()):
            return None
        else:
            return self.minstack.peek()

values = [ 3, 5, 2, 1, 4 ]
minstack = extraStackNew()
#minstack = extraStack()
for i in range(len(values)):
    minstack.push(values[i])
    print("after push {0}, the min value = {1}".format(values[i], minstack.min()))

for i in range(len(values)):
    v = minstack.pop()
    print("after pop {0}, the min value = {1}".format(v, minstack.min()))


