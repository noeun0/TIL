import sys
sys.stdin = open("input.txt")
for tc in range(1,int(input())+1):
    page,pa,pb = map(int,input().split(" "))
    count_a=0
    count_b=0

    start = 1
    end = page

    while start<=end:
        mid = (start + end) // 2
        count_a+=1
        if mid ==pa:
            break
        elif pa<mid:
            end=mid

        else:
            start=mid

    start = 1
    end = page
    while start<=end:
        mid = (start + end) // 2
        count_b+=1
        if mid ==pb:
            break
        elif pb<mid:
            end=mid
        else:
            start=mid

    #print(count_a,count_b)
    if count_a>count_b:
        print("#{} B".format(tc))
    elif count_a<count_b:
        print("#{} A".format(tc))
    else:
        print("#{} 0".format(tc))