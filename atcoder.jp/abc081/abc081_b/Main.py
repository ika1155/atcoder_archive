n=input().rstrip()
a=list(map(int, input().split()))

count=0
j=True

while j:
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] /=2
        else:
            j=False

    if j:
        count+=1

print(count)