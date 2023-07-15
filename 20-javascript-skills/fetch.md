# fetch

```javascript
fetch("https://api.coinpaprika.com/v1/tickers").then((response) =>
  response.json().then((json) => {
    json.sort((a, b) => {
      return -(a.quotes.USD.price - b.quotes.USD.price);
    });
    setCoins(json);
    setLoading(false);
  })
);
```
