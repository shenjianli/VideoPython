from os import mkdir
from os.path import isdir
import datetime
from time import sleep
import cv2

while True:
    # 参数0表示笔记本自带摄像头
    cap = cv2.VideoCapture(0)
    # 获取当前日期时间，例如，2021-10-26 14:26:30
    now = str(datetime.datetime.now())[:19].replace(':', "_")
    print(datetime.datetime.now())
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
    # 关闭摄像头
    cap.release()
    # 每15秒钟捕捉一次图像
    sleep(15)