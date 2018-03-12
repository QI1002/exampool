
class Employee(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def getRank(self):
        return None
        #return self.rank        
        #raise ValueError("not support in base class")

class Fresher(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        self.rank = 0
    def getRank(self):
        return self.rank        

class Engineer(Employee):
    def __init__(self, name):
        super(Engineer,self).__init__(name)
        self.rank = 1

e0 = Employee("Zero")
e1 = Fresher("One")
e2 = Engineer("Two")

print((e0.getName(), e0.getRank()))
print((e1.getName(), e1.getRank()))
print((e2.getName(), e2.getRank()))
