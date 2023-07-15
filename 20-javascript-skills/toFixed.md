# toFixed()

```javascript
<select>
  {coins.map((item) => (
    <option key={item.id}>
      {item.name}: {item.quotes.USD.price.toFixed(3)}
    </option>
  ))}
</select>
```
