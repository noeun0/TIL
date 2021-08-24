### 스택

- 후입선출(LIFO, Last In First Out)
- 자료구조 : 자료를 선형으로 저장할 저장소
- 저장소 자체를 스택으로 부르기도 함
- 마지막 삽입된 원소위치를 top이라고 함
- push : append() / pop : pop()
- 파이썬은 스택 자료구조를 따로 제공하지 않는다. 기본 클래스 list를 이용하여 흉내 낼 수 있다.

```
stack = [1,2,3]
stack.append(4)

# 꺼내기
top = stack.pop()

# 꺼내진 않고 확인하기
top = stack[-1]

# 크기 확인
len(stack)+1
```

