### 카운팅 정렬

- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
- 각 항복의 발생 회수를 기록하기 위해 정수 항목으로 인덱스 되는 카운트의 배열을 사용하기 때문
- 카운트들을 위한 충분한 공간을 할당하려면 집합내의 가장 큰 정수를 알아야 한다.

- 시간 복잡도 O(n+k) : n은 리스트길이, k는 정수의 최댓값

- n이 비교적 작을때만 가능하다.

1.Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다.

```python
counts=[0]*(k+1) # 데이터 원소의 범위 만큼

data = [9,4,1,3,3,1,3,2,1,3,1,2,3]
for i in range(1,len(data)):
	counts[data[i]]+=1
```

2.정렬된 집합에서 각 항목의 위치를 앞의 요소드를 누적해서 원소를 조정한다

```python
for i in range(1,len(c)):
	count[i] += count[i-1]
	
```

3.counts[n]을 감소시키고 temp에 n을 삽입한다. (counts[n]에 저장된 값의 인덱스에!)

```python
for i in range(len(B)-1,-1,-1):
    count[Data[i]]-=1
    newData[count[Data[i]]]=Data[i]
	#newData[counts[data[i]]-1] = data[i]
	#count[date[i]]-=1
```





### 선택 정렬

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

 
