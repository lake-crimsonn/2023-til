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

- 깃에 한번 기록된 라지파일(100메가바이트 이상의 파일)은 히스토리에 남는다. 라지파일이 있으면 깃허브에 푸쉬를 할 수 없다. 실제 파일목록에서 라지 파일을 삭제하더라도 히스토리가 파일을 기억하고 있다. 그래서 푸쉬가 안된다.
- git reset --hard HEAD~2 이 명령어 절대 사용하지 않기. 파일이 다 날아간다.

- https://rtyley.github.io/bfg-repo-cleaner/

---

## 깃 파일 복구

- git reflog
- git reset --hard [commit_id]

---

## CLRF 문제

```
warning: in the working copy of '10-deep-learning/7-July/huggingface/1-huggingface-hub.ipynb', LF will be replaced by CRLF the next time Git touches it
```

- line ending 혹은 EOL 문제. OS마다 사용하는 개행 문자 차이로 인한 문제다. Windows는 CRLF. Linux, MacOS는 LF를 이용한다.
- 실제 코드는 변경된 게 없는데 소스의 CR/LF 때문에 변경으로 착각하여 commit 을 하게 될 수 있으며 변경 로그를 보거나 merge 마다 문제가 될 소지가 있다.
- CR은 Carrige Return(\r). 현재 라인에서 커서의 위치를 가장 앞으로 옮김
- LF는 Line Feed(\n). 커서의 위치는 그대로 두고 종이를 한 라인 위로 올림
- CRLF(\r\n).
- 윈도우와 리눅스가 서로 글자를 전송할 때 개행문자가 제대로 반영이 안될 수 있다.

### 해결방법

#### 윈도우

- git config --global core.autocrlf true
- 윈도우에서 저장소로 보낼 때는 LF 설정.
- 저장소에서 윈도우로 가져 올때는 CRLF 설정.

#### 리눅스

- git config --global core.autocrlf input
- LF만 사용한다.

---
