n=int(input())
count=[0 for i in range(n)]

for i in range(n-1):
    a,b=map(int, input().split())
    count[a-1] +=1
    count[b-1] +=1

if n-1 in count:
    print("Yes")
else:
    print("No")