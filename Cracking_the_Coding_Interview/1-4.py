
def getAnalysis(strValue):
    result = []
    for i in range(26):
        result.append(0)
    count = len(strValue)
    for i in range(count):
        if (strValue[i] >= 'A' and strValue[i] <= 'Z'):
            result[ord(strValue[i]) - ord('A')] += 1
        if (strValue[i] >= 'a' and strValue[i] <= 'z'):
            result[ord(strValue[i]) - ord('a')] += 1
    return result
            
def isAnagram(str1, str2):
    result1 = getAnalysis(str1)
    result2 = getAnalysis(str2)
    count = len(result1)
    for i in range(count):
        if (result1[i] != result2[i]):
            return False
    return True
    
str1 = "dormitory"
str2 = "dirty room"   

print("The anagram between {0} and {1} is {2}".format(str1, str2, isAnagram(str1, str2)))

str1 = "dormitory"
str2 = "a dirty room"   

print("The anagram between {0} and {1} is {2}".format(str1, str2, isAnagram(str1, str2)))
         