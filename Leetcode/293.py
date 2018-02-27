
#293. Flip Game

def allFlip(s):
    result = []
    for i in range(1, len(s)):
        if (s[i-1] == '+' and s[i] == '+'):
            result.append(s[:i-1]+"--"+s[i+1:])

    return result

given = "++++"
print("{0}:{1}".format(given, allFlip(given)))
