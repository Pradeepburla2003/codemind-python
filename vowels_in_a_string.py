x=input()
y=input()
j=0
for i in range(len(x)):
    if x[i]==y:
        print("True")
        print(i)
        j=1
        break
if(j==0):
    print("False")
        