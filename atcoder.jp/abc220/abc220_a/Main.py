a,b,c=map(int,input().split())

p=b//c

if p*c >= a:
    print(p*c)
else:
    print(-1)