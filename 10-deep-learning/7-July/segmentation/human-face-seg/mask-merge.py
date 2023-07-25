import cv2
import numpy as np
from PIL import Image

if __name__ == "__main__":
    
    
    """ image path """
    line_mask_path = "C:\\data\\lapa\\LaPa\\results\\fmask.png"
    mask_path = "C:\\data\\lapa\\LaPa\\results\\1.png"

    """ image size """
    image_h = 512
    image_w = 512
    hori_line = 372

    """ image loading """
    line_mask = cv2.imread(line_mask_path, cv2.IMREAD_UNCHANGED)
    line_mask = cv2.resize(line_mask, (image_w, image_h))
    # line_mask = cv2.cvtColor(line_mask, cv2.COLOR_BGRA2BGR)
    
    mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    mask = cv2.resize(mask, (image_w, image_h))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2BGRA)
    
    """검은배경 만들기"""
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if (mask[i][j][:3] == 0).all():
                mask[i][j] = [0,0,0,0]
            
            if mask[i][j][3] == 255:
                mask[i][j] = [0,0,0,255]
    
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j][3] == 255:
                line_mask[i][j] = mask[i][j] * line_mask[i][j]
                line_mask[i][j][3] = 255
    
    # cv2.imshow("mov_img",mask)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    print(np.shape(line_mask))
    cv2.imwrite('C:\\data\\lapa\\LaPa\\results\\save4.png', line_mask)