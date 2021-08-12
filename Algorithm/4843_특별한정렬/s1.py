import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    list_n=list(map(int,input().split()))
    list_n.sort()
    result=[]


    for i in range(N//2):
        result.append(str(list_n[N-1-i]))
        result.append(str(list_n[i]))
        #result.aprint(list_n[i],end=" ")
    print("#{} {}".format(" ".join(result[0:10]))