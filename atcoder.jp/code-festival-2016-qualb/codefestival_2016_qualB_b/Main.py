n, a, b=map(int, input().split())
s = list(input())
count=0
count_f=0

for i in s:
    if i == "c":
        print("No")
    
    if i == "a":
        if count < a+b:
            print("Yes")
            count += 1
        else:
            print("No")
    
    if i == "b":
        if count < a + b and count_f < b:
            print("Yes")
            count += 1
            count_f += 1
        else:
            print("No")