x=input()
c=0
for i in x.split():
    if(i.lower()==i.lower()[::-1]):
        c+=1
print(c)