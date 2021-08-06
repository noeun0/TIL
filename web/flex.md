# flex

> CSS의 flex는 엘리먼트들의 크기나 위치를 쉽게 잡아주는 도구이다.  이를 이용하면 레이아웃을 매우 효과적으로 표현할 수 있다.

CSS Flexible Box Layout

- 요소 간 공간 배분과 정렬 기능을 위한 1차원 레이아웃
- 요소와 축 두가지로 구성!
  - 요소 : Flex container( 부모 요소 ) /Flex Item( 자식 요소 )
  - 축 : Main axis ( 메인 축 ) / cross axis ( 교차 축)

https://flexboxfroggy.com/#ko

구성요소

- Flex Continer ( 부모 요소 )
  - flexbox 레이아웃을 형성하는 가장 기본적인 모델
  - Flex Item 들이 놓여있는 영역
  - **display : flex** 혹은 **inline-flex**로 시작
- Flex Item( 자식 요소 )
  - 컨테이너의 컨텐츠



### 속성

##### `justify-content` : 가로 정렬

: flex-end

: flex-start

: center

: space-between : 가로 전반적으로 퍼지게

: space-around :  양끝도 마진을 주고 퍼지게



##### `align-content`: 세로선 상에 여분의 공간이 있는 경우 flex 컨테이너의 여러줄의 간격을 조절한다

: flex-start

: flex-end

: center

: space-between

: space-around

: space-evenly



##### `align-items` : 세로선 상에서 정렬

: flex-start : 요소들을 꼭대기로

: flex-end : 요소들을 바닥으로

: center : 요소들을 가운데로

: baseline : 컨테이너의 시작 위치로

: stretch : 컨테이너에 맞도록 늘림



##### `flex-direction`

: row : 요소들을 텍스트 방향과 동일하게 정렬

: row-reverse : 요소들을 테스트의 반대방향으로 정렬 - start와 end도 반대가 된다.

: column : 요소들을 위에서 아래로 정렬 (보통 세로 정렬)

​	 -> flex의 방향이 column일 경우 justify-content의 방향이 세로, aㅋㅋlign-items의 방향이 가로

: column-reverse : 요소들을 아래서 위로 정렬



##### `flex-wrap`

: nowrap : 요소들을 한 줄에 정렬

: wrap : 요소들을 여러 줄에 정렬

: wrap-reverse : 요소들을 여러 줄에 걸쳐 반대로 정렬



non 속성 

display non
