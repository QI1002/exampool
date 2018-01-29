
#29. Divide Two Integers

def divide(a, b):
    if (b == 0):
        raise ZeroDivisionError("division by zero")
    if (a == 0):
        return 0

    if (a*b > 0):
        if (a < 0): a, b = -a, -b
        i, j = b, 0
        while(i <= a):
            j += 1
            i += b
    else:
        if (a > 0): a,b = -a, -b
        i, j = 0, 0
        while(i > a):
            j -= 1
            i -= b
    return j

a, b = 10, 3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = 9, 3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = 1, 3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = -10, -3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = -9, -3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = -1, -3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = -10, 3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = -9, 3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = -1, 3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = 10, -3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = 9, -3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)
a, b = 1, -3
print("{0}//{1}={2}({3})", a, b, divide(a, b), a//b)

