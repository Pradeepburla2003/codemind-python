x=input()
y=input()
for i in y.lower().split():
    if i in x.lower().split():
        print(i,end=" ")