
def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

def index_sort(people):
    weight = []
    height = []
    count = len(people)
    for i in range(count):
        weight.append(i)
        height.append(i)
        
    for i in range(count):
        hmin = wmin = i        
        for j in range(i+1, count, 1):    
            if (people[weight[j]][0] < people[weight[wmin]][0]):
                wmin = j
            if (people[height[j]][1] < people[height[hmin]][1]):
                hmin = j                
        swap(weight, i, wmin)
        swap(height, i, hmin)

    return weight, height

def index_convert(index):
    count = len(index)
    convert = []
    for i in range(count):
        convert.append("")
        
    for i in range(count):
        convert[index[i]] = i
        
    return convert    
    
def findConflict(sync1, sync2):
    count = len(sync1)
    conflict = [0 for i in range(count)]
    for i in range(count):
        for j in range(i+1, count, 1):
            if ((sync1[i] > sync1[j] and sync2[i] < sync2[j]) or 
                (sync1[i] < sync1[j] and sync2[i] > sync2[j])):
                #print(str(i)+ " "+str(j))
                #print(str(weight)+ " "+str(height))
                conflict[i] += 1
                conflict[j] += 1
    return conflict
                
def findMonoSeq(people, weight, height):
    #TODO: it's better to traverse all max values per steps, it may need stack
    while(True):
        conflict = findConflict(weight, height)
        print(people)
        print(conflict)
        max = 0
        for i in range(len(conflict)):
            if (conflict[max] < conflict[i]):
                max = i
                
        if (conflict[max] == 0):
            return people
                    
        weight.pop(max)
        height.pop(max)
        people.pop(max)
        
    return people
                     
people = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
#people = [(65,80),(70,150),(56,90),(75,190),(60,95),(68,110)]
#people = [(65,80),(70,150),(56,160),(75,190),(60,95),(68,110)]
count = len(people)
weight, height = index_sort(people)
print(people)
weight0 = index_convert(weight)
height0 = index_convert(height)
print("weight sort = {0} {1}".format([people[weight[i]][0] for i in range(count)], weight0))
print("height sort = {0} {1}".format([people[height[i]][1] for i in range(count)], height0))
print("===============================")
print(findMonoSeq(people, weight0, height0))