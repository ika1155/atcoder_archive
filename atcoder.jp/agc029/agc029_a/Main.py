s = list(input().rstrip())
count=0
b=0

for i in s:
    if i == "B":
        b += 1
    else:
        count += b

print(count)