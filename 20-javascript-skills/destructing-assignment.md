# destructing assignment

- 구조 분해 할당

  ```javascript
  const foo = { "fizz-buzz": true };
  const { "fizz-buzz": fizzBuzz } = foo;

  console.log(fizzBuzz); // "true"
  // fizzBuzz = true
  ```

- 실전

  ```javascript
  const { isLoading: infoLoading, data: infoData } =
    useQuery < InfoData > (["info", coinId], () => fetchCoinInfo(coinId));
  ```

  - infoLodaing = false, data = Object
