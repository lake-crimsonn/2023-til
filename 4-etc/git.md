# git

## 깃 명령어

- 보편적인 명령어

  - https://bacassf.tistory.com/28

- 원격 레포지토리 주소 변경

  - git remote set-url origin [url]

- 강제로 푸쉬하기

  - git push -u origin +master

- git remote
    <details><summary>명령어</summary>
    <div>

  1. git repository 확인하기 : \$ git remote

  2. git repository 추가하기 : \$ git remote add <단축이름> <url>

  3. git repository 가져오기 : $ git fetch <Repository alias> <branch>또는 $ git pull <Repository alias> <branch>

  4. git repository에 수정사항 저장하기 : \$ git push <Repository alias> <branch>

  5. git repository 확인하기 : \$ git remote show <Repository alias>

  6. git repository 이름 변경하기 : \$ git remote rename <현재 Repository alias>

  7. git repository 삭제하기 : $ git remote remove <Repository alias> 또는 $ git remote rm <Repository alias>

    </div>
    </details>

---

## 깃 페이지

- npm i gh-pages

  - npm run build: 프로덕션 빌드
  - package.json
    - "homepage": "https://깃허브이름.github.io/레포지토리"
    - scripts
      - "deploy": "gh-pages -d build"
        - -d: 디렉토리
      - "predeploy": "npm run build"
        - 디플로이를 하면 프리디플로이가 먼저 실행돼서 빌드한다.

---

## 깃 라지파일

- 깃에 한번 기록된 라지파일(100메가바이트 이상의 파일)은 히스토리에 남는다. 라지파일이 있으면 깃허브에 푸쉬를 할 수 없다. 실제 파일목록에서 라지 파일을 삭제 했더라도 히스토리가 파일을 기억하고 있다. 그래서 푸쉬가 안된다.
- git reset --hard HEAD~2 이 명령어 절대 사용하지 않기. 파일이 다 날아간다.

- https://rtyley.github.io/bfg-repo-cleaner/

---

## 깃 파일 복구

- git reflog
- git reset --hard [commit_id]

---
