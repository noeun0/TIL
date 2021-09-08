맨 상위 폴더 아래

static/images 폴더 생성해서 이미지 넣고

settings에 

```python
STATIC_URL = '/static/'
#url로 변경이 일어났을떄 url 경로를 바꾸는 것이다.


STATICFILES_DIRS = [BASE_DIR/'static']
```





사용하고 싶은 html 파일 

```
{% load static %}
```



##### 미디어 경로 변수화 하기

ulrs.py

- settings.py 를 불러와서 static()에 변수화 하기.

```python
urlpatterns = [
   ....
   
] + static (settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT) 
```







실행 순서

장고는 http 요청이 들어왔기 떄문에

urls가 반응한다. 인덱스 함수를 실행

아티클을 가지고 콘텍스트에 담아서 인덱스html을 크롬 브라우저에게 전달

크롬은 사용자에게 보여줄 수 있도록 렌더링 하는 중에

static 경로의 이미지를 찾기 위해 장고에게 요청, 그럼 장고는 이미지를 찾아서 보내고 크롬은 그 페이지를 조립해서 보여준다.



---

### Model Filed

### 이미지 업로드 기능 동작

#### 1. models.py

- `ImageField`
  - 쓰기 위해서 `pip install pillow`
  - 이미지 업로드에서 사용하는 모델 필드

```python
img = models.ImageField()
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



