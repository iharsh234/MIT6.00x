# PROBLEM 1: COUNTING VOWELS
count = 0
for x in s.lower():
    if  x=="a" or  x =="e" or x == "i" or x =="o" or x == "u":
       count = count + 1
print "Number of vowels:",count

# PROBLEM 2: COUNTING 'BOB'S  
count = 0
for x in range(len(s)):
     x = s.find("bob")
     if x != -1:
        count = count+1
     s = s[x+2:]
print "Number of times bob occurs is:",count

# PROBLEM 3: ALPHABETICAL SUBSTRINGS
b = []
for num in s:
    c = ord(num)
    b.append(c)
f = []
for x in xrange(len(b)):
    for p in range(len(b)+1):
        d = b[x:p]
        e = sorted(d)
        if e == d:
            f.append(d)
h = []
for i in range(len(f)):
    g = len(f[i])
    h.append(g)
v = []
for j in range(len(f)):
    if len(f[j]) == max(h):
        v.append(f[j])
k = v[0]
harsh =  ''.join([chr(k[x]) for x in xrange(len(k)) ])
print "Longest substring in alphabetical order is:",harsh
