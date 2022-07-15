a=int(input())
b=a
a=str(a)
a=a[::-1]
c=pow(b,2)
d=''
for i in a:
    d+=i
d=int(d)
e=pow(d,2)
e=str(e)
e=int(str(e[::-1]))
if(c==e):
    print("True")
else:
    print('False')