import copy
  
#add the code to evaluate performance speed up
#by argv and enlarge Jugs #  
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
            self.volume += source.volume
            source.volume = 0

def print_results(results):
    print_str = "";
    for x in results:
       print_str += "[" + str(x[0]) + "," + str(x[1]) + "]"
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
    b.setfrom(a)    
    
def move_b2a(a,b):
    a.setfrom(b)    
    
def do_actions(id, a, b):
    if (id >= len(actions)):
        raise IndexError
    actions[id](a,b)
    
actions = [empty_a, empty_b, full_a, full_b, move_a2b, move_b2a]
actions_desc = ["empty 5 quart jug", "empty 3 quart jug", "full 5 quart jug", "full 3 quart jug", "move 5 quart jug to 3 quart jug", "move 3 quart jug to 5 quart jug"]
possible_result = []
possible_flow = []
answer = 4;

result = (0,0)
flow = []
state = 0

results = []
flows = []
states = []

results.append(result)
flows.append(flow)
states.append(state)

maxloop = 0
loop = 0
    
while(maxloop == 0 or loop < maxloop):

    for i in range(len(results)):
    
        if states[i] != 0:
            continue

        for j in range(len(actions)):                        
            jup5 = Jug(5, results[i][0])
            jup3 = Jug(3, results[i][1])
            flow = copy.copy(flows[i])
            do_actions(j, jup5, jup3)
            result = (jup5.volume, jup3.volume)
            print("result = {0},{1}".format(result[0], result[1]))
            if not result in results:
                results.append(result)
                flow.append(j)
                flows.append(flow)
                states.append(0)
            else:
                states[results.index(result)] = 1
                    
            if (answer == result[0] or answer == result[1]):
                jup5 = Jug(5, 0)
                jup3 = Jug(3, 0)           
                print("Found {0} by following steps: {1}".format(answer, flow))
                for k in range(len(flow)):             
                    before = (jup5.volume, jup3.volume)
                    do_actions(flow[k], jup5, jup3)
                    after = (jup5.volume, jup3.volume)       
                    print("step{0}: from {1} to {2} ({3})".format(k, before, after, actions_desc[flow[k]]))
                exit(0)    

        print("results = {0}".format(results))        

    print("loop {0} =============".format(loop))        
    loop = loop + 1
    



