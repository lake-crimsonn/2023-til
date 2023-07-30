from unet import build_unet
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping, CSVLogger
import tensorflow as tf
from glob import glob
import cv2
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


global image_h
global image_w
global num_classes
global classes
global rgb_codes


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def load_dataset(path):
    train_x = sorted(glob(os.path.join(path, "train", "images", "*.jpg")))
    train_y = sorted(glob(os.path.join(path, "train", "labels", "*.png")))

    valid_x = sorted(glob(os.path.join(path, "val", "images", "*.jpg")))
    valid_y = sorted(glob(os.path.join(path, "val", "labels", "*.png")))

    test_x = sorted(glob(os.path.join(path, "test", "images", "*.jpg")))
    test_y = sorted(glob(os.path.join(path, "test", "labels", "*.png")))

    return (train_x, train_y), (valid_x, valid_y), (test_x, test_y)


def read_image_mask(x, y):
    """ Image """
    x = cv2.imread(x, cv2.IMREAD_COLOR)
    x = cv2.resize(x, (image_w, image_h))
    x = x/255.0
    x = x.astype(np.float32)

    """ Mask """
    y = cv2.imread(y, cv2.IMREAD_GRAYSCALE)
    y = cv2.resize(y, (image_w, image_h))
    y = y.astype(np.int32)  # 마스크는 이미 정규화되어있음

    return x, y


def preprocess(x, y):
    def f(x, y):
        x = x.decode()  # 바이트에서 스트링으로 디코딩
        y = y.decode()
        return read_image_mask(x, y)

    # 파이썬 함수를 텐서플로우 함수의 연산으로 래핑, 텐서 x, y를 받아서 넘파이 작업하고 텐서로 돌려줌
    image, mask = tf.numpy_function(f, [x, y], [tf.float32, tf.int32])
    mask = tf.one_hot(mask, num_classes)

    image.set_shape([image_h, image_w, 3])
    mask.set_shape([image_h, image_w, num_classes])

    return image, mask


def tf_dataset(X, Y, batch=8):
    ds = tf.data.Dataset.from_tensor_slices((X, Y))
    ds = ds.shuffle(buffer_size=5000).map(
        preprocess)  # 첫 5000개부터 가져와서 전처리처리하고 셔플함
    ds = ds.batch(batch).prefetch(2)  # 데이터 로딩을 줄이기 위해서 배치 2개를 미리 가져옴
    return ds


if __name__ == "__main__":
    """ Seeding """
    np.random.seed(42)
    tf.random.set_seed(42)

    """ Directory for storing files """
    create_dir("files")

    """ Hyperparameters """
    image_h = 512
    image_w = 512
    num_classes = 2
    input_shape = (image_h, image_w, 3)
    batch_size = 8
    lr = 1e-4  # 0.0001
    num_epochs = 100

    """ Paths """
    dataset_path = "C:\data\lapa\LaPa"
    model_path = os.path.join("files", "model.h5")
    csv_path = os.path.join("files", "data.csv")

    """ RGB Code and Classes """
    rgb_codes = [
        [0, 0, 0], [255, 255, 255]
    ]

    classes = [
        "background", "neck"
    ]

    """ Loading the dataset """
    (train_x, train_y), (valid_x, valid_y), (test_x,
                                             test_y) = load_dataset(dataset_path)
    print(f"Train: {len(train_x)}/{len(train_y)} - Valid: {len(valid_x)}/{len(valid_y)} - Test: {len(test_x)}/{len(test_x)}")
    print("")

    """ Dataset Pipeline """
    train_ds = tf_dataset(train_x, train_y, batch=batch_size)
    valid_ds = tf_dataset(valid_x, valid_y, batch=batch_size)

    """ Model """
    model = build_unet(input_shape, num_classes)
    model.compile(
        loss="categorical_crossentropy",
        optimizer=tf.keras.optimizers.Adam(lr)
    )

    """ Training """
    callbacks = [
        ModelCheckpoint(model_path, verbose=1,
                        save_best_only=True, monitor='val_loss'),
        ReduceLROnPlateau(monitor='val_loss', factor=0.1,
                          patience=5, min_lr=1e-7, verbose=1),
        CSVLogger(csv_path, append=True),
        EarlyStopping(monitor='val_loss', patience=4,
                      restore_best_weights=False)
    ]

    model.fit(train_ds,
              validation_data=valid_ds,
              epochs=num_epochs,
              callbacks=callbacks
              )
