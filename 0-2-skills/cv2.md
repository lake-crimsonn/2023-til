# cv2

> ### cv2 한글 폴더 가져오기

```python
    img_array = np.fromfile(src, np.uint8)
    image = cv2.imdecode(img_array,cv2.IMREAD_COLOR)
```

> ### cv2 기본 사용법

```python
import cv2
image = cv2.imread(base+test_df['image'][i])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

- plt로 이미지 보기

```python
a2=[]
for image in lee_imgs:
    arr2=cv2.imread(os.path.join(data_dir_lee,image),cv2.IMREAD_GRAYSCALE)
    a2.append(arr2)

plt.figure(figsize=(10,10))
for i in range(len(a2)):
    plt.subplot(10,5,i+1)
    plt.imshow(a2[i],cmap='gray')
```

- cv2 imshow로 다른 윈도우에서 이미지 보기

```python
image = cv2.imread(imgFilesAddr[0], cv2.IMREAD_COLOR)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- cv2로 부르고 plt로 이미지 확인하기

```python
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)   # img파일을 b,g,r로 분리
img2 = cv2.merge([r,g,b]) # b, r을 바꿔서 Merge

plt.imshow(img2)
plt.xticks([]) # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()
```

---
