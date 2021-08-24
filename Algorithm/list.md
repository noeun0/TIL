# 2차원 배열

- 1차원 리스트를 묶어놓은 리스트
- 2차원 이상의 다차원 리스트는 차원에 따라 인덱스를 선언
- 2차원 리스트 선언 : 세로길이 (행) 가로길이(열)
- python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능
- 오른쪽 아래로 값이 증가한다...



행 우선 순위

```python
for i in range(len(list1)):
	for j in range(len(list1[i])):
		list1[i][j]
```

열 우선 순회

```
for j in range(len(list1[0])):
	for i in range(len(list1)):
		list1[i][j]
```

지그재그 순회

```
for i in range(len(list1)):
	for j in range(len(list1[0])):
		list1[i][j+(m-1-2*j)*(i%2)]
```



# 이진 탐색

- 데이터 양이 방대할떄, 정렬이 돼 있을때 사용한다.
- 반복문 or 재귀 함수를 사용한다.



1.반복문 사용

```python
while start<=end:
	mid = (start+end) //2
	if a[mid]==key:
		return mid
	elif a[mind]<key:
		start =mid+1
	else:
		end= mid-1
return -1
```

2.재귀함수 사용

```
def binarySearch(a,low,high,key):
	if low > high:
		return False
	else:
	mid = (low+high)//2
	if key ==a[mid]
		return True
	elif key < a[mid]:
		return binarySearch(a,low,mid-1,key)
	else:
		return binarySearch(a,low+1,mid,key)
		
```



# 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 셀렉션 알고리즘을 전체 자료에 적용한 것
- 진행 할 수록 구간의 시작이 1씩 줄어든다. 버블은 진행할 수록 구간의 끝이 줄어들었다. 
- 교환의 회수가 버블, 삽입 정렬보다 작다.
- 버블정렬, 선택 정렬 모두 평균 수행시간 & 최악 수행시간 =O(n^2)

**동작 과정**

1.주어진 리스트 중에서 최소값을 찾음

2.그 값을 리스트의 맨 앞에 위치한 값과 교환

3.맨처음 위치를 제외한 나머지를 대상으로 위의 과정 반복



```python
for minidx in range(0,n-1):
    for i in range(minidx+1,n):
        if a[i]<a[mindix]:
            a[i],a[minidx]=a[minidx],a[i]
```

 

# 셀렉션 알고리즘

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 알고리즘
- 1번 부터 k 번쨰까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k 번째를 반환
- k가 비교적 작을때 유용 O(kn)의 수행시간

```python
# 선택 정렬과 비슷하지만, mindindex의 범위가 k까지로 정해짐

for minindex in range(0,k):
	for i in range(minindex,n):
		if a[i] < a[minindex]:
			a[minindex],a[i]=a[i],a[minindex]
    return a[k-1]
    
  
```



# 비트연산

##### & : 둘다 1이여야 1! 하나라도 0이면 0!

 : 특정 비트를 0 으로 만들때 사용한다. 0으로 만들고 싶은것만 0으로 하면, 나머지는 고대로 지만 0으로 만들고 싶은 값에 0 을 연산하면 무조건 0이 되므로!

##### | :  둘다 0 이여야 0! 하나라도 1 이면 1

 : 특정 비트를 1으로 만들고 싶을떄 사용. 1로 만들고 싶은 것만 1을 연산해주면 무조건 1이 되므로!

##### ^ : 두개가 다르면 1



**1<<n**: n번 비트가 1인 값 ==2**n



### 달팽이 순환

```python
di = [0,1,0,-1]
dj = [1,0,-1,0]

cnt = 1
i,j = 0,-1
while cnt<=n*n:
    ni,nj = i+di[k], j+dj[k]
    if ni,nj 유효 & a[ni][nj] ==0
    	a[ni][nj]=cnt
      	cnt+=1
        i,j = ni,nj
    else
    	k=(k+1)%4

```