x=input()
y=input()
c=0
for i in x.split():
    for j in y.split():
        if(i.lower()==j.lower()):
            c+=1
print(c)