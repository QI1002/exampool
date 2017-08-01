
import math

def swap(l,i,j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def tuple_sort(collection):
    count = len(collection)
    index = len(collection[0]) -1
    for i in range(count):
        min = i
        for j in range(i+1, count, 1):
            if (collection[min][index] > collection[j][index]):
                min = j
        swap(collection, min, i)
    return collection

def sumLimit(a,b,limit):
    collection = []
    b_upper = math.floor(limit/b)+1
    for i in range(b_upper):
        a_upper = math.floor((limit - (i*b))/a)+1
        for j in range(a_upper):
            collection.append((j, i, j*a+i*b))

    return len(collection), collection

def multipleLimit2(a,b,limit):
    collection = []
    b_upper = math.floor(math.log(limit,b))+1
    for i in range(b_upper):
        a_upper = math.floor(math.log(limit/math.pow(b,i),a))+1
        for j in range(a_upper):
            collection.append((j, i, int(math.pow(a,j)*math.pow(b,i))))

    return len(collection), collection


def multipleLimit3(a,b,c,limit):
    collection = []
    c_upper = math.floor(math.log(limit,c))+1
    for i in range(c_upper):
        b_upper = math.floor(math.log(limit/math.pow(c,i),b))+1
        for j in range(b_upper):
            a_upper = math.floor(math.log(limit/math.pow(c,i)/math.pow(b,j),a))+1
            for k in range(a_upper):
                collection.append((k, j, i, int(math.pow(a,k)*math.pow(b,j)*math.pow(c,i))))

    return len(collection), collection

def multipleLimit3Nozero(a,b,c,limit):
    collection = []
    c_upper = math.floor(math.log(limit,c))+1
    for i in range(1,c_upper,1):
        b_upper = math.floor(math.log(limit/math.pow(c,i),b))+1
        for j in range(1,b_upper,1):
            a_upper = math.floor(math.log(limit/math.pow(c,i)/math.pow(b,j),a))+1
            for k in range(1,a_upper,1):
                collection.append((k, j, i, int(math.pow(a,k)*math.pow(b,j)*math.pow(c,i))))

    return len(collection), collection

def findKNozero(a,b,c,k):
    limit = math.floor(math.pow(a,k/3))
    collection = []
    sum = 0
    while(sum < k):
        sum, collection = multipleLimit3Nozero(3,5,7,limit)
        limit *= 10
        tuple_sort(collection)
    return collection[k]

#print(sumLimit(3,5,20))
#print(sumLimit(3,5,40))

#print(multipleLimit2(3,5,200))
#print(multipleLimit2(3,5,1000))

print(tuple_sort(multipleLimit3Nozero(3,5,7,1000000)[1]))
#print(str(50) + " " + str(findKNozero(3,5,7,50)))


