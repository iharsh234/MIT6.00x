# PROBLEM 7
#Write a Python function that returns a list of keys in aDict with the value target.
#The list of keys you return should be sorted in increasing order. 
#The keys and values in aDict are both integers. 
#(If aDict does not contain the value target, you should return an empty list.)

def keysWithValue(aDict, target):
   a = []
   for x in aDict:
       if aDict[x]== target:
           a.append(x)
   return a
