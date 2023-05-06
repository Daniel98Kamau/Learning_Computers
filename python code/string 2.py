print ('Enter text.')
S = input ('')
if '(' and ')' in S:
    t= S.index('(')
else:
    print('Text has no brackets')
Z = []
Y = []
X = str()             
for i in range(len(S)):
    if S[i]==('('):
        Z= Z+[i+1]
    if S[i]==(')'):
        Y=Y+[i] 
for i in range(len(Z)):
    X= str(X+S[Z[i]].upper()+S[Z[i]+1:Y[i]])
print (X)

 



    
        
        
        


    

