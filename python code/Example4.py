print ('Enter a decimal number.')
X = int ( input () )
Y = str (X%2)
if X == 0:
    print (0)
while X != 1:
    X = int ( (X-X%2)//2 )
    Y = ( Y+ str (X%2))
##print (Y)
##print (Y[ : :-1 ])
##print ( Y [-1])
z = str( )
for i in range ( len (Y)-1,-1,-1):
    z = str( z + Y[i] )
    #print ( Y[i], end = '' ) 
print(z)


    
    
    

    


