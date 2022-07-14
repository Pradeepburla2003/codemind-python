s1=input().lower()
s2=input().lower()
d=[]
for i in s1:
    if(i!=' ' and i not in s2):
        d.append(i)
for i in s2:
    if(i!=' ' and i not in s1):
        d.append(i)
d=sorted(set(d))
print(len(d))