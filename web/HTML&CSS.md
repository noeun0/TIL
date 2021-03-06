# HTML / CSS



# 1. html

> HyperText Markup Language 하이터 텍스트를 가장 중요한 특징으로 하는 마크업이라는 형식을 가진 컴퓨터 프로그래밍 언어
>
> GML -> SGML -> SGMLguid -> HTML ( 17개의 태그에 <a>태그를 추가해서 발전)

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 단순하게 데이터를 표현 : 저장, 조건, 반복이 안된다.
- 웹 페이지를 작성하기 위한 언어 : 의미와 구조를 정의



### 기본구조

**html**

- head : 문서 제목, 문자 코드와 같이 해당 문서 정보를 담고 있다. 메타데이터
- body : 화면에 나타나는 정보. 실제 내용에 해당



**DOCTYPE**

`<!DOCTYPE html>`

태그가 제거되거나 새로 추가되거나 변경되거나 하기 때문에 어떤 표준을 따르고 있는 테그들인지 알려주어야 한다. document type 을 html로 선언한다.



**DOM 트리 구조**

- Document Object Model - 태그들을 하나의 객체로 생각

**요소**

- 태그와 내용으로 구성되어 있다.
- 요소는 중첩될 수 있다.
- 오류를 반환하지 않는다
- 태그는 그 정보의 성격과 의미를 나타냄
- 속성(attribute)
  - <속성명="속성값"> - 태그별로 다 다름
  - 공백 금지! 쌍따옴표 사용!으로 통일하자
  - 시작태그에 작성됨
  - 이름과 값이 하나의 쌍으로 존재
  - 태그와 상관없이 사용가능한 속성들도 있다
  - 경로나 크기와 같은 추가 정보를 제공
- MDN에서 html 정보를 확인할 수 있다.



### 태그

`<p>`  

: paragraph 단락을 표현할때 사용

- css를 사용해서 간격을 바꿔줄 수 있다.

`<br>`

: a forced line-break

- 내용이 없는 태그

- 갯수를 맘대로 두어서 간격을 `<p>`보다 더 자유롭게 변경 가능
- 시각적으로는 나눠지지만 구간을 알려줄려면 `<p>`를 사용하는게 더 좋다

`<img>`

: 문서에 이미지를 포함한다.

- `src=""` : 이미지 경로
- `width=`& `height=` 를 변경하여 이미지의 크기를 조절할 수 있다.
- `alt=""` : alternative text 대체 메세지
- `title=""` : 이미지에 마우스를 가져다 댔을때 나오는 메세지 



**텍스트 관련 태그와 속성**

- `<b>` vs `<string>` : 굵게 / 강조 

- `<i>` vs `<em>` : i는 어떤 이유에서 주위와 구분해야 하는 경우. em은 강세를 나타냄 /둘다 기울임꼴 표시
- `<span>`, `<br>`, `<img>` 
- 등등

**table**

- `<tr>` `<td>` ...  안중요
- `border` : 테두리 

```html
<table>
    <tr>
        <td><td/><td></td>
    </tr>
    <tr>
        <td><td/><td></td>
    </tr>
    <tr>
        <td><td/><td></td>
    </tr>
</table>
```



**리스트 관련 요소**

- `<ol>` : ordered list
- `<ul>` : unordered list   

> ​	태그의 중첩이 필요할 때가 있다. 가독성을 위해 탭해준다.

```html
<ul>
    <li> </li>
    <li> </li>
    <li> </li>
</ul>

<ol>
    <li> </li>
    <li> </li>
    <li> </li>
</ol>
```

`<meta>` 

- `charset = "utf-8"`를 넣어주면 깨짐을 방지할 수 있음



`<form> </form>`  

: 서버로 데이터를 보내주는 태그

- 어디로 보내주는가를 설정해줌

- `action=` : 보내주는 주소

- `method=` : 보내주는 방식 

  - `"get"` : url로 전송하는 방법
  - `"post"` : 보이지 않게 전송하는 방법

  

`<input>` 

: (주로 form 안에서 사용!)

