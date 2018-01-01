
#591. Tag Validator

def getComment(s, i):
    for k in range(i, len(s), 1):
        if (s[k:k+3] == "]]>"):
            return k

    return None

def getStartTag(s, i):
    for j in range(i+1, len(s), 1):
        if (s[j] == ">"):
            if ((j-i) >= 10): return None
            for k in range(i+1, j, 1):
                if (ord(s[k]) > ord('Z')): return None
                if (ord(s[k]) < ord('A')): return None
            return s[i+1:j] 

    return None 

def getEndTag(s, i):
    for j in range(i-1, -1, -1):
        if (s[j:j+2] == "</"):
            if ((i-j) >= 11): return None
            for k in range(j+2, i, 1):
                if (ord(s[k]) > ord('Z')): return None
                if (ord(s[k]) < ord('A')): return None
            return s[j+2:i] 

    return None 

def parse(s):

    for i in range(len(s)):
        if (s[i:i+9] == "<![CDATA["):
            j = getComment(s, i)
            if (j == None):  return False
            return parse(s[j+1:])
        if (s[i] == "<"):
            ts = getStartTag(s, i)
            if (ts == None): return False
            for j in range(len(s)-1, i-1, -1):
                if (s[j] == ">"): break
            if (s[j] != ">"): return False  
            te = getEndTag(s, j)
            if (te == None): return False
            if (ts != te): return False
            return parse(s[i+len(ts)+2:j-len(te)-2])     
    return True

print(parse("<DIV>test</DIV>"))
print(parse("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))
print(parse("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")) 
print(parse("<A>  <B> </A>   </B>"))
print(parse("<DIV>  div tag is not closed  <DIV>"))
print("==============================================")
print(parse("<DIV>  unmatched <  </DIV>"))
print(parse("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"))
print(parse("<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"))
print(parse("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"))
