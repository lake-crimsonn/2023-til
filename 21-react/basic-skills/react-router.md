# react-router

- [튜토리얼](https://reactrouter.com/en/main/start/overview)
- <details>
  <summary>react-router-dom 코드</summary>
  <div markdown="1">

  ```javascript
      App
      |--- 1
      routes
      |--- Details 3
      |--- Home
      components
      |--- Movie 2

      1
      import { BrowserRouter, Routes, Route } from "react-router-dom";
      <BrowserRouter basename={process.env.PUBLIC_URL}>
      <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/movie" element={<Details />} />
      </Routes>
      </BrowserRouter>

      2
      import { Link } from "react-router-dom";

      <h2>
      <Link to="/movie">{title}</Link>
      </h2>

      // a태그 대신 Link태그를 이용하면 새로고침 하지 않고 페이지를 이동한다

      3
      [App.js]
      <Route path="/movie/:id" element={<Details />} />

      [Details.js]
      import { useParams } from "react-router-dom";
      const { id } = useParams(); //const id = useParams()와 다름

      // useParams으로 url에 있는 파라미터를 받아올 수 있다.
  ```

  </div>
  </details>

---
