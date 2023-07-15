# map

### map으로 리스트 추가하기

- 잊어버리지 말기!

```javascript
    <div>
    {movies.map((movie) => (
    <div key={movie.id}>
        <h2>{movie.title_long}</h2>
        <img src={movie.medium_cover_image} />
        <h3>{movie.rating}</h3>
        <p>{movie.summary}</p>
        <ul>
            {movie.genres.map((g) => (
                <li key={g}>{g}</li>
            ))}
        </ul>
    </div>
    ))}
```

---
