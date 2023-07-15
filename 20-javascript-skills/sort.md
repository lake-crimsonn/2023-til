# sort()

1.

```javascript
// 소트 할 배열
let list = ["Delta", "alpha", "CHARLIE", "bravo"];
// 임시 배열은 위치 및 정렬 값이있는 객체를 보유합니다.
let mapped = list.map(function (el, i) {
  return { index: i, value: el.toLowerCase() };
});
// 축소 치를 포함한 매핑 된 배열의 정렬
mapped.sort(function (a, b) {
  return +(a.value > b.value) || +(a.value === b.value) - 1;
});
// 결과 순서를 위한 컨테이너
let result = mapped.map(function (el) {
  return list[el.index];
});
```

2.

```javascript
json.sort((a, b) => {
  return -(a.quotes.USD.price - b.quotes.USD.price);
});
```

- 설명

```
  mapped.sort(function (a, b) {
  return +(a.value > b.value) || +(a.value === b.value) - 1;
});

The code you provided is using the sort() method on an array called mapped. This method is used to sort the elements of an array in place and returns the sorted array.

The sorting logic in the code is implemented using a compare function (a, b) => { return +(a.value > b.value) || +(a.value === b.value) - 1 }.

In this compare function, the + operator is used to convert a boolean value to a number. The expression a.value > b.value compares the value property of objects a and b. If a.value is greater than b.value, it returns 1, indicating that a should be sorted after b. If a.value is less than b.value, it returns -1, indicating that a should be sorted before b. If a.value is equal to b.value, it returns 0, indicating that the order of a and b should not be changed.

Overall, this code sorts the mapped array based on the value property of the objects in ascending order.
```

- [reference link](https://velog.io/@jazzyfact95/TIL-JS-sort-%EC%A0%95%EB%A0%AC-%EB%8B%A4%EC%A4%91-%EC%A0%95%EB%A0%AC)

---
