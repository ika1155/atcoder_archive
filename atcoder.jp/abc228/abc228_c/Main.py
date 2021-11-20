import sys
def main():
    input = sys.stdin.readline

    n, k =map(int,input().split())
    score=[0]*n

    for i in range(n):
        p1, p2, p3 = map(int,input().split())
        score[i]=(p1+p2+p3)

    rank=sorted(score, reverse=True)

    for i in score:
        if i + 300 >=rank[k-1]:
                print("Yes")
        else:
                print("No")

    
if __name__ =='__main__':
    main()