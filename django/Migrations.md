## Migrations

> django가 model에 생긴 변화를 DB에 반영하는 방법



`makemigrations`

: model을 변경한 것에 기반한 새로운 마이그레이션을 만들때 사용

```
python manage.py makemigrations
```



`migrate`

: 마이그레이션을 DB에 반영하기 위해 사용

설계도를 실제 DB에 반영하는 과정

모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

``` 
python manage.py migrate
```

-> 첫 마이그레이트 시에 기존에 내장되있는 기본 앱들의 설계도 들도 함께 반영된다.



`sqlmigrate`

: 해당 설계도가 sql문으로 어떻게 해석되어서 동작할지 미리 확인 가능

```
python manage.py sqlmigrate articles 0001
```



`showmigrations`

: 해당 설계도가 migrate 됐는지 안됐는지 여부를 확인할 수 있음



### DateField's options

`auto_now_add`

: 최초 생성 일자

- django ORM이 최초 insert시에만 현재 날짜와 시간으로 갱신

`auto_now`

: 최초 수정 일자

- django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신













sqlmigrate

showmigrations

