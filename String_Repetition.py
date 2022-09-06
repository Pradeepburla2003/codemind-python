a=input()
n=int(input())
s=a.count('a')
d=n//len(a)
k=n%len(a)
r=a[:k]
t=r.count('a')
print((s*d)+t)
