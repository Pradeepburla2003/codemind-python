x=input()
c,k=0,0
for i in range(len(x)):
    c=0
    for j in range(0,len(x)):
        if(x[i]==x[j] and i!=j):
            c=1
            break
    if(c==0):
        print(x[i])
        k=1
        break
if(k==0):
    print("-1")