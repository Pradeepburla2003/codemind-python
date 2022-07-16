a=input()
b=[]
for i in a:
    if(i.isalpha() or i.isdigit()):
        b.append(i)
b=sorted(b)
j=0
for i in a:
    if(i.isdigit() or i.isalpha()):
        print(b[j],end="")
        j+=1
    else:
        print(i,end="")