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

---

시퀀스형 순서가 있는 데이터

리스트 튜플 레인지 문자형 바이너리

- 형변환

![image-20210719162939622](C:\Users\rey\AppData\Roaming\Typora\typora-user-images\image-20210719162939622.png)

반드시 모두 실행해보기

---

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

![image-20210719164000281](C:\Users\rey\AppData\Roaming\Typora\typora-user-images\image-20210719164000281.png)

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



