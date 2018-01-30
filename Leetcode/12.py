
def toRoman(num):
    if (num >= 8000): 
        return None

    r = ""
    five = ["V", "L", "D", "MMMMM"]
    one = ["I","X","C","M"]
    step = 10
    for i in range(4):
        d = num % step
        d = (d*10)//step
        step *= 10
        if (d > 5): 
            if (d == 5):
                r = five[i] + r
            else:    
                r = five[i] + one[i]*(d-5) + r
        else:  
            if (d != 0): r = one[i]*d + r

    return r 

a = 7777
print("{0}'s roman = {1}", a, toRoman(a))
a = 2222
print("{0}'s roman = {1}", a, toRoman(a))
a = 1000
print("{0}'s roman = {1}", a, toRoman(a))

