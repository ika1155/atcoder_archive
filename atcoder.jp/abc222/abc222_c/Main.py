n,m=map(int, input().split())
#2N人　m=ラウンド数

jan=[[0 for i in range(m)]for j in range(2*n)]
#勝数、番号
rank = [[0,i]for i in range(2*n)]


def win(a,b):
    if a=="G":
        if b=="G":
            return "D"
        elif b=="C":
            return "A"
        else: #P
            return "B"
    elif a=="C":
        if b=="G":
            return "B"
        elif b=="C":
            return "D"
        else: #P
            return "A"
    else: #P
        if b=="G":
            return "A"
        elif b=="C":
            return "B"
        else: #P
            return "D"

for i in range(2*n):
    line=input().rstrip()
    
    for j in range(m):
        jan[i][j]=line[j]


for i in range(m):
    for j in range(n):
        p1=rank[2*j][1]
        p2=rank[2*j+1][1]
        
        a=jan[p1][i]
        b=jan[p2][i]
        
        winner=win(a,b)

        if winner=="A":
            rank[2*j][0] -=1
        elif winner=="B":
            rank[2*j+1][0] -=1
        else:
            continue
        
        rank.sort()

for i in range(n*2):
    print(rank[i][1]+1)
