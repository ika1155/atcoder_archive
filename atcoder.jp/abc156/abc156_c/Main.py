n=int(input())
li=list(map(int, input().split()))

s=round(sum(li)/n)
count=0
for i in li:
  count += (i-s)**2

print(count)