
#163. Missing Ranges

def missingRanges(data, lower, upper):
    mylower = lower
    myupper = upper
    result = []
    for i in range(len(data)):
        if (data[i] < lower or data[i] > upper):
            continue
        if (data[i] == mylower): 
            mylower += 1
            continue
        if (data[i] == myupper):
            myupper -= 1
            continue
        if (mylower == (data[i]-1)):
            result.append(str(mylower))
        else:
            result.append(str(mylower)+"->"+str(data[i]-1)) 
        mylower = data[i]+1

    if (mylower == (myupper-1)):
        result.append(str(mylower))
    else:
        result.append(str(mylower)+"->"+str(myupper))

    return result

sample = [0,1,3,50,75]
print("{0}=>{1}".format(sample, missingRanges(sample, 0, 99)))
sample = [0,1,3,50,75,99,101]
print("{0}=>{1}".format(sample, missingRanges(sample, 0, 99)))
sample = [-3,1,3,50,75]
print("{0}=>{1}".format(sample, missingRanges(sample, 0, 99)))

