# PROBLEM 4  

def myLog(x,b):
   c = [x,b]
   x = max(c)
   b = min(c)
   if x%b == 0 and b%2 == 0 and b>2:return 0
   d = []
   for i in range(x/b):
       if b**i == x:
           return i
       elif b**i < x:
           d.append(i)
   return d[-1]
