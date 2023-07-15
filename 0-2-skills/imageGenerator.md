# image generator

- [230704-2-imageGen](/3-deep-learning/7-July/230704-2-imageGen.ipynb)

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 이미지 제너레이터를 정의합니다.
train_datagen = ImageDataGenerator(rescale=1. / 255)
val_datagen = ImageDataGenerator(rescale=1. / 255)

def get_steps(num_samples, batch_size):
    if (num_samples % batch_size) > 0:
        return (num_samples // batch_size) + 1
    else:
        return num_samples // batch_size
```

```python
class_col = train_df.columns[2:]
batch_size = 32

# 훈련자료: w,b 갱신
train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_df,
    directory=base,
    x_col = 'image',
    y_col = class_col,
    target_size = (112, 112),
    color_mode='rgb',
    class_mode='raw',
    batch_size=batch_size,
    seed=42
)

# 훈련된 w,b 검증
val_generator = val_datagen.flow_from_dataframe(
    dataframe=val_df,
    directory=base,
    x_col = 'image',
    y_col = class_col,
    target_size = (112, 112),
    color_mode='rgb',
    class_mode='raw',
    batch_size=batch_size,
    shuffle=True
)
```
