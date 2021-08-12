import sys
sys.stdin = open("input.txt")

for _ in range(10):
    N = int(input())
    list_l = [list(map(int, input().split())) for _ in range(100)]
    nx = 99
    for i in range(100):
        if list_l[99][i] ==2:
            ny = i


    #print(nx,ny)
    while nx > 0:
        list_l[nx][ny] = 3
        if ny - 1 in range(100) and list_l[nx][ny-1] == 1:  # 왼쪽으로 갈 수 있다면
            ny -= 1
        elif ny + 1 in range(100) and list_l[nx][ny+1] == 1:
            ny += 1
        else:
            nx -= 1
    print("#{} {}".format(N,ny))