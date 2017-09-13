
#57. Insert Interval

def line_overlay(line, p):
    return (line[0] <= p and line[1] >= p) 

def line_merge(lines, target):

    result = []
    newline = None
    prev_end = target[0] if target[0] < lines[0][0] else lines[0][0]
    prev_end -= 1

    for i in range(len(lines)):

        overlay = False
        line = lines[i]
        prev_end = prev_end if i == 0 else lines[i-1][1]

        if (line_overlay(line, target[0])):
            overlay = True
            newline = line
        else:
           if (target[0] < line[0] and target[0] > prev_end):
               newline = (target[0], line[1])

        #print((newline, line, e))

        if (line_overlay(line, target[1])):
            newline = (newline[0], line[1])
            result.append(newline)
            overlay = True
            newline = None
        else:
            if (target[1] < line[0] and target[1] > prev_end):
                newline = (newline[0], target[1])
                result.append(newline)
                newline = None

        #print((newline, overlay, result, line, s))

        if (newline == None and overlay == False):
            result.append(line)

    if (newline != None):
        result.append((newline[0], target[1]))

    if (target[0] > prev_end):
        result = list(lines)
        result.append(target)

    return result
               

lines = [(2,3),(5,8),(11,13)]
print(line_merge(lines, (9,10)))
print(line_merge(lines, (9,11)))
print(line_merge(lines, (8,10)))
print(line_merge(lines, (8,11)))
print(line_merge(lines, (14,16)))
print(line_merge(lines, (0,1)))
print(line_merge(lines, (4,14)))
print(line_merge(lines, (0,10)))
print(line_merge(lines, (0,14)))

 
