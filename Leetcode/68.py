
#68. Text Justification

def justify(ss, width):
    #print(ss)
    count = len(ss)
    gap = 0
    output = ""
    length = 0

    for i in range(len(ss)):
        length += len(ss[i])
    
    while(count != 0):
        v = ss.pop(0)
        #print((v, length, width, gap))
        output = output + " "*gap + v
        count -= 1
        if (count != 0):
            length -= len(v)          
            gap = (width - length - len(output))/ count
            if (width == 0): gap = 1

    return output   
    
def fullJustify(s, width = 16):
    tokens = s.split()
    result = []
    start = 0
    length = 0
    for i in range(len(tokens)):
        length += len(tokens[i])
        if (start != i): length += 1
        print((start, length, tokens[i]))
        if (length > width):            
            ss = [tokens[j] for j in range(start, i, 1)]
            result.append(justify(ss, width))
            start = i
            length  = len(tokens[i])

    result.append(justify(tokens[start:], 0)) 
    return result

#sample = "This is an example of text justification."
sample = "Extra spaces between words should be distributed as evenly as possible."
lines = fullJustify(sample, 22)
for line in lines:
    print(line)
