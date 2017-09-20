
#45. Jump Game II

def minJump(data):
    count = len(data)-1
    step = 1
    start = 0
    end  = start + data[start]
    while(end < count):
        #print((start,end))
        max = end
        for i in range(start+1, end, 1):
            if ((data[i]+i) > (data[max]+max)): max = i
        start = max 
        end = start + data[start]
        step += 1

    return step

print(minJump([2,3,1,1,4]))
print(minJump([2,3,2,1,1,4]))
print(minJump([3,3,1,2,1,4]))

