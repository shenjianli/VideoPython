from os import mkdir
from os.path import isdir
import datetime
from time import sleep
import cv2

# 正常运行 摄像头捕捉当前图像保存当前图片（摄像头会一直开着，监控容易被发现）
# 参数0表示笔记本自带摄像头
cap = cv2.VideoCapture(0)
while True:
    # 获取当前日期时间，例如，2021-10-26 14:26:30
    now = str(datetime.datetime.now())[:19].replace(':', "_")
    print("当前时间：", now)
    if not isdir(now[:10]):
        mkdir(now[:10])
    # 捕捉当前图像，ret = True表示成功 False 表示失败
    ret, frame = cap.read()
    if ret:
        # 保存图像，以当前日期时间为文件名
        fn = now[:10] + '/' + now + '.jpg'
        cv2.imwrite(fn, frame)
        print("保存监控图片：", fn)
    # 每5秒钟捕捉一次图像
    sleep(5)