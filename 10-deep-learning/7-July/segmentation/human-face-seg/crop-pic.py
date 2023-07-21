import cv2
import numpy as np

if __name__ == "__main__":
    
    
    """ image path """
    pic_path = "C:\\data\\lapa\\LaPa\\results\\B.jpg"
    mask_path = "C:\\data\\lapa\\LaPa\\results\\mask_colored.png"

    """ image size """
    image_h = 512
    image_w = 512
    hori_line = 372

    """ image loading """
    image = cv2.imread(pic_path, cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image, (image_w, image_h))

    mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    mask = cv2.resize(mask, (image_w, image_h))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR)
    
    # for i in range(len(mask)):
    #     for j in range(len(mask[i])):
    #         if (mask[i][j] == [0, 0, 0, 255]).all():
    #             mask[i][j] = [0, 0, 0, 0]

    # _,alpha = cv2.threshold(mask,0,255,cv2.THRESH_BINARY) # 투명
    
    b, g, r = cv2.split(image)
    alpha = mask.mean(axis=-1, keepdims=True)
    alpha = np.array(alpha).astype('uint8')
    crop_image = cv2.merge([b,g,r, alpha])
    
    # 검은배경 만들기
    for i in range(len(crop_image)):
        for j in range(len(crop_image[i])):
            if(crop_image[i][j][3] == 0).all():
                crop_image[i][j] = [0,0,0,255]
          
    # 턱 하단과 모델마스크 선까지의 거리 계산
    lip_arr = []
    for i in range(len(crop_image)):
        for j in range(len(crop_image[i])):   
            if(crop_image[i][j][0] == 177 and crop_image[i][j+2][0] == 177 and crop_image[i][j-2][0] == 177).all():
                lip_arr.append(hori_line-i)
    
    # 얼굴 내리기        
    dst = min(lip_arr)
    print(lip_arr)
    mov_img = np.zeros((512,512,4), np.uint8)
    
    for i in range(len(crop_image)):
        for j in range(len(crop_image[i])): 
            try:
                mov_img[i+dst][j] = crop_image[i][j]
                if(mov_img[i][j][3] == 0).all():
                    mov_img[i][j] = [0,0,0,255]
            except:
                pass

    # cv2.imshow("mov_img",mov_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite('C:\\data\\lapa\\LaPa\\results\\save3.png', mov_img)