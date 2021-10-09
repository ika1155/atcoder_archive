n,p=map(int,input().split())

score=list(map(int,input().split()))

total=0

for i in range(n):
    
    if score[i]<p:
        total += 1

print(total)