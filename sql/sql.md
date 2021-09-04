# SQL 기본

##### 절차적 / 비절차적 언어

절차적 데이터 조작어 : 어떻게 데이터를 접근하는지 명세 PL/SQL , T-SQL

비절차적 데이터 조작어 : 무슨 데이터를 원하는지 명세 DML

##### Relation Database

- 계층형 : tree

- 네트워크형 : Owner, Menber

- 관계형 : Relation(table)

##### 연산

- 집합 연산 : Union, Difference, Intersect, Cartesion Product
- 관계 연산 : Selection, Projection, Join, Division



### SQL(Structured Query Language)

##### SQL 이란?

- 관계형 데이터 베이스에서 데이터의 구조를 정의, 조작, 제어가 가능한 절차적 언어
- ANSI / ISO표준을 준수하며 DBMS가 바뀌어도 그대로 사용 가능

##### SQL 종류

- DDL :정의 (create, alter, rename, drop )
- DML : 조작 (select, upload, insert, delete)
- DCL : 권한 부여, 회수 (revoke, grant)
- TCL : 트랜젝션 제어 (commit , rollback)

##### SQL 실행 순서

1. passing : 문법 확인 / 구문 분석 / 캐시에 저장
2. execution : 옵티마이저 실행 계획에 SQL 실행
3. fetch : 데이터를 읽고 전송

##### SQL 실행 순서

**FWGHSO**

select c (5)

from t (1)

where c=v (2)

group by c (3)

having c>v (4)

order by c (6)



### DDL

- pk 지정하는 법

```sql
Alter table t add constraint pk_별칭
	primary key(C);
```

```sql
Create table ... ,
	constraint pk_별칭
	Primary key(C);
```



- Create

```sql
Create table(C VARCHAR(10) NOT NULL,default/date/...,
			CONSTRAINT PROD_PK PRIMARY KEY (컬럼명)
```

- Alter

```sql
ALTER table table명 RENAME to table명
					RENAME COLUMN 컬럼명 to 컬럼명
					ADD(추가할 컬럼명)
					MODIFY(바꿀 컬럼)
					DROP COLUMN(삭제할 컬럼)
					add constraint 제약조건명 제약조건(컬럼명)
					DROP 제약조건명
					disable constraint 제약조건 임시 비활성화
					cascade constraint #자식들삭제
```

- Drop (로그 안남음)

```
DROP table table명 (Cascade Constraint)
```



##### 참조 무결성 규정

```sql
C references t(C) on delete cascade;
					set null;
					set default;
					restrict;
C references t(c) on insert Automatic;
					Dependent;
					set null;
					set default;
					
										
```



##### table  탐색 없이 fetch할때 index 생성하기

```sql
creat table t(...) organization index
```



**외래키 특징**

- 테이블 생성시 설정할 수 있다

- 외래키 값은 널 값을 가질 수 있다.

- 한 테이블에 여러개 존재할 수 있다.

- 외래키 값은 참조 무결성 제약을 받을 수 있다.

  

**view**

: 단지 정의만 갖고 있다.

```sql
create view T as select * from T
```

- 장점 : 보안기능, 데이터 관리 쉬움, 여러개 뷰 생성 가능/ 단순화, 독립성, 보안성 상승

- 단점 : 독자적 인덱스 x, 연산의 제약, 구조 변경 x

- 실제 데이터를 저장할 수도 있다.



### DML

insert

```sql
INSERT into T Values V
```

update

```sql
UPDATE T set C="" where
```

select

```sql
Select * from T
```

delete

```sql
Delete from T where
```



##### 테이블 삭제 SQL 비교

- Drop table : Auto Commit / Rollback 불가능

  테이블 정의 자체를 완전히 삭제 로그 x

- Truncate table : Auto Commit / Rollback 불가능

  테이블 초기화 로그 x

- Delete from : 사용자 commit / Rollback 가능

  데이터만 삭제 로그 남음



##### DML 대용량 배지 속도 향상법

- 인덱스 제거하고 나중에 다시 생성
- 수정 가능 조인 뷰나 merge 활용
- insert 구문에서 nologging 사용
- sql 서버라면 최소로깅모드 insert기능 활용



### where

##### where 문의 연산자 

: like/between/in/not/is null/비교연산자

- 집계함수는 사용 불가하다.

  

##### 연산자 우선순위

1. 괄호로 묶은 연산

2. 부정 연산자
3. 비교 연산자, sql비교 연산자
4. 논리 연산자 (and -> or)



##### Null처리함수

- NVL(c,v) : c가 널이면 v 출력 = ISNULL()
- NVL2(c,v1,v2) : 널이 아니면 v1, 널이면 v2
- NULLIF(a,b) : a==b이면 null, 아니면 a
- COALESCE(v1,v2,v3...) : null 이 아닌 최초 표현식

##### count

- count(*) : null값을 포함한 행의 개수 계산 (조건 절이 거짓일떄 0 반환)
- count(C) : null 값을 포함하지 않은 행의 개수 계산



### 함수

built in fuction

- single
  - 문자열 함수 : lower / upper / ascii / char / concat / substr / length / ltrim / rtrim / trim
  - 날짜형 함수 : sysdate / extract
  - 숫자형 함수 : abs / sign / mod / ceil / floor / round / trunc
- multi
  - Aggregate : 집계함수 : count / sum / avg / max / min / stddev / varian
  - Group
  - Window



##### order by

- 날짜형은 가장 최근 날짜부터 정렬
- 컬럼명 대신 alias명이나 컬럼 순서를 나타내는 정수를 혼용하여 사용 가능

##### with ties

```sql
select top(n) with ties c1,c2
from t order by cl
```



### DCL

- grant

```sql
Grant privileges on t to user
	with grant option # 권한을 부여하는 궈한을 부여
	with admin option # 테이블에 대한 모든 권한을 부여
```

- revoke

```sql
Revoke privileges on t from user
```



### TCL

트렌젝션

- 데이터베이스의 작업을 처리하는 논리적 연산 단위, 분리할 수 없는 한개 이상의 데이터 조직

트렌젝션 특징 - 원일고지

- 원자성 : 모두 실행하던지 말던지
- 일관성 : 트랜젝션 실행 전후 내용 동일
- 고립성 : 실행 중 다른 트렌젝션의 영향 x
- 지속성 : 갱신한 db 내용이 영구 저장

트렌젝션의 격리성이 낮은 경우 문제점

- dirty read
- non-Repeatable read
- Phantom read

트렌젝션 구문

```
Begin Transaction
save transaction
	sql 문
	commit or rollback or rollack to 별칭
```



Decode

- decode(c,p,v1,v2)

Case

```sql
searched_case_exprssion:
select c case with c= v1 then v2
	else v3
	end as 별칭 from t
```

```sql
searched_case_expression:
select c case c with v1 then v2
else v3
end as 별칭 from t
```



ROWID

- 실제 데이터를 보관하는 테이블 블록의 주소

1) 오라클 db내에서 데이터를 구분할 수 있는 유일한 값
2) 조회를 원하는 블록을 바로 참조 가능
3) 오브젝트 / 상대파일 / 블록 / 데이터 번호로 구성

WITH

ROLE

- aksgdms dbms사용자에게 개별적으로 많은 권한을 부여하는 번거로움과 어려움을 해소하기 위해 다영한 궈한을 하나의 ㄱ그룹으로 묶은 논리적 권한의 그룹