s1=input().split()
s2=input().split()
d=[]
for i in s1:
    if i in s2:
        d.append(i)
c=0
for i in d:
    if(s1.count(i)==s2.count(i)):
        c+=1
print(c)