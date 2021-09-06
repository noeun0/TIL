# SQL 활용

**순수 관계 연산자**

- select
- project
- join
- devide



### join

- 일반적으로 PK나 FK값의 연관성에 의해 성립
- EQUL join은 =연산자에 의해 수행되며 그외에 비교 연산자를 사용하는 경우는 non EQUI join
- 대부분 non EQUI join 을 수행할 수 있지만 설계상의 이유로 수행이 불가능한 경우도 존재



#### INNER JOIN

- on 구를 사용하여 테이블을 연결
- EQUI, NON EQUI 로 구성된다.



**EQUI join** 

- 해쉬 조인에 사용

```sql
Select * from t1, t2 where t1.c = t2.c
```



**ANSL 표준 join**

```sql
Select * from t1 inner join t2
				left outer join
				right outer join
				full outer join
				
		on t1.c = c2.2 ;
		using c
```



#### OUTER JOIN

- 두 테이블 간 교집합을 조회하고 한쪽 테이블에만 있는 데이터도 포함시켜서 조회한다.
- 왼쪽 테이블에만 있는 행을 포함하면 left outer join , 오른쪽 테이블의 행만 포함시키면 right outer join 이다.
- fill outer join 은 모두 사용하는 것!!
- 오라클 DB에선 (+)기호를 사용해서 할 수 있음



**left outer join**

- 기준 반대의 테이블 즉 inner 구문에 (+)붙히기
- ansi로 바꾸려면 inner 구문 즉 (+)가 붙은 부분을 on에 넣어주자.

```
select s.name , p.name , dname 
  from student s, professor p, department d
 where s.profno=p.profno(+),
   and p.deptno=d.deptno(+); 
```



**full outer join**

```sql
select * from Table1 A, Table2 B
where A.col(+) = B.col
AND A.col(+) = 값1
AND B.col = 값2
UNION ALL
select * from Table1 A, Table2 B
where A.col = B.col(+)
AND A.col = 값1
AND B.col = 값2(+)

```



**CARTESION PRODUCT**

- 테이블 조인 조건이 없는 경우 모든 데이터를 조합하는 조인
- M*N건 발생
- COSS JOIN 사용!!

```
select * from t cross join t2
```



**UNION (중복 x)  /  UNION ALL (중복 O)**

- 두 테이블의 칼럼 수, 칼럼의 데이터 형식 모두가 일치해야 한다.
-  UNION은 두 테이블을 하나로 합치면서 중복된 데이터를 제거한다,
  - 그 과정에서 정렬을 발생

```sql
select * from t1 Union select * from t2
				 Union all # 이걸 사용하는 경우 별칭은 첫번째 select 절의 별칭
```



**INTERSECTION **

- 두 테이블에서 교집합을 조회한다
- 즉 두 테이블에서 공통된 값 조회



**DIFFERENCE**

EXCEPT (server) / MINUS (oracle)

= not in (널이 포함되면 행 선택 안됨), not exists (널이 포함된 채로 행 선택 됨)



**Self Join**

한 테이블 내에 두개의 칼럼이 연관 관계를 갖고 있는 경우 동일 테이블 사이의 조인

칼럼명이 겹치기 떄문에 별칭 사용한다.



**Natural join**

- inner join의 하위 개념. 두 테이블 간의 동일한 이름을 갖는 모든 컬럼들에대해 equi 조인을 수행
- where 절에 조인 조건 추가 x
- 별칭 사용 금지

```
select deptno from emp noatural join dept
```



### 계층형 질의

- 계층형 질의는 테이블에 계층형 데이터가 존재하는 경우 데이터를 조회하기 위해 사용

- 엔티티를 순환관계 데이터 모델로 설계할 경우 계층형 데이터가 발생

##### 용어

- 노드 : 계층 구조 상의 항목
- 루트 : 최 상단 노드 레벨1
- 부모 : 두 노드 관계에서 상위
- 자식 : 두 노드 관계에서 하위
- 리프 : 최하위 노드 

##### 계층형 질의

LEVEL : 루트 데이터를 1로 시작하여 하위로 내려갈수록 리프까지 1씩 증가

CONNECT_BY_ISLEAF : 리프데이터면 1, 그렇지 않으면 0

CONNECT_BY_ISCYCLE : 자식을 갖는데, 해당 데이터가 조상으로서 존재하면 1, 그렇지 않으면 0



##### START WITH ~ CONNECT BY 절

START WITH : 계층 구조 저낵의 시작 위치 지정

