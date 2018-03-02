
#288. Unique Word Abbreviation

class dictionary:

    def getABB(self, s):
        if (len(s) <= 2): return s
        return s[0]+str(len(s)-2)+s[-1]

    def isUnique(self, s):
        abb = self.getABB(s)
        if (abb in self.abb):
            return (self.abb[abb] == s)
        else:
            return True

    def __init__(self, d):
        self.dict = d
        self.abb = {}
        for s in d:
            abb = self.getABB(s) 
            if (self.isUnique(s)):
                self.abb[abb] = s 
            else:
                self.abb[abb] = None

sample = ["deer", "door", "cake", "card"]
d = dictionary(sample)
s = "dear"
print("{0}:{1}".format(s, d.isUnique(s)))
s = "cart"
print("{0}:{1}".format(s, d.isUnique(s)))
s = "cane"
print("{0}:{1}".format(s, d.isUnique(s)))
s = "make"
print("{0}:{1}".format(s, d.isUnique(s)))

sample = ["deer"]
d = dictionary(sample)
s = "door"
print("{0}:{1}".format(s, d.isUnique(s)))

sample = ["door", "door"]
d = dictionary(sample)
s = "door"
print("{0}:{1}".format(s, d.isUnique(s)))

sample = ["deer", "door"]
d = dictionary(sample)
s = "door"
print("{0}:{1}".format(s, d.isUnique(s)))

