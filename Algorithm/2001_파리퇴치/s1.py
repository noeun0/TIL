import sys

sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N,M=map(int,input().split(" "))
    list_l=[]
    for _ in range(N):
        list_l.append(list(map(int,input().split(" "))))

    result=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum1=0
            for x in range(M):
                for y in range(M):

                    sum1 += list_l[i+x][j+y]

            if result<=sum1:
                result =sum1

    print("#{} {}".format(tc,result))