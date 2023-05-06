Class=[{'admNo.':'001','name':'Kamau','subject':['math','language','arts','history','science'],'score':[70,60,80,70,86]},{'admNo.':'002','name':'John','subject':['math','language','arts','history','science'],'score':[40,40,40,40,40]},{'admNo.':'003','name':'Ndegwa','subject':['math','language','arts','history','science'],'score':[50,50,50,50,50]},{'admNo.':'004','name':'Kamau','subject':['math','language','arts','history','science'],'score':[30,30,30,30,30]},{'admNo.':'005','name':'Muhia','subject':['math','language','arts','history','science'],'score':[20,71,72,73,74]},{'admNo.':'006','name':'Kelvin','subject':['math','language','arts','history','science'],'score':[60,65,33,50,45]},{'admNo.':'007','name':'Mau','subject':['math','language','arts','history','science'],'score':[41,42,43,44,45]},{'admNo.':'008','name':'Grace','subject':['math','language','arts','history','science'],'score':[90,38,81,82,83]},{'admNo.':'009','name':'Mary','subject':['math','language','arts','history','science'],'score':[70,34,60,50,40]},{'admNo.':'010','name':'Smith','subject':['math','language','arts','history','science'],'score':[60,40,30,30,30]},{'admNo.':'011','name':'Joj','subject':['math','language','arts','history','science'],'score':[36,34,21,39,41]},{'admNo.':'012','name':'Tim','subject':['math','language','arts','history','science'],'score':[50,51,52,53,55]},{'admNo.':'013','name':'Omondi','subject':['math','language','arts','history','science'],'score':[45,20,48,30,50]},{'admNo.':'014','name':'Bett','subject':['math','language','arts','history','science'],'score':[67,78,89,90,84]}]
z = []
for i in range (len (Class)):
    q = Class[i]['score']
    count=0
    for y in q:
        if y<=40:
            count = count+1
    if count>1:
        print(Class[i]['admNo.'],Class[i]['name'])
    else:
        z.append(Class[i])
for i in range(len(z)):
    print(z[i])
