# 문자열 메소드

#### 문자열(String)

#####  : 변경할 수 없고(immutable), 순서가 있고(ordered), 순회가능한(iterable)



### 조회 / 탐색

`.find(x)`

- x의 첫번째 위치를 반환한다. 없으면 -1을 반환.



`.index(x)`

- x의 첫번째 위치를 반환한다. 없으면 오류 발생



### 문자열 변경

`.replace(ord,new[,count])`

- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

- count 를 지정하면 해당 갯수만큼 시행한다. 안지정하면 그냥 다

`strip([chars])`

- 특정 문자를 지정하면 양쪽을 제거하거나, 왼쪽 or 오른쪽 제거
- 지정하지 않으면 공백을 제거한다.
- 인자로 받는 chars값의 순서가 상관없다. chars안에 있는 값인지 확인하고 있으면 삭제
- 처음으로 chars안에 없는 값이 나오면 중지

`.split([chars])`

- 문자열을 특정한 단위로 나누어 리스트로 반환.
- split()은 공백을 기준으로 나눈다.

`'separator'.join(iterable)`

- 특정 문자열로 만들어 반환

- 반복가능한 요소를 구분자와 합쳐 문자열로 반환한다.

- int형 리스트는 불가능하므로 map을 사용해서 str로 바꾼 뒤 조인해주면 편하다

  ```python
  ''.join(map(str,list1))
  ```



- `.capitalize()` : 앞글자를 대문자로 만들어 반환.

- `.title()` : '나 공백 이후를 대문자로 만들어 반환.

- `.upper()` : 모두 대문자로 변환 후 반환.

- `.lower()` : 모두 소문자로 변환 후 반환.

- `.swapcase()` : 대 소문자 변경

  

---

# SET 메소드

#### Set 

##### : 변경가능, 순서 없음, 순회 가능

`.add`

- 세트에 요소 추가
- 중복이 불가하므로 같은 값 두번 넣으면 변화 없음
- 원래 객체를 변경해준다.

`.update(*others)`

- 여러 값을 추가한다.
- 반드시 iterable 데이터 구조를 전달해야 한다.

` .remove(elem)`

- elem을 세트에서 삭제, 없으면 KeyError

`.discard(elem)`

- elem을 세트에서 삭제, 없어도 에러가 발생하지 않는다.

`.pop()`

- 임의의 원소를 제거해 반환한다



