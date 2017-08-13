
# draw them in graph

class rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def center(self):
        x = self.x + self.width/2
        y = self.y + self.height/2
        return (x,y)
        

        
class line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.coeff()
    def coeff(self):
        self.b = xdiff = self.x1 - self.x2
        self.a = ydiff = self.y2 - self.y1 
        self.c = - (self.a * self.x1 + self.b * self.y1)    
        self.coeff = (self.a,self.b,self.c)
    def equation(self, point):
        return self.a * point[0] +self.b * point[1] + self.c
    
center1 = rectangle(0,0,2,1).center()
center2 = rectangle(10,10,12,20).center()
cl = line(center1[0], center1[1], center2[0], center2[1])
print("the line {0} pass {1} with result {2}".format(cl.coeff, center1,cl.equation(center1)))
print("the line {0} pass {1} with result {2}".format(cl.coeff, center2,cl.equation(center2)))
    
        
        