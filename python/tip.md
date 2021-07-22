# 파이썬 tip

> 새로 알게된 것들



### 딕셔너리

1. key값 가져오는 법

```python
dict.keys()
```

2. key값과 value값 같이 사용하기

```python
for key,value in dict.items():
	print(key,value)
```

3. key값과 value 값을 리스트에 넣을 수도 있다.

```python
list1 = list(dict.items())
list2 = list(dict.keys())
list3 = list(dict.values())
```



##### enumerate

- items를 보니 리스트의 enumerate가 생각나서 정리.

- enumerate(seq,start=0)

- seq : sequence_type_object로 string, tuple, range() 등이 있다

- start : default =0

  ​	값 지정시 start값 부터 index 시작

```python
for idx,i in enumerate(list1,start =1):
	print(idx,i)
```





### 복소수

- a+bi 꼴로 실수와 허수의 합으로 이루어지는 수.

- 복소수의 크기는 복소 평면에 플로팅된 원점에서 복소수 값까지의 벡터 길이

- (a^2+b^2)^1/2 와 같다.

- type(x) == complex

- 복소수는 값을 비교할 수 없다.

- 실수부와 허수부를 사용하려면? real, imag를 사용하면 된다

  

- 복소수의 크기 구하기

```python
x= (x.real**2 + x.imag**2)**(1/2)
```







# 더 간단하게

###### if a== True? a != False?

```python
if a:
```

###### if a== False? a != True?

```python
if not a:
```



​     