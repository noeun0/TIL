### SQL과 ORM 문법 비교

>  orm문법을 사용하기 위해`python manage.py shell_plus` 입력하기!



모든 레코드 조회

```shell
#orm
User.objects.all()
User.objects.all().query
```

```sqlite
--sql
SELECT * FROM 
```



user 레코드 생성

```shell
#orm
In [2]: User.objects.create(first_name='길동',
   ...: last_name='홍',
   ...: age=10,
   ...: country='제주',
   ...: phone='010-1234-1234',
   ...: balance=100,
   ...: )
```

```sql
--sql
INSERT INTO users_user      
values (102, '길동', '김', 20, '서울', '010-1234-1234', 100);


```

- 둘다 더 적게 값을 넣을려고 하면 오류난다.



수정하기

```shell
#orm
In [4]: user = User.objects.get(pk=102)

In [5]: user
Out[5]: <User: User object (102)>

In [6]: user.last_name
Out[6]: '김'

In [7]: user.last_name='홍'

In [8]: user.save()

In [9]: user.last_name
Out[9]: '홍'
```

```sql
--sql
sqlite> UPDATE users_user
   ...> SET first_name='철수'
   ...> where id=102;
```



삭제하기

> orm에선 삭제하고 조회하면 오류가 나지만 sql에선 걍 안된다.

```shell
#orm
In [11]: user=User.objects.get(id=102)

In [12]: user.delete()
Out[12]: (1, {'users.User': 1})

```

```sql
--sql
sqlite> DELETE FROM users_user
   ...> WHERE id=101;
   
User.objects.get(pk=1).delete()
```



전체 데이터 갯수 구하기

```shell
#orm
User.objects.count()
len(user.objects.all())
```

```sql
--sql
SELECT count(*) FROM users_user

```



나이가 30인 사람의 성 가져오기

```shell
#orm
User.objects.filter(age=30).values('first_name')
```

```sql
--sql
SELECT first_name FROM users_user
WHERE age=30;

```



나이가 30살 이상인 사람의 명수 가져오기

> orm 에선 lookup사용해야한다

```shell
#orm
#lookup을 사용한다!
User.objects.filter(age__gte=30).count()
```

```sql
--sql
SELECT COUNT(*) FROM users_user
WHERE age>=30
```



나이가 20살 이하인 사람의 명수 가져오기

```shell
#orm
User.objects.filter(age__lte=20).count()
```

```sql
--sql
SELECT COUNT(*) FROM users_user
WHERE age<=20
```



나이가 30이고 성이 김인 사람의 명수 가져오기

```shell
#orm
User.objects.filter(last_name='김',age=30).count()
```

```sql
--sql
SELECT count(*) FROM users_user
WHERE age=30 AND last_name='김';
```



나이가 30이거나 성이 김인 사람의 명수 가져오기

```shell
#orm
User.objects.filter(Q(last_name='김')|Q(age=30)).count()
```

```sql
--sql
SELECT count(*) FROM users_user
WHERE age=30 OR last_name='김';
```



폰번호가 02로 시작하는 사람의 명수 가져오기

```shell
#orm
User.objects.filter(phone__startwith='02').count()
```

```sql
--sql
SELECT COUNT(*) FROM users_user
WHERE phone LIKE '02-%';
```



강원도에 살고 성이 황인 사람의 이름 가져오기

```shell
#orm
USer.objects.filter(country='강원도', last_name='황').values('first_name')

USer.objects.filter(country='강원도', last_name='황').values('first_name').first().get('first_name')
```

```sql
--sql
SELECT first_name FROM users_user
WHERE country='강원도' AND last_name='황'
```



나이가 가장 많은 10명 가져오기

```shell
#orm
User.objects.order_by('-age')[:10]

```

```sql
--sql
SELECT * FROM users_user
ORDER BY age DESC LIMIT 10;
```



잔액이 적은 10명 가져오기

```shell
#orm
User.objects.aggregate(avg_age=Avg('age'))
User.objects.aggregate(Avg('age'))
```

```sql
--sql
SELECT AVG(age) FROM users_user
WHERE last_name='김'
```



강원도 사는 사람의 잔액 평균

```shell
#orm
User.objects.filter(country='강원도').aggregate(Avg('balance'))
```

```sql
--sql
SELECT AVG(balance) FROM users_user
WHERE country='강원도';
```

