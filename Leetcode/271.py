
#271. Encode and Decode Strings 

def encode(s):
    result = ""
    count = 0
    word = None
    output = False
    for c in s:
        if (c == word):
            count += 1
            if (count > 255): count,output = 255, True
        else:
            if (word != None): output = True
            else: count, word = 1, c

        if (output):
            result += chr(count)
            result += word
            output = False
            count = 1
            word = c

    if (word != None):
        result += chr(count)
        result += word

    print(list(result))
    return result

def decode(s):
    result = ""
    for i in range(0,len(s),2):
        count = s[i]
        word = s[i+1]
        result += (word*ord(count))
    print(list(result))    
    return result    

data = 'abaabbc'
edata = encode(data)
print("{0}:{1}".format(data, decode(edata)))
