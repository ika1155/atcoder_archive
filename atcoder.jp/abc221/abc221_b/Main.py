s=list(input())
t=list(input())
a="No"

if s==t:
    a="Yes"

for i in range(len(s)-1):
    s[i], s[i+1] = s[i+1], s[i]
    if s==t:
        a="Yes"
    s[i], s[i+1] = s[i+1], s[i]

print(a)