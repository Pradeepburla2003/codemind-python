s=input()
t=input()
stag=[]
for i in range(len(s)):
    if s[i]!='#':
        stag.append(s[i])
    else:
        stag.pop()
stag1=[]
for i in range(len(t)):
    if t[i]!='#':
        stag1.append(t[i])
    else:
        stag1.pop()
print(stag==stag1)
        