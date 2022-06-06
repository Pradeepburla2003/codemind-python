x=input()
c=0
for i in x.split():
    c=len(i)
    break
for i in x.split():
    if(c>len(i)):
        c=len(i)
print(c)