def longest_word(words):
    longest_word = words[0]
    for item in words:
        if len(item)> len(longest_word):
            longest_word = item
    return (longest_word)
        
f = open('filestask.txt','r')
a = f.read()
f.close()
for i in a:
    if i.isalpha()==False and i!=' ' and i!='\n':
        a = a.replace(i,'')
        
b = 'This file contains words that start with letter (Aa)' + '\n'
d = a.split()
c = []
g = set(d)
count = 0
for i in g:
    if i[0] == 'a' or i[0] == 'A':
       c.append(i)
       count = count+1

if count == 0:
    print("Text has no words starting with 'a'")
else:
    for i in range(len(c)):
        for j in range(len(c)):
            if j>i:
               if len(c[i])>len(c[j]):
                   temp = c[i]
                   c[i] = c[j]
                   c[j] = temp
    for i in c:
        e = longest_word(c)
        if len(i) == len(e):
            e = e + ',' + i
print(e)



for i in range(len(c)):
    if i != len(c)-1:
        b = b + str(c[i]) + '\n'
    else:
        b = b + str(c[i])

f = open('awords.txt','w')
f.write(b)
f.close()

