# async

- async 함수안에서 await 사용하기
- await 역시 어나니머스함수처럼 변수에 담기
- await(await()) 처럼 숏컷으로 사용가능

```javascript
fetch("https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year")
  .then((response) => response.json())
  .then((json) => {
    setMoives(json.data.movies);
    setLoading(false);
  });
```

```javascript
const response = await fetch(
  `https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year`
);
const json = await response.json();
setMoives(json.data.movies);
setLoading(false);
```

```javascript
const json = await (
  await fetch(
    `https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year`
  )
).json();
setMoives(json.data.movies);
setLoading(false);
```

---
