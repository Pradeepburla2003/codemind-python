x=input().split()
s1,s2=0,0
for i in x:
    s1+=ord(min(i))
    s2+=ord(max(i))
print(s2-s1)