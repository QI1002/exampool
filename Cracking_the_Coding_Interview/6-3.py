import copy
  
class Jug:

    def empty(self):
        self.volume = 0 
    
    def full(self): 
        self.volume = self.capacity
        
    def __init__(self, capacity):
        self.capacity = capacity
        self.empty()
        
    def __init__(self, capacity, volume):
        self.capacity = capacity
        self.volume = volume       
        
    def setfrom(self, source): 
        if (source.volume + self.volume > self.capacity):
            source.volume = source.volume - (self.capacity - self.volume)
            self.volume = self.capacity
        else:
            source.volume = 0
            self.volume += source.volume

def print_results(results):
    print_str = "";
    for x in results:
       print_str += "[" + str(x[0].volume) + "," + str(x[1].volume) + "]"
    return print_str
                
def empty_a(a, b):
    a.empty()
    
def empty_b(a, b):
    b.empty()
    
def full_a(a, b):
    a.full()
    
def full_b(a, b):
    b.full()

def move_a2b(a,b):
    a.setfrom(b)    
    
def move_b2a(a,b):
    b.setfrom(a)    
    
def do_actions(id, a, b):
    if (id >= len(actions)):
        raise IndexError
    actions[id](a,b)
    
a = Jug(5)
b = Jug(3)        

actions = [empty_a, empty_b, full_a, full_b, move_a2b, move_b2a]
actions_desc = ["empty 5 quart jug", "empty 3 quart jug", "full 5 quart jug", "full 3 quart jug", "move 5 quart jug to 3 quart jug", "move 3 quart jug to 5 quart jug"]
possible_result = []
possible_flow = []
answer = 4;

result = [a,b]
flow = []

values = set()
results = []
flows = []

values.add(result[0].volume)
values.add(result[1].volume)
results.append(result)
flows.append(flow)

maxloop = 4
loop = 0
    
while(maxloop == 0 or loop < maxloop):

    for i in range(len(results)):
        for j in range(len(actions)):
            result = [copy.copy(results[i][0]), copy.copy(results[i][1])]
            do_actions(j, result[0], result[1])
            bool1 = result[0].volume in values
            bool2 = result[1].volume in values
            print("result = {0},{1}".format(result[0].volume, result[1].volume))
            if (bool1 == False) or (bool2 == False):
                results.append(result)
                if (bool1 == False): values.add(result[0].volume)
                if (bool2 == False): values.add(result[1].volume)
            
            if (answer in values):
                print("Found {0} by following steps:".format(answer))
                exit(0)    

        print("results = {0}".format(print_results(results)))        

    print("loop {0} =============".format(loop))        
    loop = loop + 1
    



