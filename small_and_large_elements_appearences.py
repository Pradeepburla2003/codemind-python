x=input()
a=[]
for i in x:
    if(i!=' '):
        a.append(i)
print(min(a),a.count(min(a)),max(a),a.count(max(a)))