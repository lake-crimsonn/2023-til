import cv2


if __name__ == "__main__":
    """ image path"""
    pic_path = "C:\\data\\lapa\\LaPa\\results\\B.jpg"
    mask_path = "C:\\data\\lapa\\LaPa\\results\\mask.png"

    """ image size """
    image_h = 512
    image_w = 512

    """ image loading """
    image = cv2.imread(pic_path, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (image_w, image_h))

    mask = cv2.imread(mask_path, cv2.IMREAD_COLOR)
    mask = cv2.resize(mask, (image_w, image_h))

    

