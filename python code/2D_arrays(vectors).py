import math 
A = [6,2,0]
B = [[4,5,6],[6,5,3],[1,0,9],[8,2,0],[6,3,0],[6,2,0],[7,7,8],[4,-7,9],[9,11,1],[1,2,0]]
print (B)
m = len(A)
n = len(B)
c = []
#k is the ratio of dot product (A.B) and product of magnitudes of (A,B)equal to cos()
x = A[0]*B[0][0]+ A[1]*B[0][1]+ A[2]*B[0][2]
a = math.sqrt(A[0]**2+A[1]**2+A[2]**2)
##(a) is the magnitude of vector A
b = math.sqrt(B[0][0]**2+B[0][1]**2+B[0][2]**2)
##(b) is the magnitude of vector B[0]
y = a*b
kmax = x/y
i = 0
while i <n:
    x = A[0]*B[i][0]+ A[1]*B[i][1]+ A[2]*B[i][2]
    a = math.sqrt(A[0]**2+A[1]**2+A[2]**2)
    b = math.sqrt(B[i][0]**2+B[i][1]**2+B[i][2]**2)
    y = a*b
    k = x/y
    if k > kmax:
        kmax = k
        c = B[i]
    i = i+1
print ('vector from B forming min angle with A is ' ,c)
##print (kmax)
       

    

    

        

