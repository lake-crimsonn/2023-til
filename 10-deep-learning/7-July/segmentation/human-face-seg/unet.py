
import os # 출력 경고창 없애기
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2" 

from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPool2D, Conv2DTranspose, Concatenate, Input
from tensorflow.keras.models import Model

def conv_block(inputs, num_filters):
    x = Conv2D(num_filters, 3, padding="same")(inputs) 
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Conv2D(num_filters, 3, padding="same")(x)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    return x

def encoder_block(inputs, num_filters):
    x = conv_block(inputs, num_filters)
    p = MaxPool2D((2, 2))(x)
    return x, p

def decoder_block(inputs, skip, num_filters):
    # 일반적인 컨볼루션의 반대 방향으로 진행 up-conv
    x = Conv2DTranspose(num_filters, (2, 2), strides=2, padding="same")(inputs) # 스트라이드가 2라서 크기가 2배로 증가 32->64
    x = Concatenate()([x, skip]) # [64x64 512, 64x64 512] -> 64x64 1024
    x = conv_block(x, num_filters) # 64x64, 1024 -> 64x64, 512
    return x

def build_unet(input_shape, num_classes):
    inputs = Input(input_shape) # 512x512 3를 받아서 케라스텐서로 변경해줌
    
    s1, p1 = encoder_block(inputs, 64) # 512, 256 
    s2, p2 = encoder_block(p1, 128) # 256, 128
    s3, p3 = encoder_block(p2, 256) # 128,64
    s4, p4 = encoder_block(p3, 512) # 64, 32

    # 플래튼 시키면 위치정보를 잃어버리니까 컨블럭에 입력
    b1 = conv_block(p4, 1024) # 32x32 1024

    # 이전형태, 저장해둔 위치정보, 채널수
    d1 = decoder_block(b1, s4, 512) # 64x64 512 
    d2 = decoder_block(d1, s3, 256) # 128x128 256
    d3 = decoder_block(d2, s2, 128) # 256x256 128
    d4 = decoder_block(d3, s1, 64) # 512x512 64

    # 마지막은 클래스 수, 커널은 1, 멀티클래스니까 softmax
    outputs = Conv2D(num_classes, 1, padding="same", activation="softmax")(d4)

    model = Model(inputs, outputs) # 모델 인스턴스 생성
    return model

# 인터프리터에서 직접 실행이 되는 경
if __name__ == "__main__":
    input_shape = (512, 512, 3)
    model = build_unet(input_shape, 11)
    # model.summary()