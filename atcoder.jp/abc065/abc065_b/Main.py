n = int(input())
a=[0]*n

for i in range(n):
    a[i]=int(input())

end=True
right=1
count=0

while end:
    right = a[right-1]
    count += 1

    if right == 2:
        print(count)
        end = False
    
    if count == n:
        print(-1)
        end = False