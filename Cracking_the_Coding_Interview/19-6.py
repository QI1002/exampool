
def showS(num):
    return "" if (num == 1) else "s" 
    
def showNum999999(num):
    if (num > 999999):
        return ""

    if (num == 0):
        return showNum999(num)
        
    if (num <= 999):
        result = ""
    else:    
        result = showNum999(num//1000) + " Thunred" + showS(num//1000) + " "
    
    if ((num % 1000) != 0):
        result += showNum999(num % 1000)
    
    return result
        
def showNum999(num):
    zero = "Zero"
    digit = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Night", "Ten", 
             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nighteen"]
    decade = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Nighty"]         
    
    if (num > 999):
        return ""
        
    if (num == 0):
        return zero
        
    if (num < 100):    
        result = ""  
    else:
        result = digit[num//100] + " Hundred" + showS(num//100) + " "
        
    re = num - (num//100)*100    
    if (re < 20):
        result += ("" if (re == 0) else digit[re])
    else:
        result += (decade[re//10] + digit[re%10])
        
    return result
    
for i in range(999950,999999,1):
    print("{0:06d}={1}".format(i,showNum999999(i)))            
    