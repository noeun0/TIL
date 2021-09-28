### Handling HTTP requests

>  Django에서 http요청을 처리하는 방법



##### Django shortcut functions 사용

- render, redirect 가 대표적shortcut function 이다.!

- 개발에 도움이 되는 여러 함수와 클래스를 제공한다
  - render()
  - redirect()
  - get_object_or_404()
  - get_list_or_404()

get_object_or_404()

- 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 경우 http404를 raise
- 500등의 에러를 받았을 땐 원인을 찾지 못한다. 더 정확한 사유를 전달해주어야 한다.
- 객체를 가져올 때 get을 사용하지 않고, get_object_or_404(인스턴스, pk=pk값)
- detail, delete, update 변경 가능..



##### Django view decorators

- 해당 함수를 수정하지 않고 기능을 연장 해주는 함수
  - request_http_methods
  - require_POST
  - require_safe (= require_GET)

```python
import django.views.decorators.http import request_http_methods

@request_http_methods(['GET','POST'])
def create,update(request,(pk)):
    
@require_POST
def delete(request,pk)
   
@require_safe
def index, detail(request,pk)

```



- http 요청에 따라 적절한 예외처리, 데코레이터를 통해 서버를 보호하고 클라이언트에게 정확한 상황을 제공하는 것이 중요하다

  





















1. View decorators 사용

   