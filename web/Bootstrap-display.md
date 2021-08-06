# 반응형 웹 구현 - display

> bootstrap을 사용한 반응형 웹 구현하기



display 속성 값을 사용하면, 중단점마다의 요소의 특성을 변경시켜 줄 수 있다.

이를 활용하여 웹의 구조를 띄다가 화면의 크기가 작아져 작은 기기의 액정의 크기가 된다면 그에 적합한 구조로 변경 시켜 줄 수 있다.



**display 속성**

`.d-{value}` ~을위한 `xs`

`.d-{breakpoint}-{value}`대한 `sm`, `md`, `lg`, `xl`,와 `xxl`.

- `none`
- `inline`
- `inline-block`
- `block`
- `grid`
- `table`
- `table-cell`
- `table-row`
- `flex`



**요소 숨기기**

| 화면 크기            | 수업                              |
| -------------------- | --------------------------------- |
| 모두에 숨겨진        | `.d-none`                         |
| xs에서만 숨김        | `.d-none .d-sm-block`             |
| sm에만 숨김          | `.d-sm-none .d-md-block`          |
| md에서만 숨김        | `.d-md-none .d-lg-block`          |
| lg에서만 숨김        | `.d-lg-none .d-xl-block`          |
| xl에서만 숨김        | `.d-xl-none .d-xxl-block`         |
| xxl에서만 숨김       | `.d-xxl-none`                     |
| 모두에 표시          | `.d-block`                        |
| xs에서만 볼 수 있음  | `.d-block .d-sm-none`             |
| sm에서만 볼 수 있음  | `.d-none .d-sm-block .d-md-none`  |
| md에서만 볼 수 있음  | `.d-none .d-md-block .d-lg-none`  |
| LG에서만 볼 수 있음  | `.d-none .d-lg-block .d-xl-none`  |
| xl에서만 볼 수 있음  | `.d-none .d-xl-block .d-xxl-none` |
| xxl에서만 볼 수 있음 | `.d-none .d-xxl-block`            |



미디어 쿼리

단말기의 유형과 어떤 특성이나 수치에 따라 웹사이트의 스타일을 수정할 때 용이

- 특정 조건이 충족되면 일정 스타일 클래스를 적용시킬 수 있게 한다

- ```
  @media(조건){
  .클래스 {스타일}
  }
  ```

  

