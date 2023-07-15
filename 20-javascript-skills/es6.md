# es6

```javascript
const value = event.currentTarget.value;
const { value } = event.currentTarget;
const {
  currentTarget: { value },
} = event;
```

- 3개의 스테이트먼트는 모두 같은 의미다.
- 같은 이름으로 밸류를 편하게 가져오기 위해서 사용한다.

```javascript
// not good way
const value = event.currentTarget.value;
const tagName = event.currentTarget.tagName;
const width = event.currentTarget.width;
const id = event.currentTarget.id;

// good way
const {
  currentTarget: { value, tagName, width, id },
} = event;
```

- currentTarget의 여러 변수를 가져다 쓸 때 유용하다.

---
