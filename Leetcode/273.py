
#273. Integer to English Words

digits = ["zero", "one", "two", "three", "four", "five", 
          "six", "seven", "eight", "night", "ten", "eleven", "twelve",
          "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
          "eightenn", "nighteen"]
          
decades = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "nighty"]           

def sintToEng(d):

    if (d >= 10000):
        raise Exception('larger than 9999')
        
    t = d // 1000
    h = (d - t*1000) // 100
    dd = d - t*1000 - h*100
    
    #print((t,h,dd))
    result = ""
    if (t != 0):
        result += (digits[t] + " thousand")
        if (t != 1): result += "s"
    if (h != 0):
        if (len(result) != 0): result += " "
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
    return sintToEng(d)
    
for num in range(300):
    print("{0}=>{1}".format(num, intToEng(num)))        

for num in range(1000, 1100, 1):
    print("{0}=>{1}".format(num, intToEng(num)))
    
for num in range(2000, 2100, 1):    
    print("{0}=>{1}".format(num, intToEng(num)))
