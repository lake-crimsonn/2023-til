from train import create_dir, load_dataset
from sklearn.metrics import f1_score, jaccard_score
import tensorflow as tf
from tqdm import tqdm
from glob import glob
import pandas as pd
import cv2
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 경고창 지우기


global image_h
global image_w
global num_classes
global classes
global rgb_codes
global cnt
cnt = 0


def grayscale_to_rgb(mask, rgb_codes):
    h, w = mask.shape[0], mask.shape[1]
    mask = mask.astype(np.int32)  # rgb코드에 넣기위해서
    output = []

    for i, pixel in enumerate(mask.flatten()):
        output.append(rgb_codes[pixel])
    print(np.shape(output))
    output = np.reshape(output, (h, w, 3))
    return output


def save_results(image_x, pred, save_image_path):

    pred = np.expand_dims(pred, axis=-1)
    pred = grayscale_to_rgb(pred, rgb_codes)

    print(save_image_path)
    cv2.imwrite(save_image_path, pred)


if __name__ == "__main__":
    """ Seeding """
    np.random.seed(42)
    tf.random.set_seed(42)

    """ Hyperparameters """
    image_h = 512
    image_w = 512
    num_classes = 11
    filename = "sample_gd4"

    """ Paths """
    model_path = os.path.join("C:\\data\\lapa\\LaPa\\files", "model.h5")
    pic_path = f"C:\\data\\lapa\\LaPa\\results\\{filename}.jpg"

    """ RGB Code and Classes """
    rgb_codes = [
        [0, 0, 0], [177, 255, 255], [255, 255, 255], [255, 255, 255],
        [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255],
        [255, 255, 255], [255, 255, 255], [255, 255, 255]
    ]

    classes = [
        "background", "skin", "left eyebrow", "right eyebrow",
        "left eye", "right eye", "nose", "upper lip", "inner mouth",
        "lower lip", "hair"
    ]

    """ Load the model and pic"""
    model = tf.keras.models.load_model(model_path, compile=False)

    """ Prediction """
    image = cv2.imread(pic_path, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (image_w, image_h))
    image_x = image
    image = image/255.0  # (H, W, 3)
    image = np.expand_dims(image, axis=0)  # [1, H, W, 3]
    image = image.astype(np.float32)

    """ Prediction """
    pred = model.predict(image, verbose=0)[0]
    pred = np.argmax(pred, axis=-1)  # [0.1, 0.2, 0.1, 0.6] -> 3
    pred = pred.astype(np.int32)

    """ Save the results """
    filename = "mask_"+filename
    save_image_path = f"C:\\data\\lapa\\LaPa\\results\\{filename}.png"
    # print(save_image_path)
    save_results(image_x, pred, save_image_path)
