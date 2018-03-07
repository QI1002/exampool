
#158. Read N Characters Given Read4 II 

class fileread:
    
    def __init__(self, sample):
        self.sample = sample 
        self.cursor = 0

    def reset(self):
        self.cursor = 0

    def read4(self):
        result = self.sample[self.cursor:self.cursor+4]
        self.cursor += len(result)
        return result

    def readN(self, n):
        nn = ((n+3)/4)*4
        result = ""
        for i in range(0, n, 4): result += self.read4()
        return result[:n]

    def read(self, n):
        result = self.sample[self.cursor:self.cursor+n]
        self.cursor += len(result)
        return result

example = "Read N Characters Given Read4 II"  
f = fileread(example)
n1, n2 = 3, 11
print("{0}:{1}".format(n1, f.readN(n1)))
print("{0}:{1}".format(n2, f.readN(n2)))
f.reset()
n1, n2 = 3, 11
print("{0}:{1}".format(n1, f.read(n1)))
print("{0}:{1}".format(n2, f.read(n2)))

