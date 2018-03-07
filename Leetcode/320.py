
#320. Generalized Abbreviation 

def abbr(s):
    if (len(s) == 0): return [s]

    result = [s]
    for i in range(0, len(s)):
        for j in range(1, len(s)+1-i):
            news = s[:i] + str(j) + s[i+j:i+j+1]
            r = abbr(s[i+j+1:])
            if (len(r) == 0): result.append(news)
            else:
                for x in r: result.append(news+x)
   
    return result

print(abbr("w"))
print(abbr("wo"))
print(abbr("wor"))
print(abbr("word"))


