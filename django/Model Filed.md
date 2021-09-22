### Model

- 단일한 데이터에 대한 정보를 갖음
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들 포함
- 저장된 데이터 베이스 구조
- model을 통해 뎅터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨

> 모델과 데이터베이스는 다른 존재이다.





### 이미지 파일 업로드 하기

맨 상위 폴더 아래

static/images 폴더 생성해서 이미지 넣고

*settings.py*

```python
STATIC_URL = '/static/'
#url로 변경이 일어났을떄 url 경로를 바꾸는 것이다.


STATICFILES_DIRS = [BASE_DIR/'static']
```



*사용하고 싶은 html 파일* 

```
{% load static %}
```



### 미디어 경로 설정, 변수화 하기

*settings.py*

```python
MEDIA_URL = '/media/' # 경로의 이름 / url을 어떻게 구성할지?
MEDIA_ROOT = BASE_DIR / 'media' #실제 파일이 저장되는 공간
```

*ulrs.py*

- settings.py 를 불러와서 static()에 변수화 하기.

- `from django.conf.urls.static import static`

  `from django.conf import settings`

```python
urlpatterns = [
   ....
   
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
```



*사용할 html*

```
{{ article.image.url }}

```



---

### Model Filed

### 이미지 업로드 기능 동작

#### 1. models.py

- `ImageField`
  - 쓰기 위해서 `pip install pillow`
  - 이미지 업로드에서 사용하는 모델 필드

```python
image = models.ImageField(upload_to='images/')
```



-> 아래와 같이 이미지 입력 폼이 생김

![image-20210908130504732](C:\Users\rey\Documents\GitHub\TIL\django\img\image-20210908130504732.png)

(속성 brank : TRUE -> 빈 값을 줄 수 없게 설정)



#### 2. form.html

- 사진을 보내거나 받는 서비스라면 다른 형식의 파일을 넣을 예정이라고 기입해주어야한다.

  form 속성에 `enctype="mutipart/form-data"`

```html
    <form action = "" method = "POST" class="col-4 offset-4" enctype="mutipart/form-data">
        {% csrf_token %} 
        
        {% bootstrap_form form %}
        ...
```



#### 3. views.py

- 유효성 테스트에서 `is_valied`에서 통과하지 못한다.
- 이미지는 files로 들어오기 때문에 `articleform`에 `request.FILES`를 추가해주어야한다.

```
form = ArticleForm(request.POST, request.FILES)
```



#### 실행 순서

장고는 http 요청이 들어왔기 떄문에 우선 urls가 반응한다. 인덱스 함수를 실행

아티클을 가지고 콘텍스트에 담아서 인덱스html을 크롬 브라우저에게 전달

크롬은 사용자에게 보여줄 수 있도록 렌더링 하는 중에

static 경로의 이미지를 찾기 위해 장고에게 요청, 그럼 장고는 이미지를 찾아서 보내고 크롬은 그 페이지를 조립해서 보여준다.