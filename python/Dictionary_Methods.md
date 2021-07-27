# Python Dictionary Methods



Removes all elements from the dictionary

```
.Clear()
```



Returns a copy of the dictionary

```
.Copy()
```



Returns a dictionary with the specified keys and value

```python
.fromkeys()

dict.fromkeys(list_key,['a'])
# list_key에 있는 값들을 키값으로 하고, 모든 value값을 a로 하는 딕셔너리를 만들어준다

list(dict.fromkeys(list_key))
# 키값으로 구성된 리스트를 만들어준다.
# 위 코드는 중복을 제거하되, 순서는 유지하려는 경우 사용된다.
```



- 기존의 딕셔너리를 변경하지 않는다? 주로 위의 경우에 사용하는 듯

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

list1 = ['one','two']
car.fromkeys(list1,['zero'])
print(car)
# 를 하면 기존의 car 딕셔너리가 변함없이 출력된다...
```



Returns the value of the specified key

```
.get()
```



Returns a list containing a tuple for each key value pair

```
.items()
```



Returns a list containing the dictionary's keys

```
.keys()
```



Removes the element with the specified key

```
.pop()
```



Removes the last inserted key-value pair

```python
.popitem() # 맨 나중에 추가된 값 삭제!!
```



Returns the value of the specified key. If the key does exist: insert the key, with the specified value

- 딕셔너리 자료형에 없는 키로 접근하면 오류가 발생된다. 이런 keyError를 발생시키지 않고 단순히 키를 조회하는 경우라면 get 메소드를 사용하면 없는 키의 반환은 None이거나 default가 된다. 또한 필요에 따라 단순히 조회뿐만 아니라 없는 키의 경우, 값을 부여해 줄 수 있는 setdefault함수가 존재한다.

```python
.setdefault(a,defalult)
#setdefault()메소드는 키 a가 딕셔너리에 있으면 dict[a]값을 반환하고
#아니면 dict[a]=default를 설정한 후 default를 다시 반환한다.

```

 

Updates the dictionary with the specified key-value pairs

- 딕셔너리 형태의 파일을 더해줄때 사용된다.

```
.update()
```



Returns a list of all the values in the dictionary

```
.values()
```



---

##### point!!

- fromkeys를 사용하여 중복을 제거하는 방법
- 딕셔너리에 오류없이 특정 값이 있으면 그냥 유지하고 없으면 추가해주는 방법

