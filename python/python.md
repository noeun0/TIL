# python

- 인터프리터 언어

  - 소스 코드를 컴파일 하지 않고 한주씩 읽어서 실행

  - 컴파일 언어에 비해 느릴 수 있지만 빌드 과정 없이 바로 실행

    (반대 = 컴파일러 언어)

- 동적 실행 언어

  - 변수에 별도의 타입 지정이 필요 없음

- 객체 지향 프로그래밍

  - 파이썬은 모두 객체로 이루어져있다.

- 대화형 환경

  - 기본 interpreter
  - jupyter notebook

- 스크립트 환경

  - .py 파일을 작성하고 IDE 혹은 Text editor 활용

    기본적으로 활용 가능하나 디버깅 및 코드 편집 반복 실행이 어렵다

    대화형 모드로 동작한다

##### 주석

ctrl + /

- 한줄 주석은 #
- "", ''' 로 표현하는 방법은 docstring 을 위해 사용하기도 한다.
  - docstring : 함수/클래스의 설명을 작성



**변수**

할당 연산자 (Assignment Operator)

`=`

- 변수는 `=`를 통해 할당 된다.
- `type()`을 활용해서 데이터 타입을 확인 할 수 있다.
- `id`()를 활용하여 해당 값의 메모리 주소를 확인할 수 있다.
- 같은 값을 동시에 할당 가능
- 다른 값을 동시에 할당 가능



**식별자**

변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름.

- 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성

- 첫 글자에 숫자가 올 수 없다.

- 길이의 제한이 없다.

- 대소문자 구별

- 예약어는 사용될 수 없음

- 내장함수나 모듈 등의 이름으로 만들면 안됨

  ```
  False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

  > import keyword
  > print(keyword.kwlist) 를 통해 불가능한 키워드 들을 확인할 수 있음

  

**데이터 타입**

- 숫자, 문자, 참거짓

`int`

- 모든 정수는 `int`로 표현
- 파이썬엔 `long`이 없음
- 8진수 : `0o` / 2진수 : `0b` / 16진수: `0x` 

파이썬에서 표현할 수 있는 최대 숫자?

- 파이썬은 정수 자료형에 오버플로가 X
- 읨의 정밀도 산술을 표현하기 때문 -> 유동적으로 바이트 수를 조절하며 사용



`float`

- 실수

- 부동 소수점을 사용하기 때문에 항상 같은 값으로 일치하지 않음

- `==`으로 비교할 수 없음.. 

  - -> abs로 절댓값을 만들어서 1e-10 랑 비교하자.. 작으면 같은것
  - -> abs 로 절댓값을 만들어서 sys.float_info.epsilon이랑 비교하자... 작으면 같은 것
  - import math
    math.isclose(a, b)를 사용할 수도 있다..

  ```
  a = 3.5 - 3.12
  b = 0.38
  
  abs(a - b) <= 1e-10
  ```

  

- 사직연산도 제대로 안됨.. 반올림 해서 사용하도록 하자

  ```
  round(3.5 - 3.12, 2)
  -> 0.38
  ```

`complex`

- 각각 실수로 표현되는 실수부와 허수부를 가진다.
- 복소수는 허수부가 j
- 실수부는 : / 허수부는 : 



### String interpolation



- `%-formatting`

  - `%d` : 정수
  - `%f` : 실수
  - `%s` : 문자열

  ```python
  print('hello %s' % name)
  print('score is %d' % score)
  print('score is %f' % score)
  ```

- `str.format()` 

  ```python
  print('hello {}'.format(name))
  print('hello {} {}'.format(name, score))	
  ```

- `f-strings`: 

  ```python
  print(f'hello {name} {score}')
  ```

  ```python
  pi = 3.141592
  print(f'{pi:.3}')
  print(f'{pi*3:.4}')
  # 출력 형식 지정도 가능
  ```

  

**표현식**

- 하나의 값으로 환원 될 수 있는 문장을 의미
- 식별자, 값, 연산자로 구성
- 표현식을 만드는 문법은 일반적인 수식의 규칙과 유사

**문장**

- 파이썬이 실행가능한 최소한의 코드 단위
- 하나의 값도 문장이 될 수 있다
- 표현식도 문장이 될 수 있다



**문장안에 표현식이 포함된다.**



---



시퀀스형 순서가 있는 데이터

리스트 튜플 레인지 문자형 바이너리

- 형변환

반드시 모두 실행해보기



변경 불가능한 데이터(immutable)

- 리터럴- 숫자, 문자열, 참/거짓
- range
- tuple



변경 가능한 데이터(mutable)

- list
- set
- doctionary

---

##### 컨테이너 분류

순서가 있는 것 (sequence)

>  for문 사용 가능!

- string 
- list 
- tuple 
- range

순서가 없는 것 

>  값이 있는지 확인하거나, 값을 활용해서 데이터를 꺼낸다거나

- set  
- dictionary

---

##### 딕셔너리 값 가져오는 법

```\
students['phone']
```

- 값이 없으면 에러가 난다

```
students.get('phone')
```

- 값이 없으면 None을 출력한다

> 2번째 방법을 주로 사용한다.

---

##### enumerate

> (index, value) 형태의 tuple로 구성된 열거 객체를 반환해준다.

```python
greetings=['하이','hello']
for greeting in enumerate(greetings):
	print(greeting)
```

```python
greetings = eumerate(['하이','hello'])
for index, greeting in greetings:
	print(greeting)
```

- 변수를 다르게 주어서 사용할 수 있다.

---

###### 반복문 제어 -break

- break : 반복문을 종료
- continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- for-else : 끝까지 반복문을 실행한 이후에 else 문 실행
  - break

---



