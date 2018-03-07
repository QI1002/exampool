
#157. Read N Characters Given Read4 

cursor = 0
example = "Read N Characters Given Read4"

def read4():
    global example, cursor
    result = example[cursor:cursor+4]
    cursor += len(result)
    return result 

def readN(n):
    nn = ((n+3)/4)*4
    result = ""
    for i in range(0, n, 4):
        result += read4()

    return result[:n]

cursor, n = 0, 11
print("{0}:{1}".format(n, readN(n)))
cursor, n = 0, 22
print("{0}:{1}".format(n, readN(n)))

