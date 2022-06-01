x,y=map(int,input().split())
a=[int(i) for i in str(x)]
l=len(a)
s1,s2,j=0,0,0
for i in a:
    s1=s1*10+i
    j+=1
    if(j==y):
        break
for i in range(l-y,l):
    s2=s2*10+a[i]
print(abs(s1-s2))
    
    