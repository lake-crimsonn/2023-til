### gpu 설치

1. 프로그램 추가/제거에서 nvidia 삭제
2. 구글에 nvidia cuda 11.8 검색하고 설치
3. 구글드라이브 '공유문서함/2023메타버스아카데미/딥러닝'에 있는 파일 다운받고 압축 풀기
4. C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8에 bin, lib, include, LICENSE 복사
5. 환경변수 bin, lib, include 파일주소 추가
   - 윈도우검색창에 '시스템 환경 변수 편집' 검색 후 클릭
   - 하단에 있는 환경변수 클릭
   - Path 선택하고 편집 클릭
   - 새로 만들기 클릭해서 bin, includ, lib 파일주소 추가(컴퓨터마다 주소가 다를 수 있음)
   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include
   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib
6. anaconda 프롬프트 열고 gpu가상환경과 텐서플로우 설치
   - conda create -n gpu python=3.9
   - conda activate gpu
   - pip install tensorflow-gpu==2.8.0
   - pip install protobuf==3.20.1 --force-reinstall
   - python
   - \'>>>' 프롬프트가 뜨고나서 아래 명령어 실행
   - import tensorflow as tf
   - from tensorflow.python.client import device_lib
   - device_lib.list_local_devices()
   - 결과창에 GPU라는 단어가 있으면 성공
7. 실패시 gpu 가상환경 다시 설치
   - conda deactivate
   - conda remove --name gpu --all
   - 4번부터 6번까지 이상없는지 확인하면서 다시 실행

---

- C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
- C:\Users\user\Documents\카카오톡 받은 파일\zlibwapi.dll-61514 설치하기

---
