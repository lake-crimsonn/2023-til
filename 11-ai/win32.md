# win32

```python
import win32gui
# 현재 실행중인 윈도우 핸들 목록 가져오기
def get_window_hwnd_list():
    def callback(_hwnd, _result: list):
        title = win32gui.GetWindowText(_hwnd)
        if win32gui.IsWindowEnabled(_hwnd) and win32gui.IsWindowVisible(_hwnd) and title is not None and len(title) > 0:
            _result.append(_hwnd)
        return True

    result = []
    win32gui.EnumWindows(callback, result)
    return result
```

```python
hwnd_list = get_window_hwnd_list()

index = 0
for hwnd in hwnd_list:
    print("index : " + str(index) + " / hwnd : " + str(hwnd) + " / title : " + win32gui.GetWindowText(hwnd))
    index += 1

```

---
