n=int(input())
m=list(map(int,input().split()))
count=0
ans=set()

for i in range(1, 150):
    for j in range(1,150):
        ans.add(4*i*j+3*i+3*j)


for i in m:
    if i not in ans:
        count += 1

print(count)
