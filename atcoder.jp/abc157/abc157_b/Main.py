b=[]*3

for i in range(3):
    lis=list(map(int,input().split()))
    b.append(lis)

n = int(input())
num=[0]*n
ans="No"

for i in range(n):
    num[i] = int(input())

for i in range(3):
    for j in range(3):
        if b[i][j] in num:
            b[i][j] = 0

for i in range(3):
    if b[i][0] == b[i][1] == b[i][2]:
        ans="Yes"
    elif b[0][i] == b[1][i] == b[2][i]:
        ans="Yes"

if b[1][1] == b[2][2] == b[0][0]:
    ans = "Yes"
elif b[0][2]==b[1][1]==b[2][0]:
    ans = "Yes"


print(ans)