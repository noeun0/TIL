import sys
sys.stdin = open("input.txt")
for tc in range(1,int(input())+1):
    N,K = map(int,input().split(" "))
    list_n=[x+1 for x in range(12)]
    #print(list_n)
    count=0
    for i in range(1<<len(list_n)):
        result = 0
        num_count=0
        for j in range(len(list_n)):
            if i & (1<<j):
                result+=list_n[j]
                num_count+=1
        if result ==K and num_count ==N:
            count+=1
    print("#{} {}".format(tc,count))
