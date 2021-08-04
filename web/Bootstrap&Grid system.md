# Bootstrap

> 디자인 적인 요소들에 관한 클래스(선택자) 들을 구현해놓은 라이브러리



### 사용법

###### 파일 다운받아서 사용하기

1. https://getbootstrap.com/docs/5.0/getting-started/download/ 에서 Compiled CSS and JS 다운로드해서 해당 폴더에 넣어줌

2. css, js 사용을 위한 코드를 html에 추가해준다

   ```html
   <head>
   	<link rel="stylesheet" href="css/boorstrap.css">
   </head>
   
   <body>
   	<script src="bootstrap.bundle.js"></script>
   </body>
   ```

###### 오픈 소스 CDN인 jsDelivr 이용하기

- https://getbootstrap.com/docs/5.0/getting-started/introduction/ 의 css,js를 head와 body에 복붙

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

```

#### CDN?

- content delivery network
- 컨텐츠를 효율적으로 전달하기 위해 서버와 사용자 사이의 물리적 거리를 줄여 컨텐츠 로드 지연을 최소화 한다.
- 분산 된 서버로 관리하기 때문에 누구나 동일한 품질의 컨텐츠를 시간을 늦추지 않고 사용할 수 있다.
- 따로 관리하는 업체가 있고, bootstrap도 업체와 계약을 한 것이다!
- 외부 서버를 활용함으로써 본인 서버의 부하가 적어진다.
- 트래픽의 절반 이상을 cdn이 차지하고 있다.



### 문법



-추가 예정

#### .mt-1? 

>  마진 탑 1로 줘라!

#### .mx-0?

> x축 즉 좌우를 뜻한다 / y는 상하!!
>
> mx-auto : 수평 중앙 정렬



### Flexbox in Bootstrap?

`.d-flex` : 부트스트랩에서도 flex를 똑같이 사용할 수 있다.



---



# Grid system

>  responsive web design
>
> 다양한 화면의 디바이스의 등장으로 필요해짐
>
> 별도의 기술이름이 아니라 웹 디자인에 대한 접근 방식
>
> 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 언어
>
> media queries, flexbox, bootstrap grid system, the viewport meta tag 등이 있음



### Grid system 구성

- bootstrap grid system은 flexbox로 제작됨

- 깔끔하고 일관성 있는 작업을 하기 위한 시스템

- container, rows(행), column(열),으로 컨텐츠를 배치하고 정렬

  - container : grid 시스템이 적용 되는 전체 범위
  - row : columns의 wrapper
  - column (col) : container는 12개의 컬럼으로 나누어 구성됨. 
    - 너비는 백분율로 설정 되므로 항상 부모 요소를 기준으로 유동적으로 크기가 조정된다
    - grid layout에서 내용은 반드시 columns안에 있어야 한다. 오직 columns만 row의 바로 하위 자식 일 수 있다.
  - gutter : 간격을 위한 여백을 주는 것 
    			- column사이의 padding
    			- grid 시스템에서 반응적으로 공간을 확보하고 컨텐츠를 정렬하는데 사용

- 12개의 column, 6개의 grid breakpoints로 구성

  - container-> rows -> column 으로 구성

- 이 grid system을 쉽게 css로 구현할 수 있게 돕는 css framework가 bootstrap

  -> 반응형이 가능하게 됨



ex)

```html
  <div class= "container">
    <h2 class="text-center">column class - 1</h2>
    <div class="row">
  
      <div class="box col-3">1</div>
      <div class="box col-6">2</div>
      <div class="box col-3">3</div>
    </div>
      
```



### Grid breakpoints

- 다양한 디바이스에 적용하기 위해 특정 픽셀 조건에 대한 지점을 정해둠
- 대부분의 크기를 정하기 위해 em rem을 사용하지만 px은 grid breakpoint에 사용된다
  - viewport 너비가 픽셀 단위이고 글꼴 크기에 따라 변하지 않기 때문이다!

- breakpoint에 따른 설정이 가능하도록 각각 크기 별로 선택자를 제공한다.

- 미디어 쿼리를 이용해 싸이즈가 나뉘어져 있다.

### nesting

-추가 예쩡
