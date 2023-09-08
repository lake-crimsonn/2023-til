### 230906

# dreambooth

```
:: Required Files ::

Python 3.10.6
    - https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe

Stable Diffusion Model Cards
    - https://huggingface.co/CompVis/stable-diffusion-v-1-4-original
    - https://huggingface.co/stabilityai/stable-diffusion-2-1

GIT
    - https://gitforwindows.org/



:: Open PowerShell Prompt ::

C:
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
python -m pip install --upgrade pip
./webui.bat --listen

Move "sd-v1-4.ckpt" and "stable-diffusion-2-1.ckpt" to /stable-diffusion/models/Stable-Diffusion



:: Install Dreambooth ::

Extensions -> Available -> Dreambooth

```

### xformer 설치가 되지 않을 경우
- webui-user를 vscode로 열고 "set COMMANDLINE_ARGS= --xformers"
### 리눅스
- ./webui.sh --xformers

---