n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
b=list(set(a))
c=[]
for i in b:
    c.append(a.count(i))
c=sorted(c)
c=c[::-1]
d=[]
for j in range(len(c)):
    for i in a:
        if(a.count(i)==c[j] and i not in d):
            d.append(i)
            break
print(*d)