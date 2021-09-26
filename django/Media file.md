## Media file

- 사용자가 웹에서 업로드하는 정적 파일
- 유저가 업로드 한 모든 정적 파일



##### Model field

- Imagefield
  - 이미지 업로드에 사용하는 모델 필드
  - FileField를 상속받는 서브 클래스 이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며, 더해서 사용자에 의해 업로드된 객체가 유효한 이미지인지 검사함
  - imageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용해서 최대 길이를 변경 가능하다
  - 사용하려면 Pillow 라이브러리가 필요



- FileField
  - 파일 업로드에 사용하는 모델 필드
  - 2개의 선택 인자를 갖고 있다
    - uload_to
    - strage ( 사용 x )

- upload_to?
  1. 문자열 값이나 경로 지정 ( strftime() 형식 포함 가능 )
  2. 함수 호출

models.py

```python
Class MyModel(Models.model):
# MEDIA_ROOT/uploads/경로로 파일 업로드
upload = models.Filefield(upload_to = 'uploads/')
upload = models.filefield(upload_to = 'uploads/%Y/%M/%d/')
```

---



### 이미지 업로드

#### 📌settings.py

- MEDIA_ROOT, MEDIA_URL 설정해주기

```python
MEDIA_ROOT = BASE_DIR/'media'
```

>  (폴더가 자동으로 생성된다.)

```python
MEDIA_URL = '/media/'
```

> 반드시 url은 /로 끝날것!!, static url과 다르게!!



#### 📌url.py

✨사용자가 업로드 한 파일이 우리 프로젝트에 업로드 되지만, **실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 url이 필요하다**

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> MEDIA_URL, MEDIA_ROOT를 우선적으로 선언해야한다.



ImageField 작성

> 작성 전에 Pillow 설치하자!
>
> `pip install Pillow`
>
> `pip freeze > requirements.txt`
>
> `python manage.py makemigrations`
>
> `python manage.py migrate`
>
> 까지!



#### 📌Models.py

- `upload_to` 속성을 사용해서 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정하자

```python
image=models.ImageField(blank=True, upload_to='images/',)
```



##### Model field option

blank

- 기본값 False
- True 인 경우 필드를 비워 둘 수 있다.
- **유효성 검사**에서 사용된다. 필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있다.

null (X)

- 기본 값 : False
- True면 django는 빈 값을 Null로 저장

- **문자열 기반 필드에는 사용하는 것을 피해야 한다.**
- 문자열 기반 필드는 데이터 없음이 빈 문자열 인데, 데이터 없음에 대해 널값으로 표현하는 걸 추가하게 되면 표현 가능 방법이 중복된다. 

- DB에만 영향을 미친다. -> 특수 경우가 아닌 이상 사용하지 않음.



form 요소 - enctype 속성

- multipart/form-data
  - **파일 / 이미지 업로드 시에 반드시 사용해야 한다.**
  - `<input type='file'>`을 사용할 경우에 사용

#### 📌create.py

- form 안에 enctype 속성을 추가해준다!!

```python
<form ... enctype = 'multipart/form-data'>
```

#### 📌views.py

> request에서 이미지 같은 파일들은 post 형태로 들어오지 않아.... FILES에 들어와...
>
> 받은 데이터에서 post,files 방식 두개로 가져와야됨..

```python
form= ArticleForm(request.POST, request.FILES)
```



input  요소 - accept 속성

- 입력 허용할 파일 유형을 나타내는 문자열
- 쉼표로 구분된 고유파일 유형 지정자
- 파일 검증을 하는 것은 아니다.

```html
<input type='file' accept="video/*" >
```

---



### 업로드 된 파일 가져오기

> 앞의 과정이 우선이 되야함

detail.html

```html
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```



하지만 위의 한줄만 입력했을때, 기존의 이미지를 등록하지 않은 게시글들은 img를 찾을 수 없어 오류가 나게 된다. 그러므로 분기해주자.

```html
{% if article.image %}
	<img src="{{ article.image.url }}" alt="{{ article.image }}">
{% else %}
	<img src="{% static 'images/default.jpg' %}" alt="default image">
	
{% end if %}
```



----

### 이미지 수정하기

- 이미지는 바이너리 데이터 이기 때문에 텍스트 처럼 일부만 수정하는 것은 불가능
- 때문에 새로운 사진으로 덮어 씌우는 방식을 사용



#### 📌update.html

```html
<form ... enctype="multipart/form-data">
```



#### 📌views.py

```python
def update(request,pk):
	...
	form = ArticleForm(request.POST, request.FILES, instance=article)

```









