#https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

n=int(input())

x=n/1.08

if x.is_integer():
    print(int(x))
else:
    a=(int(x)+1)*1.08
    if int(a) == n:
        print(int(x)+1)
    else:
        print(":(")