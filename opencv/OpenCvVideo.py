from os import mkdir
from os.path import isdir
import datetime
from time import sleep
from threading import Thread
from shutil import copyfile
import cv2

# 正常运行，录制视频

# 参数0表示笔记本自带摄像头
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_fps = 25
video_format = cv2.VideoWriter_fourcc(*'mp4v')


now = str(datetime.datetime.now())[:19].replace(':', '_')
dirName = now[:10]
tempAviFile = dirName + '/' + now + '.mp4'
if not isdir(dirName):
    mkdir(dirName)

aviFile = cv2.VideoWriter()
aviFile.open(tempAviFile, video_format, frame_fps, frameSize, True)


def write():
    while cap.isOpened():
        ret, frame = cap.read()
        print("开始写入视频", ret)
        if ret:
            aviFile.write(frame)
    aviFile.release()


Thread(target=write).start()
input("输入结束录制")
aviFile.release()
cap.release()

