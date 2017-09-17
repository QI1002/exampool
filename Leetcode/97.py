
#97. Interleaving String

class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

def isInterleave(s1, s2, s3):

    st = stack()
    st.push((0,0,0))
    
    while(not st.isEmpty()):
        i, j, k = st.pop()
        
        while(k < len(s3)):
            m1 = (i < len(s1) and s3[k] == s1[i])
            m2 = (j < len(s2) and s3[k] == s2[j])
            if (m1):
                if (m2): st.push((i,j+1,k+1))    
                i += 1
                k += 1
            else:
                if (m2):
                    j += 1
                    k += 1    
                else:
                    break
                
        if (k == len(s3)): return True    
          
    return False
   
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"       
s4 = "aadbbbaccc"

print(isInterleave(s1, s2, s3))
print(isInterleave(s1, s2, s4))