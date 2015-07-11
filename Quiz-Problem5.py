# PROBLEM 5

def lessThan4(aList):
   d = []
   for x in aList:
      if len(x) < 4:
         d.append(x)
   return d
