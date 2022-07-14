s1=input().lower()
s2=input().lower()
d=[]
for i in s1:
    if(i!=' ' and i in s2):
        d.append(i)
print(len(sorted(set(d))))