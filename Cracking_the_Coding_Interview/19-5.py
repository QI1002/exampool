
import random
import copy

def min(a,b):
    if (a > b):
        return b
    else:
        return a
            
class colorGuess:
    def __init__(self, solution = None):
        self.colors = ['R', 'Y', 'G', 'B']
        self.sample = {'R':0, 'Y':0, 'G':0, 'B':0}
        if (solution != None):
            self.solution = solution
            for i in range(4):
                self.sample[self.solution[i]] += 1            
        else:       
            self.solution = []        
            for i in range(4):
                index = random.randint(0,3)
                self.solution.append(self.colors[index])
                self.sample[self.solution[i]] += 1
                   
    def guess(self, answer):
        if (len(answer) != 4):
            return (0,0)
        
        hit = 0
        pesudo_hit = 0    
        solution_sample = copy.copy(self.sample)
        guess_sample = {'R':0, 'Y':0, 'G':0, 'B':0}
        for i in range(4):
            if (answer[i] == self.solution[i]):
                hit += 1
                solution_sample[answer[i]] -= 1
            else:            
                guess_sample[answer[i]] += 1
                
        for key in guess_sample:
            pesudo_hit += min(guess_sample[key], solution_sample[key])
            
        return (hit, pesudo_hit)           
        

cg = colorGuess(['R','G','G','B'])
ans = ['Y','R','G','B']
print("colorGuess {0} for {1} is {2}".format(ans, cg.solution, cg.guess(ans)))
ans = ['Y','R','G','G']
print("colorGuess {0} for {1} is {2}".format(ans, cg.solution, cg.guess(ans)))           
ans = ['Y','Y','Y','Y']
print("colorGuess {0} for {1} is {2}".format(ans, cg.solution, cg.guess(ans)))           
ans = ['G','G','G','G']
print("colorGuess {0} for {1} is {2}".format(ans, cg.solution, cg.guess(ans)))                 
cg = colorGuess()
print("colorGuess {0} for {1} is {2}".format(ans, cg.solution, cg.guess(ans))) 