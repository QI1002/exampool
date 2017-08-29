
def getAnalysisNew(strValue):
    result = []
    for i in range(256):
        result.append(0)
    count = len(strValue)
    for i in range(count):
        result[ord(strValue[i])] += 1

    return result

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

def isAnagram(str1, str2, newflow = False):
    ana = getAnalysisNew if newflow else getAnalysis
    result1 = ana(str1)
    result2 = ana(str2)
    count = len(result1)
    for i in range(count):
        if (result1[i] != result2[i]):
            return False
    return True

def isAnagramNew(str1, str2):
    sort1 = "".join(sorted(list(str1)))
    sort2 = "".join(sorted(list(str2)))
    return sort1 == sort2

#method = isAnagram
method = isAnagramNew

str1 = "dormitory"
str2 = "dirtyroom"

print("The anagram between {0} and {1} is {2}".format(str1, str2, method(str1, str2)))

str1 = "dormitory"
str2 = "a dirty room"

print("The anagram between {0} and {1} is {2}".format(str1, str2, method(str1, str2)))

