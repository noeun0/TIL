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

