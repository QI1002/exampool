
#186. Reverse Words in a String II

def reverse(ss):
    result = ""
    count = len(ss)
    end = i = count-1
    while (i >= 0):
        if (ss[i] == " "):
            if (end != i):
                result += ss[i+1:end+1]
            result += " "
            end = i-1
        i -= 1

    if (end > 0):
        result += ss[:end+1]

    return result

sample = "the sky is blue"
print("\"{0}\"=>\"{1}\"".format(sample, reverse(sample)))
sample = " the sky is blue "
print("\"{0}\"=>\"{1}\"".format(sample, reverse(sample)))
sample = "  the sky   is blue    "
print("\"{0}\"=>\"{1}\"".format(sample, reverse(sample)))

         