- `name`= 입력받을 값을 전달할 변수 이름
  - `name="hide"` 로 설정하면 보이지는 않지만 값 전송
  - name="name" -> url 뒤에 name=노은영 식으로 붙혀서 전송

-  `type=` : 받는 값의 타입

  - `"file"` : 파일 전송
    - 파일을 전송하려면 form 태그에 `action="위치" method ="post" enctype="multipart/form-data"`를 추가해주아야 한다.
  - `"button"`  : 버튼

  -  ` "text"`  : 텍스트 입력
  -  `"password"`  : 비밀번호
  -  `   "number"` : 숫자 입력
  -  `   "radio"` :  라디오 버튼
  -  `"submit"` : 전송
  - `"reset"` : 초기화
  -  `"textarea"` :cols/rows지정 가능, value값을 두줄 이상 받을 수도 있기 때문에 윗 타입들과는  다른 형식이다. 
  - 요소의 동작은 type에 따라 달라지므로, 숙지해야함

- `value=` : 디폴트 값을 지정

- `id=` : label과 연결해줌

- `placeholder=` : 입력받기 전에 보여줄 텍스트

- `pattern=` : 데이터 검증

- `required= ` : 필수 입력사항 인지

- `autofocus=` : 페이지가 열릴때 포커스가 이동하게

  ```html
  # 한 질문에 해당하는 것들은 name을 통일해야함
  # 전달될 값은 value
  <input type = 'radio' id="temp1" name = 'temp' value="under">
  <label for "temp1"> 37도 미만 </label>
  <input type = 'radio' id="temp2" name = 'temp' value="over">
  <label for "temp2"> 37도 이상 </label>
  ```

  

`<select>`  

:선택박스로 입력받음

