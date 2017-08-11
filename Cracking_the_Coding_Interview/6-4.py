
#if hats = 1 , there shall be a man to see there is no one who wear hats 
#but genie says there is hat in these people, so he will know he wear the only hat and remove it
#if hats = 2, but no one remove it in the first night. So there shall be a man to see there is a man who wear hats 
#and but he don't remove it in first night, so he will know he wear the another hat also so both of them will remove it in the second night 
#if hats = 3 ... imply from hats = 2 

def removeHats(hats):
    if (hats == 1): 
        return 1 
    
    return removeHats(hats-1)+ 1 
        

hats = 10
print("We need {0} days to remove {1} hats from genie".format(removeHats(hats), hats))

