n=int(input())
l=[]

for i in range(n):
    l.append(input())

s=(list(set(l)))

print(len(s))