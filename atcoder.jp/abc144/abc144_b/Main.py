n=int(input().rstrip())

l=[1,2,3,4,5,6,7,8,9]
j=True

for i in range(9):
    for j in range(9):
        s=l[i]*l[j]
        if n == s:
            j=False
            break
    if j == False:
        break
            

if j:
    print("No")
else:
    print("Yes")