a=input()
ch='aeuioAEUIO'
ch2='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
c=0
d=len(a)-1
for i in range(len(a)//2):
    if(a[i] in ch and a[d] in ch2):
        c+=1
    elif(a[i] in ch2 and a[d] in ch):
        c+=1
    d=d-1
print(c)