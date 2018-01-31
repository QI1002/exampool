
#3. Longest Substring Without Repeating Characters

def longest(s):
    i = 0
    ll = ""
    while(i < len(s)):
        j = i
        i += 1
        while(i < len(s)):
            if (s[i] in s[j:i]):
                if (len(s[j:i]) > len(ll)):
                    ll = s[j:i]
                break
            i += 1

    return ll

s = "abcabcbb"
print("{0} => {1}".format(s, longest(s)))
s = "bbbbb"
print("{0} => {1}".format(s, longest(s)))
s = "pwwkew"
print("{0} => {1}".format(s, longest(s)))

