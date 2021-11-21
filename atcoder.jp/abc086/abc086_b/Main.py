a, b=map(str,input().split())
ab = int(a+b)

c= ab ** 0.5

if c.is_integer():
    print("Yes")

else:
    print("No")