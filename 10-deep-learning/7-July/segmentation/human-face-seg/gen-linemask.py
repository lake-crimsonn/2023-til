import cv2
import numpy as np

if __name__ == "__main__":
    
    
    """ image path """
    mask_path = "C:\\data\\lapa\\LaPa\\results\\mask_female.png"
    
    
    """ image size """
    image_h = 512
    image_w = 512
    filter_wh = 64

    """ image loading """
    mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    mask = cv2.resize(mask, (image_w, image_h))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR)
    mask_c = mask.copy()
    
    # 커널로 마스크 노이즈 제거
    kernel = np.ones((filter_wh,filter_wh,3), np.uint8)
    
    check_arr = []
    for i in range(len(kernel)):
        for j in range(len(kernel[i])):  
            if i == 0:
                kernel[i][j] = [0,0,0]   
                kernel[j][i] = [0,0,0]
            elif i == len(kernel)-1:
                kernel[j][i] = [0,0,0]
                kernel[i][j] = [0,0,0]

    stride = 1
    
    fillcnt = filter_wh * 4
    cnt = 0
    cnt2 = 0
    start_pos = 0
    i,j = start_pos, start_pos
    xst, yst = 0,0
    loop = 1
    while(loop == 1):
        
        if (i+yst) >= 448:
            loop = 0
        
        if (j+xst) >= 512:
            i += 1
            j = start_pos        
            xst = start_pos
             
        if j == filter_wh:
            j = start_pos
            xst += filter_wh
            
        if i == filter_wh:
            i = start_pos
            yst += filter_wh
            
        if (kernel[j][i] == mask[j+xst][i+yst]).all():
            cv2.line(mask_c,(j+xst,i+yst),(j+xst,i+yst),(0,0,255),1)
            cv2.line(mask_c,(i+yst,j+xst),(i+yst,j+xst),(0,0,255),1)
        
        j += 1
        
    
    cv2.imshow('rec', mask_c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                
    # # 라인 마스크 생성
    # linemask = np.zeros((512,512,3), np.uint8)
    
    # chin_arr = []
    # # 턱 하단과 모델마스크 선까지의 거리 계산
    # for i in range(len(mask)):
    #     for j in range(len(mask[i])):   
    #         if(mask[j][i][0] == 177 and mask[j+10][i][0] == 177 and mask[j-10][i][0] == 177).all():    
    #             chin_arr.append(j)
    #             cv2.line(linemask,(i,j),(i,j),(255,0,0),thickness=5)
                
    # dst = max(chin_arr)+10
    # print("dst:",dst)
    
    # cv2.rectangle(linemask, (0,dst),(512,512), (255,255,255), cv2.FILLED)

        