def fibbonacci(n):
    if n<2:
        return n
    else:
        a = (fibbonacci(n-1)+ fibbonacci(n-2))
        return  1+a
def Fibbonacci(n):
    if n<2:
        return n
    else:
        a = (Fibbonacci(n-1)+ Fibbonacci(n-2))
        return  a
    
n = 1
while n >0:
    print  (fibbonacci(n))
    n= n+1
    if n > 20:
        break
c = [1]
for i in range(30):
    c.append(Fibbonacci(30))
print (c)
print ('Enter a positive integer')
s = int(input())
n = 1
while n>0:
    b = fibbonacci(n)
    if b >= s:
        break
    n = n+1
if b == s:
    print ('sum is ',b, ' and n(number of fibbonacci numbers) is ',n)
else:
    print (s," is not a sum of 'n' fibbonaci numbers")

    


    
    