- `multiple : 다중 선택 가능하게 함

- `<option>`  `</option>` 

  - `value =` 값에 전달할 값을 넣어주어야 함

    

`<a>`  

: 링크임을 알려준다. ==anchor(닻)

- 링크라는 것을 알려주는 태그

- `href =` 링크를 넣어주는 속성

- `target =` 어디에 링크를 넣어줄 것인가

  - _blank: 새창에서 열어줌

- `title =` 마우스를 올려놨을때 보여지게 할 내용

  

`<div>`

- 일정 영역으로 묶어줌

- 스타일 만들때 스타일을 묶어주기도(?)

  

`<label> </label>`

: 특별한 기능은 없지만, 무언가의 이름표라는 것을 기술

- 그냥 이름표를 만들어 줄 수 도 있지만 checkbox  전체를 라벨로 묶어서 범위를 만들어줄 수도 있다.

- `for=`  뭐를 위한 라벨인지 . 클릭했을때 커서가 어디로 가는지
  
  - input의 `id` 값을 넣어줌
  
    

---



### **시맨틱 태그**

> div로만 구조를 나누니 어떤 역할의 코드인지 구분이 안됨
>
> html5에서 의미론적 요소를 담은 태그의 등장. 별도의 역할은 없음

- header : 문서 전체나 섹션의 헤더
- nav : 네비게이션
- aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
- section : 문서의 일반적인 구분, 컨텐츠의 그룹 표현
- article : 문서, 페이지, 사이트 안에서 독립적으로 구부되는 영역
- footer : 문서 전체나 섹션의 푸터 

역할

- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 뿐만 아니라 의미를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 가독성을 높일 수 있고 유지보수를 쉽게 함
- 검색엔진 최적화를 위해 메타태그. 시멘틱 태그 등을 통한 마크업을 효과적으로 할 필요가 있다.
- 의미와 관련성을 가지는 거대한 데이터베이스로 구축하고자 하는 발상

> 웹 접근성 :  장애인이나 고령자 분들이 제공되는 서비스를 비장애인들과 동등하게 접근하고 이용할 수 있도록 보장하는 것



div#ssafy : #은 id 선택자

div.ssafy : class .은 클래스 선택자



---

# 2. CSS

> 스타일 레이아웃을 통해 문서를 표시하는 방법을 지정하는 언어

- css 구문은 선택자와 함께 열림
- 선택자를 통해 스타일을 지정할 html 요소를 지정
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 : 어떤 스타일 기능을 변경할지 결정
  - 값 : 어떻게 스타일 기능을 변경할지 결정

- 정의 방법

  - 인라인 : 태그 안에서 작성한다
  - 내부참조 : head 태그 내 `<style>`태그에 작성
  - 외부참조 : 외부 css파일을 `<head>`내 `<link>`통해 불러오기

   

**선택자** 

: 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 필요

- 기본 선택자

  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자

**결합자**

- 자손 결합자 : selector A 하위의 모든 selectorB 요소

  ```
  div span
  ```

- 자식 결합자 : selector A 바로 아래의 selectorB 요소

  ```
  div > span
  ```

- 일반 형제 결합자 : selectorA의 형제 요소 중 뒤에 위치하는 selectorB요소를 모두 선택

  ```
  p ~ span
  ```

- 인접 형제 결합자 : selectorA의 형제 요소중 바로 뒤에 위치하는 selectorB요소를 선택

  ```
  p + span
  ```

- 의사 클래스 / 요소

  - 링크  동적 의사 클래스
  - 구조적 의사 클래스


**css 적용 우선순위**

1. 중요도

- important

2. 우선 순위

- 인라인 > id 선택자 > class 선택자 > 요소 선택자

3. 소스 순서

**css 상속**

- css는 상속을 통해 부모 요소의 속성을 자식에게 상속
- 속성 중에는 상속이 되는것과 되지 않는 것이 있다.
- 상속되는 것
  - text 관련 요소 (font, color, text-align), opacity, visibility
- 상속 되지 않는 것
  - box model 관련 요소 (width, height, margin, padding, border, box-sizing, display),
  - position 관련 요소(position, top/right/bottom/left)



html 요소 구성 : box 형태로 되어있다!

- content : 글이나 이미지 등 요소 실제 내용

- padding : 테두리 안쪽의 내부 여백 배경색, 이미지 적용 가능

- border : 테두리

- margin : 테두리 바깥의 외부 여백 배경색 지정 못함

  값의 갯수에 따라 나타내는 바가 달라짐

  - 1개 : 상하좌우
  - 2개 : 상하 / 좌우
  - 3개 : 상/ 좌우 / 하
  - 4개 : 상 / 우 / 하 / 좌

  마진 상쇄 : block A의 top 과 block B의 bottom 에 적용된 각각의 margin이 둘 중에서 큰 마진 값으로 결합되는 현상

`p:nth-of-type`

: n번째 p를 찾아 속성을 적용해준다.



`p:nth-child`

:모든 자식중 n번째 값에 속성을 적용해준다.



style은 보통 헤더에 넣는다.



---

# display

### block

- 한줄 전체를 사용 마진을 전부 차지
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다.
- div, p, hr, h, ul, ol, li, form  등

### inline

- 자기 부분만 차지
- 너비, 마진을 줄 수 없다.
- 위아래 마진을 line height를 사용해서 지정해줄 순 있음
- input, span, a, img, label, b, em, i, strong( 하나의 단어만 수정하는.. ) 등..

### inline-block

- block 과 inline 레벨 요소의 특징을 모두 갖는다.
- inline처럼 한줄에 표시 가능하며
- block처럼 width, height, margin 속성을 모두 지정할 수 있다.

### none

class 생성자 형태로 아래와 같이 값을 줄 수 있다!

```html
.none{
	display : none ;
}
```

- 해당 요소를 화면에 표시하지 않는다.
- visibility : hidden은 공간은 차지하나 화면에만 안보임



서로의 형태로 `style="display:inline"`형태로 변경 가능 하다.

> 큰 부분안에 작은 부분을 넣는건 o ( block 안에 inline)
>
> 반대는 x



---

# CSS position

- relative : 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동
  - 레이아웃에서 요소가 차지하는 공간은 static 일때와 같다.
- absolure : 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않는다.
  - 가장 가까히 있는 부모, 조상 요소를 기준으로 이동
  - 원래 위치에 있던 과거 위치 공간은 더이상 존재하지 않는다. 즉 아래 것들이 위로 올라오게됨!





---



클래스 선택자 > div선택자

