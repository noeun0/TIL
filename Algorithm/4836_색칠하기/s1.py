import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    list_p=[[0]*10 for _ in range(10)]
    for _ in range(int(input())):
        si,sj,ei,ej,color=map(int,input().split(" "))
        for i in range(si,ei+1):
            for j in range(sj,ej+1):
                list_p[i][j]+=color
    count=0
    #print(list_p)
    for p_i in range(len(list_p)):
        for p_j in range(len(list_p[p_i])):
            if list_p[p_i][p_j]==3:
                count+=1
    print("#{} {}".format(tc, count))