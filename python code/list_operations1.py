A = [[]]
B = []
print ('Enter number of rows in list')
#x = int(input())
##print ('Enter number of columns in list')
##y = int(input())
#A = [[10,2,13,4,5,66,7,11,-9] for i in range(x)]
A=[[4,5,6,7,62,33],[24,32,100,158,59,19],[32,57,99,8,44,17]]
x=3
for i in range(0,x,1):
    if i ==0:
        A[i] = A[i][x-1:]
    else:
        A[i] = A[i][(x-1)-i:-i]
##print (A)
for i in range(len(A)):
    B += A[i]
print (max(B))


