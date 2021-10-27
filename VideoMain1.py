#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import cv2

# 捕获摄像头
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_fps = 25
video_format = cv2.VideoWriter_fourcc(*'mp4v')

video_file_fp = cv2.VideoWriter()
video_file_fp.open('camera_video.mp4', video_format, frame_fps, frameSize, True)

start_time = time.time()
video_time_length = 60
print('start to record video')

while True:
    sucess, video_frame = cap.read()
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cv2.putText(video_frame, time_str, (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    video_file_fp.write(video_frame)
    cv2.imshow('frame', video_frame)
    cur_time = time.time()
    if cur_time - start_time > video_time_length:
        print('End the video with ' + str(video_time_length) + ' s')
        break
    if cv2.waitKey(1) & 0xff == 27:  # esc key
        break


video_file_fp.release()
cap.release()
#os.system(f'ffmpeg -i "output.avi" -vcodec h264 "output.mp4"')
cv2.destroyAllWindows()


mp4_file_size = os.path.getsize('camera_video.mp4')
print(int(mp4_file_size/1024), 'KBytes')