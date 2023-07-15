# conda
>### 가상환경 확인하기
- conda info --env 
>### 다른 환경으로 패키지 옮기기
  - conda activate py
  - pip freeze > requirements.txt
    - /py/site-package의 목록 저장
  - dir *.txt
  - deactivate
  - conda activate gpu
  - pip install -r requirements.txt

- ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\ci_311\\anyio_1676425491996\\work\\dist'
  - vscode로 패키지를 설치해서 설치 경로가 길어짐. 윈도우 폴더이름 256을 넘어서 생기는 오류
  - 방법1. @ file 'C:/~' 삭제 하면 된다.
  - 방법2. 레지스트리 편집기로 폴더 이름 디폴트 바이트 수를 높이면 된다.
  - [link](http://ngmsoftware.com/bbs/board.php?bo_table=study&wr_id=428&sfl=mb_id%2C1&stx=admin&sst=wr_nogood&sod=desc&sop=and&page=4)
---


