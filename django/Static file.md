## Static file

- 정적 파일
- 응답할때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 일반적으로 이미지, 자바스크립트, css와 같은 미리 준비된 파일
- django에서는 static file이라고 한다.



Static file 구성

- ` django.contrib.staticfiles`가 INSTALLED_APPS에 포함되어 있는지 확인 (이미 있다.)
- seetings.py에 `STATIC_URL`을 정의 ( 이미 있다.)
- 템플릿에서 static 템플릿 테그를 사용해서 지정된 상대경로에 대한 url 빌드

```html
{% load static %}
< img src = "{% static 'my_app/example.jpg' %} alt="my img" >

```



##### Django template tag

- `load`

  - 사용자 정의 템플릿 태그 세트를 로드
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드
  - 장고를 로드할때도 똑같히 썼었다....`{% load bootstrap5 %}`

- `static`

  - STATIC_ROOT에 저장된 정적 파일에 연결

  - 해당 파일의 경로, 이름명을 기입해줌

    

##### The staticfiles app

- `STATIC_ROOT`

  - collectstatic이 배포를 위해 정적 파일을 수집하는 **디렉토리의 절대 경로**
  - django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 놓는 경로
  - 개발 과정에서 settings.py의 DEBUG값이 True로 설정되어 있으면 해당 값을 작용되지 않는다. 그러므로 작성해주어야 함!!
  - 실 서비스 환경에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함
  - settings.py

  ```html
  STATIC_ROOT = BASE_DIR/'staticfiles'
  ```

  ```bash
  $ python manage.py collectstatic
  #사용하고 있던 정적 파일들이 다 모아진다.
  ```

  -> 위의 과정은 실제 배포할떄만 사용하자!!



- `STATIC_URL`
  - STATIC_ROOT에 있는 정적 파일을 참조할 떄 사용할 url
  - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/경로 및  **STATICFILES_DIRS**에 정의된 추가 경로들을 탐색
  - **실제 파일 디렉토리가 아니며,  url로만 존재**
  - 비어있지 않은 값으로 설정한다면 반드시 /로 끝낼것!!





---

### 실습

articles에 static/articles폴더 만들어줌

articles/ static/articles에 이미지 넣어줌

```html
{% load static %} #extends아래

<img src="{% static 'articles/sample.png' %}" art="sample">
```

>  STATIC_URL은 전제 쓰이나? 웹에서 보기 위해 우리가 요청할 주소를 만들어준다. 이미지에도 주소값을 할당해준다. 



실습2 - 추가경로의 이미지 사용하기

최상단에 static/images폴더 만들기

static/images/안에 이미지 넣기

base.html에 넣어보기



settings.py에서 추가경로 넣기

```python
STATICFILES_DIR =[
	BASE_DIR / 'static',
]
```

```html
{% load static %} #extends아래

<img src="{% static 'images/sample.png' %}" art="sample">
```





---

##### Media file

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









