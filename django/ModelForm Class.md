### ModelForm Class

>  그 전에는 모델과 폼을 따로 만들었다....
>
> 기존에 만들어 둔 모델을 통해 form class를 만들 수 있는 helper

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받는다.
- meta 클래스를 선언하고 어떤 모델을 기반으로 form 을 만들지 에 대한 정보를 기입한다



Meta class

- 모델의 정보를 작성하는 곳
- model form을 사용할 경우 사용할 모델이 있어야 하는데 meta class가 이를 구성한다.
- inner class 로서 클래스 내에 선언된 다른 클래스이다.
- 데이터에 대한 데이터



forms.py

```python
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
	class Meta : 
		model = Article
        fields = ('title', 'content')
        fields = '__all__' # 모든 속성 선택
        exclude = ('title', ) # 제외하고 싶은 속성
```

- 정의를 하지 않고도 모델폼이 모델의 입력받는 방법 등을 자동으로 해석하여 양식을 만든다.







