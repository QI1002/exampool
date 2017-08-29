import sys

def getGitDate(filename):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if (lines[i][:6] == "Date: "):    
            print(lines[i][6:])
            break
            
if (len(sys.argv) == 2):
    getGitDate(sys.argv[1])    
        