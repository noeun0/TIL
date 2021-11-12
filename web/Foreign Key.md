## Foreign Key 

### Foreign Key 개념

- 외래키
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 외래키는 참조하는 테이블에서 1 개의 키에 해당하고, 이는 참조되는 측 테이블의 **기본키**를 가리킴
- 참조하는 테이블의 행 1개의 값은 참조되는 측 테이블의 행 값에 대응됨
- 반드시 기본키일 필요는 없지만 유일한 값이어야 함
- 참조하는 테이블의 행 여러개가 참조되는 테이블의 동일한 행을 참조할 수 있음

참조무결성

- 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
- 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본키 값으로 존재해야함

### 장고에서의 외래키

#### : ForeignKey filed 를사용한다!

- A many - to - one relationship

- 2개의 위치 인자가 반드시 필요

  - 참조하는 model class
  - on_delete 옵션
    - 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할지 정의
    - 데이터 무결성을 위한 중요한 결정
    - 옵션
      - CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제

- 추가옵션 

  - **related_name**='comments'

    : 역참조시 사용할 이름을 변결할 수 있는 옵션

    위와 같이 입력하면 article.comment_set -> article.comments 로 사용할 수 있다.

    migration 과정 필요

    

- migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름을 만듦

> 데이터 무결성
>
> - 데이터의 정확성과 일관성을 유지하고 보증하는 것을 가리킴
>
> - 데이터베이스나 RDBMS 시스템의 중요한 기능



models.py

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_Delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at
    updated_at
    
    def __str__(self):
        return self.content
    
```

-> 장고는 지정한 외래키 명에 id를 붙혀서 외래키를 생성한다! ( article_id )

: 하지만 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)으로 작성하는 것이 바람직하다. (1:N)



### 1:N 관계 related manager

- 역참조 ( 'comment_set')

  - Article(1) -> Comment(N)
  - article.comment 형태로는 사용될 수 없고, **article.comment_set manager**가 생성됨
  - 게시글에 몇개의 댓글이 작성되었는지 Django ORM이 보장할 수 없기 때문
  - article은 comment가 있을 수도 있고, 없을 수도 있음
  - 실제로 Article 클래스에는 Comment 와의 어떠한 관계도 작성되어 있지 않음

- 참조 ('article')

  - Comment(N) -> Article(1)

  - 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로,

    **comment.article**과 같이 접근할 수 있음

    

```
article.comment_set.all()
```

```
comments = article.comment_set.all()
for comment in comments:
print(comment.content)
```











