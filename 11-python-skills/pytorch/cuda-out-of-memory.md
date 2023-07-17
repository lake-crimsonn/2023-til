# cuda out of memory 에러

> OutOfMemoryError: CUDA out of memory. `Tried to allocate 16.00 MiB (GPU 0; >6.00 GiB total capacity; 5.32 GiB already allocated; 0 bytes free; 5.37 GiB reserved in total by PyTorch)` If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

- 16MB가 필요한데 충분한 공간이 없다는 뜻이다.
- GPU 0: 사용하는 GPU 번호다.
- total capacity: 6GB정도 공간이 있었는데,
- allocated: 5.32GB가 이미 할당 되었다.
- 0 bytes free: 0 바이트 사용할 수 있다.
- reserved in total by PyTorch: 5.37GB를 파이토치가 캐시해둔다.

### 에러가 발생하는 원인

- 모델 사이즈가 너무 크다.
- 배치 사이즈가 너무 크다.
- 데이터 증강의 정도가 너무 강압적이다.
- 메모리가 없다.

---
