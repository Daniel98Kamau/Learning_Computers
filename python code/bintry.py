f = open('binaryfile.bin','wb')
a = '''This is a collection of vectors in space, where n = 3.
(1,0,0)
(8,6,-7)
(9,8,7)
(0,0,0)
(20,3,1000)
(556,5,4)
(0,1,4)
(1,2,3)
(9,9,9)
(-7,-7,-9)
(3,6,8)
(12,5,0)
(4,8,0)
(1,1,1)
(7,8,9)'''
b = bytes(a,'utf-16')
f.write(b)
f.close()
f = open('binaryfile.bin','rb')
d = f.read()
f.close()
a = d.decode('utf-16')

def get_module(a):
   from math import sqrt
   module = sqrt(abs(x)**2+abs(y)**2+abs(z)**2)
   return module

e = a[:(a.index('(')-1)]
a = a[a.index('('):]
d = []
c = str()

for i in a:
    if i == '\n': 
        a = a.replace(i,',')
    elif i == '(' or i==')':
        a = a.replace(i,'')

b = a.split(',')
for i in range(len(b)):
   b[i] = int(b[i])
for i in range(0,len(b),3):
   d.append(b[i:i+3])

for i in range(len(d)): 
   x = d[i][0]
   y = d[i][1]
   z = d[i][2]
   module1 = get_module(d[i])
   for j in range(len(d)):
      x = d[j][0]
      y = d[j][1]
      z = d[j][2]
      module2 = get_module(d[j])
      if module2 > module1:
         d[j],d[i] = d[i],d[j]

for i in d:
    c += '\n' +str(tuple(i))
for i in c:
    if i == ' ':
        c = c.replace(i,'')
e = e+c

f = open('vectorsfile.txt','w')
f.write(e)
f.close()

f = open('binaryfile.bin','wb')
e = bytes(e,'utf-16')
f.write(e)
f.close()
