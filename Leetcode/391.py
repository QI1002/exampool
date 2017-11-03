
#391. Perfect Rectangle 

def prefectRect(rects):
    l,b,r,t = rects[0]
    for i in range(1,len(rects),1):
        if (rects[i][0] < l): l = rects[i][0]    
        if (rects[i][1] < b): b = rects[i][1]    
        if (rects[i][2] > r): r = rects[i][2]    
        if (rects[i][3] > t): t = rects[i][3]    
    
    row = [ 0 for i in range(r-l) ]
    m = [ list(row) for i in range(t-b) ]
    
    for i in range(len(rects)):
        for j in range(rects[i][0], rects[i][2], 1):
            for k in range(rects[i][1], rects[i][3], 1):
                m[k-b][j-l] += 1

    for j in range(l, r, 1):
        for k in range(b, t, 1):
            if (m[k-b][j-l] != 1):
                return False

    return True 

rectangles1 = [ [1,1,3,3], 
                [1,1,3,3],
                [1,1,3,3],
                [1,1,3,3] ] 

rectangles1 = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
print(prefectRect(rectangles1))

rectangles2 = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
print(prefectRect(rectangles2))

rectangles3 = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
print(prefectRect(rectangles3))

rectangles4 = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
print(prefectRect(rectangles4))
