x=input()
c=0
for i in x.split():
    if(c%2==0):
        print(i.lower()[::-1],end=" ")
    else:
        print(i,end=" ")
    c+=1