# react-basic

- 리액트 장점

  페이지를 리렌더링할 때 수정된 부분만 업데이트가 된다.

  같은 역할을 갖는 엘레멘트 코드를 재사용할 수 있다.

- react.js

  웹어플을 인터렉티브하게 만들어주는 라이브러리.

- react-dom

  리액트 엘레멘트를 HTML body에 두는 역할을 하는 라이브러리.

- JSX

  확장된 자바스크립트 문법, HTML과 비슷하게 생겨서 사용하기 편하다.

- Babel

  브라우저는 JSX를 이해할 수 없어서 바벨을 이용하여 JSX를 자바스크립트로 바꿔준다. 자바스크립트를 HTML처럼 이용이 가능하다. 가독성이 좋아진다.

- React.createElement()

  리액트 엘레멘트 만드는 함수.

- React.useState()

  데이터 초기화 함수. 배열의 리턴하는데, 인덱스 0번은 수정할 데이터, 인덱스 1번은 데이터를 수정할 때 사용하는 함수.

- Component

  JSX를 리턴하는 함수

- props

  부모 컴포넌트의 기능을 자식 컴포넌트에게 전달하여 사용한다. 문자열, 불리언 뿐만 아니라 함수도 상속이 가능하다. 코드를 재사용할 수 있지만, 부모 컴포넌트의 상태가 변하면 모든 자식 컴포넌트를 리렌더링한다.

- React.memo()

  부모 컴포넌트의 상태가 변할 때 영향을 받는 자식 컴포넌트만 리렌더링하게 해준다

- npx

  [참고 사이트](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b)

- react-script

* useEffect()

  - 처음 렌더링할 때, 딱 한번 실행하고 싶은 코드를 파라미터로 받는다. 혹은 특정한 스테이트가 변할 때만 실행한다.

- prop-types

  - 특정한 자료형의 데이터만 props로 사용가능하게 해준다.

- React.StrcitMode

  - 개발 단계에서 오류를 잘 잡기 위해 두번 씩 렌더링 된다

* react-router-dom
* gh-pages
* styled-components

---
