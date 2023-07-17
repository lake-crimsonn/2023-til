# gpu_empty

- 전용 gpu 메모리 알아보기

```python
import torch
torch.cuda.memory_allocated()
```

- 전용 gpu 리셋하기

```python
!pip install numba

from numba import cuda

device = cuda.get_current_device(); device.reset()
```
