import cv2
import numpy as np
import matplotlib.pyplot as plt

# 迭代次数
#iter_time = 10

# 读入灰度图
img = cv2.imread("E:\pyCharm\ID3\save.tif", flags=cv2.IMREAD_GRAYSCALE)
#img2=cv2.imread("val_391.tif",flags=cv2.IMREAD_GRAYSCALE)

# 创建核
kernel = np.ones((2, 2),np.uint8)

# 保存原图像
#imgSave = img

# 闭运算
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 开运算
# opening = cv2.morphologyEx(closing4, cv2.MORPH_OPEN, kernel)

# 膨胀
# for i in range(2):
#     img=cv2.dilate(img, kernel)
# img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
# 腐蚀
# for j in range(2):
#     img = cv2.erode(img, kernel)
#
# canny=cv2.Canny(img,30,150)
cv2.imwrite('E:\pyCharm\ID3\save_close.tif', np.hstack(( closing,)))