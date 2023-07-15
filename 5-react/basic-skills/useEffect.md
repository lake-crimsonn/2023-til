# useEffect()

- 처음 렌더링할 때, 딱 한번 실행하고 싶은 코드를 파라미터로 받는다. 혹은 특정한 스테이트가 변할 때만 실행한다.
- index.js에서 React.StrictMode 때문에 두 번 출력 될 수 있다.
- clear function 기능이 있어서 컴포넌트가 파괴될 때 리턴 메시지를 남길 수 있다.
- ```javascript
  import styles from "./App.module.css";
  import { useState, useEffect } from "react";

  function Hello() {
    const [counter, setCounter] = useState(0);
    const [search, setSearch] = useState("");

    // 렌더링 될때만 호출되는 함수
    useEffect(() => {
      console.log(
        "this line will be printed only if `Hello Fn` has been worked"
      );
      return () => {
        // 클리어 펑션으로 컴포넌트가 파괴될 때 기능한다.
        console.log("Hello Fn destroyed");
      };
    }, []);

    //search 스테이트가 변경될 때와 처음 렌더링될 때 호출된다.
    useEffect(() => {
      console.log("when the value of search changes");
    }, [search]);

    const onChange = (event) => {
      setSearch(event.target.value);
    };

    const onClick = () => {
      setCounter((prev) => prev + 1);
    };

    return (
      <div>
        <h1 className={styles.title}>welcome to react</h1>
        <input
          value={search}
          onChange={onChange}
          placeholder="searching for"
        ></input>
        <h1 className={styles.title}>{counter}</h1>
        <button onClick={onClick}>count up</button>
      </div>
    );
  }

  function App() {
    const [hide, setHide] = useState(true);

    const onClick = () => {
      setHide((prev) => !prev);
    };

    return (
      <div>
        <button onClick={onClick}>{hide ? "hide" : "show"}</button>
        {hide ? <Hello /> : null}
      </div>
    );
  }

  export default App;
  ```

---
