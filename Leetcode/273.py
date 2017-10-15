
#273. Integer to English Words

digits = ["zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "night", "ten", "eleven", "twelve",
          "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
          "eightenn", "nighteen"]

decades = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "nighty"]

def sintToEng(d):

    if (d >= 1000):
        raise Exception('larger than 999')

    h = d // 100
    dd = d - h*100

    #print((h,dd))
    result = ""
    if (h != 0):
        result += (digits[h] + " hundred")
        if (h != 1): result += "s"
    if (dd != 0):
        if (len(result) != 0): result += " "
        if (dd >= 20):
            result += decades[(dd-20)//10]
            ddd = (dd % 10)
            if (ddd != 0): result += (" " + digits[ddd])
        else:
            if (dd != 0): result += digits[dd]

    return result

def intToEng(d):

    if (d == 0): return digits[0]

    b = d//(1000*1000*1000)
    m = (d - b*(1000*1000*1000))//(1000*1000)
    t = (d - b*(1000*1000*1000) - m*(1000*1000))//1000
    dd = d - b*(1000*1000*1000) - m*(1000*1000) - t*1000
    print((b,m,t,dd))

    result = ""
    if (b != 0):
        result += (sintToEng(b) + " billion")
        if (b != 1): result += "s"
    if (m != 0):
        if (len(result) != 0): result += " "
        result += (sintToEng(m) + " million")
        if (m != 1): result += "s"
    if (t != 0):
        if (len(result) != 0): result += " "
        result += (sintToEng(t) + " thousand")
        if (t != 1): result += "s"
    if (dd != 0):
        if (len(result) != 0): result += " "
        result += sintToEng(dd)

    return result

for num in range(300):
    print("{0}=>{1}".format(num, intToEng(num)))

num = 4294967296
print("{0}=>{1}".format(num, intToEng(num)))

num = 1000001
print("{0}=>{1}".format(num, intToEng(num)))
