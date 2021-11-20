n, x = map(int, input().split())
fri=list(map(int, input().split()))
ans=[0 for i in range(n)]
end = True

s=x-1

while end:
    if ans[s] == 0:
        ans[s] = 1
        s = fri[s]-1
    else:
        end = False

print(ans.count(1))