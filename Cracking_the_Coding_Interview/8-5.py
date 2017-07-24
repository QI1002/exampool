
def addset(result, data):
    if (not data in result):
        result.append(data)

def parentheses(org, n):
    if (org == "" and n == 1):
        return ["()"]
    else:
        result = []
        stack = []
        if (n == 1):
            base = [org]
        else:
            base = parentheses(org, n-1)

        for x in base:

            addset(result, "()"+x)
            addset(result, x+"()")

            for i in range(len(x)):
                if x[i] == '(':
                    stack.append(i)
                if x[i] == ')':
                    j = stack.pop()
                    if (len(stack) == 0):
                        more = parentheses(x[j+1:i], 1)
                        for y in more:
                            addset(result, x[0:j+1]+y+x[i:])

                        addset(result, x[0:i+1]+"()"+x[i+1:])
        return result

answer = parentheses("",4)
print("2 parentheses = {0} with len = {1}".format(answer, len(answer)))

