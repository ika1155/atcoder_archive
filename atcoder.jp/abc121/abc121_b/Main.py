n,m,c=map(int,input().split())

b=list(map(int,input().split()))
count=0

for i in range(n):
    ab=0
    a=list(map(int,input().split()))
    for j in range(m):
        ab += a[j]*b[j]
    ab += c
    if ab > 0:
        count += 1

print(count)