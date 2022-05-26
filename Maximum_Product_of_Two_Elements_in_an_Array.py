a=list(map(int,input().split()))
l=len(a)
a=sorted(a)
print((a[l-1]-1)*(a[l-2]-1))
