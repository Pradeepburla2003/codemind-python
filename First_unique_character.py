x=input()
m=0
for i in x:
    c=x.count(i)
    if(c==1):
        print(i)
        m=1
        break
if(m==0):
    print('-1')