import cv2
import numpy as np

if __name__ == "__main__":

    """ image path """
    filename = "mask_sample_gd4"
    mask_path = f"C:\\data\\lapa\\LaPa\\results\\{filename}.png"

    """ image size """
    image_h = 512
    image_w = 512
    filter_wh = 64

    """ image loading """
    mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    mask = cv2.resize(mask, (image_w, image_h))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR)
    mask_c = mask.copy()

    # 라인 마스크 생성
    linemask = np.zeros((512, 512, 3), np.uint8)

    chin_arr = []
    # 턱 하단과 모델마스크 선까지의 거리 계산
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if (mask[j][i][0] == 177 and mask[j+3][i][0] == 177 and mask[j-3][i][0] == 177).all():
                chin_arr.append(j)
                cv2.line(linemask, (i, j), (i, j), (0, 0, 0), thickness=5)

    dst = max(chin_arr)+10
    print("dst:", dst)

    cv2.rectangle(linemask, (0, dst), (512, 512), (255, 255, 255), cv2.FILLED)

    # cv2.imshow('img', linemask)
    # cv2.waitKey(0)
    # cv2.destroyWindow()

    cv2.imwrite(f"C:\\data\\lapa\\LaPa\\results\\lm_{filename}.png", linemask)
