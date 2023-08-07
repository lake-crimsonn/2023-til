# git blog

> ### 설치

- bundle install
- bundle exec jekyll serve

> ### 포스트 형식

- [기본형식](https://ansohxxn.github.io/blog/posting/)

---

- [양식링크](https://syki66.github.io/blog/2020/04/12/minimal-mistakes-theme.html)
- ```
    layout: single

    title: "포스트의 제목"
    excerpt: "발췌부분 설정하면 이 글이 들어가고, 설정하지 않는다면 글의 첫 문단이 들어가게됨"

    date: 2020-04-09 16:50:00 +0900
    lastmod: 2020-04-09 16:50:00 +0900 # sitemap.xml에서 사용됨

    author_profile: false # 왼쪽부분 프로필을 띄울건지

    header:
    overlay_image: https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80
    overlay_filter: 0.5 # 투명도

    categories:
    - test post

    tags:
        - test
        - theme

    # table of contents
    toc: true # 오른쪽 부분에 목차를 자동 생성해준다.
    toc_label: "table of content" # toc 이름 설정
    toc_icon: "bars" # 아이콘 설정
    toc_sticky: true # 마우스 스크롤과 함께 내려갈 것인지 설정

  ```

> ### giscus

- https://giscus.app/ko
- 로컬 환경에서는 댓글창이 보이지 않는다.
- 로컬에서 프로덕션 모드로 실행하기.

  ```
  - npm install --global cross-env
  - cross-env JEKYLL_ENV=development jekyll serve
  ```

  https://mmistakes.github.io/minimal-mistakes/docs/layouts/

> ### timezone

- Dependency Error: Yikes! It looks like you don't have tzinfo or one of its dependencies installed. In order to use Jekyll as currently configured, you'll need to install this gem. If you've run Jekyll with `bundle exec`, ensure that you have included the tzinfo gem in your Gemfile as well. The full error message from Ruby is: 'cannot load such file -- tzinfo' If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/!
- 이런 오류가 뜬 경우
- timezone: Asia/Seoul
- gem install tzinfo
- gem install tzinfo-data

---