CONNECT BY : 다음에 전개될 지식 데이터를 지정

```
START WITH '수도권매장'
CONNECT BY '수도권매장'>'경기남부매장'
```



**PRIOR**

현재 읽을 칼럼 지정

- **PRIOR 자식** = 부모 : 부모 -> 자식 **순방향**

- PRIOR 부모 = 자식 : 자식 -> 부모 역방향

**NOCYCLE** 

: 동일 데이터가 다시 나타나면 사이클이 생겨서 오류 발생, NOCYCLE 추가하면 이후의 데이터 전개하지 않음

**ORDER SIBLINGS BY**

 : 레벨이 같은 형제 노드에서 정렬 수행

**WHERE**

 : 모든 전개를 다 하고 나서 조건을 만족하는 데이터 추출



### 서브쿼리

- select 문 내에서 다시 select 문을 사용하는 sql문이다.

- 괄호로 감싸서 사용

- 서브쿼리 안에 order by 불가



##### 실행결과의 형태에 따라 나뉨

- single row : 실행 결과가 1건 이하
- multi row : 실행 결과가 여러건
- mulit column : 실행 결과가 여러 컬럼



##### Inline View

- from 절에 사용되는 서브쿼리
- == Dymamic view
- 동적인 것처럼 사용되고 저장은 안된다.

**Scala view**

- select 문에서 사용되는 서브쿼리



##### 특징

- 서브쿼리는 select, from, having, order by 절에서 쓰인다.

- 연관 서브쿼리는 서브 쿼리가 메인 쿼리 컬럼을 포함하는 형태
- 단일행 복수행 비교연산자와 사용
- 복수행을 반환하는 경우 in, all, any 등의 비교연산자를 사용
- 다중 컬럼 서브쿼리는 여러개의 컬럼이 반환 / 오라클에서만 지원
- 연관 서브쿼리는 서브쿼리가 메인을 포함



| 프로시저              | 트리거                   |
| --------------------- | ------------------------ |
| create 사용           | create 사용              |
| excute 실행           | 자동 실행                |
| commit, rollback 가능 | commit, rollback 불 가능 |



### View

##### 뷰 특징

- 독립성 : 테이블 구조가 변경되어도 뷰를 사용하는 프로그램은 변하지 않는다.
- 편리성 : 복잡한 질의를 단순하게 작성 가능하다
- 보완성 : 숨기고 싶은 정보를 감출 수 있다. 
- 단지 정의만 갖고 있다.
- 실제 데이터를 저장할 수도 있다.

```sql
create view v as (Select* from t)
```



### GROUPING FUNCTION

##### Rollup

- 실행되는 칼럼 순서대로 subtotal을 만들고, 전체 합계도 조회됨

##### Grouping sets

- 칼럼 순서에 상관 없이 개별적으로 합계 만듬

##### cube

- 결합 가능한 모든 집계를 계산

##### grouping

- grouping 함수 들이 합계 및 소계를 계산하면 그 결과를 구분
- 성공적 계산시(합계) ->1 그렇지 않으면 ->0



### WINDOW FUNCTION

**윈도우 함수 설명**

- partition 과 group by 구문은 의미적으로 유사
- partition 구문이 없으면 전체 집합을 하나의 partition으로 정의하는 것과 동일
- 결과 건수가 줄어드는 것은 아니다
- 윈도우 함수 적용 범위는 partition을 넘을 수 없다.

**구조**

```sql
select window_function(a) over # 집계 / 순위 / 행 순서 / 비율
		(patition by C
		order by C
		windowing 절) from t; # rows / range/between and / 
							# unbounded preceding(following)/
							# current row
```

**집계함수**

Sum / AVG / COUNT / MAX / MIN

**순위함수**

RANK : 동일 순서에 동일한 값

DENSE_RANK : 동일한 순위를 하나의 건수

ROW_NUMBER : 고유한 순위 부여

**행 순서 함수**

FIRST_VALUE : 파티션 내에서 가장 처음 나온 값 (min)

LAST_VALUE : 파티션 내에서 가장 마지막 값 (max)

LAG : 이전 행을 가지고 옴

LEAD(N) : 앞의 n번째 행을 갖고 옴

**비율 함수**

CUME_DIST : 누적 백분률을 조회

PERCENT_RANK : 파티션 내의 행 순서별 백분율 조회

NTILE : 전체 건수를 주어진 컬럼 값 기준으로 n 등분 하여 순위 부여

RATIO_TO_REPORT : sum(c)에 대한 행별 컬럼 값의 백분률 조회



