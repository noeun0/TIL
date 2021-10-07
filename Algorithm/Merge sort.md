### Merge sort

- 존 폰 노이만 이라는 사람이 제안한 방식
- 일반적 방법으로 구현했을때 안정 정렬에 속하며 분할 정복 알고리즘의 하나이다.



병합 정렬

- 여러개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
- 시간 복잡도 O(n log n)
- top - down 방식
- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄



로직

- 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않다면

- 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.

- 각 부분의 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.

- 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

  

합병 알고리즘의 구체적인 개념

- 하나의 리스트를 두개의 윤등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두개의 정렬된 부분 리스트를 합해서 전체가 정렬된 리스트가 되게 하는 방법



- 크게 세가지 단계로 이루어짐

  - 분할 : 입력 배열들을 같은 크기의 2개의 부분 배열로 분할
  - 정복 : 부분 배열을 정렬 . 부분 배열의 크기가 충분히 작지 않다면 순환 호출을 이용해서 다시 분할 정복
  - 결합 : 정렬된 부분 배열들을 하나의 배열에 합병

  

- 합병 정렬의 과정

  - 추가적인 리스트가 필요하다
  - 각 부분 배열을 정렬할 때도 합병 정렬을 순환적으로 호출해서 적용
  - 합병 정렬에서 실제 정렬이 이루어지는 시점은 합병하는 단계!



한번에 구현한 코드

```python
def merge(arr):
    global count
    # 크기가 1보다 작거나 같으면 멈추고
    if len(arr)<=1:
        return
    mid = len(arr)//2
    leftgroup = arr[:mid]
    rightgroup = arr[mid:]

    merge(leftgroup)
    merge(rightgroup)

    # 여기부터 진행
    l_idx,r_idx,now = 0,0,0
    while l_idx < len(leftgroup) and r_idx < len(rightgroup):
        if leftgroup[l_idx] <= rightgroup[r_idx]:
            arr[now] = leftgroup[l_idx]
            l_idx += 1
            now += 1
        else:
            arr[now] = rightgroup[r_idx]
            r_idx += 1
            now += 1

    while l_idx < len(leftgroup):
        arr[now] =leftgroup[l_idx]
        l_idx += 1
        now += 1

    while r_idx < len(rightgroup):
        arr[now] = rightgroup[r_idx]
        r_idx += 1
        now += 1
```

