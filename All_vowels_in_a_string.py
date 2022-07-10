x=input()
ch="AEIOU"
ch2="aeiou"
d,d2=0,0
for i in ch:
    if i in x:
        d+=1
for i in ch2:
    if i in x:
        d2+=1
if(d==5 or d2==5):
    print('True')
else:
    print('False')