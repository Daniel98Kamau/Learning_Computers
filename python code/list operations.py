##print ('Enter number of list elements (n).')
##n = int(input())
A = []
A = [1,0,2,6,8]
n = len(A)
B = []
a = 0
while a<n-1:
    for j in range(n - 1):
        if A[j]< A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
    a = a + 1
B.append(A[0])
n = B[0]- A[len(A)-1]
for i in range(n):
    B.append(B[i]-1)   
i = 0
m = len(B)
while i<len(B):
    if B[i] in A:
        del B[i]
    i = i + 1
print (B)






    

         
