a=input()
b=str(set(a))
d=[]
for i in b:
    k=a.count(i)
    d.append(k)
if(len(a)==len(list(set(a)))):
    print('-1')
elif(len(d)==len(list(set(d)))):
    print('-1')
else:
    d=sorted(list(set(d)))
    t=d[len(d)-2]
    for i in b:
        if(t==a.count(i)):
            print(i)
            quit()