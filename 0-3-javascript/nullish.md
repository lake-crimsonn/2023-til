# nullish

- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing

- ?? (Null 병합 연산자 (Nullish coalescing operator))

- ??앞에 값이 null이거나 undefined이면 오른쪽 값을, 그렇지 않으면 왼쪽 값을 반환하는 논리연산자
- ```javascript
  null ?? "hello"; // "hello"
  undefined ?? "hello"; // "hello"
  "hi" ?? "hello"; // "hi"
  ```

---
