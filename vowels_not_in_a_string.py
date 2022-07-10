x=input()
ch2="aeiou"
d=0
for i in ch2:
    if i not in x:
        print(i,end=" ")
        d=1
if(d==0):
    print('0')
