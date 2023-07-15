# styled.d.ts

- 패키지의 디폴트 선언을 바꾸는 파일과 코드다.

```typescript
// import original module declarations
import "styled-components";

// and extend them!
declare module "styled-components" {
  export interface DefaultTheme {
    bgColor: string;
    textColor: string;
  }
}
```
