import pickle
f = open('vectors_binary.bin','wb')
f1 = open('origvectors.txt','r')
a = f1.read()
f1.close()
pickle.dump(a,f)
f.close()

f = open('vectors_binary.bin','rb')
b = pickle.load(f)
f.close()

def get_module(a):
   from math import sqrt
   module = sqrt(abs(x)**2+abs(y)**2+abs(z)**2)
   return module

c = b 
e = a[:a.index('\n')]
a = a[a.index('('):]
d = []

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
   e = e + '\n' + str(tuple(i)) 
      
f2 = open('vectorsfile.txt','w')
f2.write(e)
f2.close()
f = open('vectors.bin','wb')
pickle.dump(e,f)
f.close()
