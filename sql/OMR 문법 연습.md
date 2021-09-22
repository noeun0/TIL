# workshop

#### 1.

1.

```sql
CREATE TABLE countries(
	room_num TEXT,
	check_in TEXT,
    check_out TEXT,
    grade TEXT,
    price INT
	);

```

2.

```sql
INSERT INTO countries VALUES (202, 2020-01-01, 2020-01-02, suite, 400);
```

3.

```sql
ALTER TABLE countries RENAME TO hotels;
```

4.

```sql
SELECT room_num, price FROM hotels
ORDER BY price DESC LIMIT 2;

```

5.

```sql
SELECT count(*) FROM hotels
GROUP BY grade
ORDER BY count(*) DESC;
```

6.

```sql
SELECT * FROM hotels
WHERE room_num like 'B%' OR grade='suite'
```

7.

```sql
SELECT room_num FROM hotels
WHERE room_num BETWEEN 100 AND 1000 AND check_in='2020-01-04'
ORDER BY price ASC
```



#### 2.

1)

```
users_user.objects.all()
```

2)

```shell
users_user.objects.filter(id=19).values('age')
```

3)

```shell
users_user.objects.all().values('age')
```

4)

```shell
users_user.objects.filter(age__lte=40).values('id','balance')
```

5)

```shell
users_user.objects.filter(balance__gte=500).values('first_name')
```

6)

```shell
users_user.objects.filter(first_name__endswith='수', country='경기도').values(balance)
```

7)

```shell
from django.db.models import Q
users_user.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()
```

8)

```shell
users_user.objects.filter(phone__startswith='010').count()
```

9)

```shell
user = users_user.objects.get(first_name='옥자',last_name='김')
user.country = '경기도'
user.save()
```

10)

```shell
users_user.objects.get(first_name='진호',last_name='백').delete()
```

11)

```shell
users_user.objects.values('first_name','last_name','balance').order_by('balance')[:4]
```

12)

```shell
users_user.objects.filter( age__lte=30, phone__contains='123').values()
```

13)

```shell
users_user.objects.filter(phone__startswith='010').values('country').distinct()
```

14)

```shell
from django.db.models import Avg
users_user.objects.all().aggregate(Avg('age'))
```

15)

```shell
from django.db.models import Avg
users_user.objects.filter(last_name='박').aggregate(Avg('balance'))
```

16)

```shell
from django.db.models import Max
users_user.objects.filter(country='경상북도').aggregate(Max('balance'))
```

17)

```shell
from django.db.models import Max
users_user.objects.filter(country='제주특별자치도').values('balance').order_by('-balance')[:1]
```

