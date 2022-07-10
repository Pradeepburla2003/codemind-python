x=input()
y=input()
c=0
for i in x.lower():
    if i in y.lower():
        c+=1
if(c==len(x)):
    print('True')
else:
    print('False')