# glob

```python
from glob import glob
baseFolder = 'C:/data/kfood/*'
Folders = glob(baseFolder)
dataList = []

for folder in Folders:
    subFolders = glob(folder+'/*')
    for subfolder in subFolders:
        fileList = glob(subfolder+'/*.jpg')
        dataList.append(fileList)

dataList
```
