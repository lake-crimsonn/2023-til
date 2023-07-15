# cra

> ### 설치 및 실행

- npx create-reat-app [appname] --template typescript
- npm i --save-dev @types/styled-components
- npm i styled-components

> 템플릿 없이 cra를 만들었다면..

- 그냥 다시 설치하는 걸 추천
- npm install --save typescript @types/node @types/react @types/react-dom @types/jest
- App.js, index.js -> App.tsx, index.tsx
- npx tsc --init
- tsconfig.json
  ```javascript
    {
    "compilerOptions": {
    ......
    "jsx": "react-jsx"
        }
    }
  ```
- index.tsx

  ```javascript
    import ReactDOM from "react-dom/client"

    const root = ReactDOM.createRoot(document.getElementById("root") as        HTMLElement);
  ```

- npm i --save-dev @types/styled-components

---
