n=int(input())
d=list(str(n*n))
a=list(str(n))
s=len(a)
d=d[s:len(d)]
c=0
for i in a:
    if i not in d:
        c+=1
        break
if(c==0):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')