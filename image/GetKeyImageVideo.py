from PIL import Image
import cv2


# 把视频分拆为图片帧
def split_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    num = 1
    while True:
        success, data = cap.read()
        if not success:
            break
        im = Image.fromarray(data)
        im.save('split_{}.jpg'.format(str(num)))
        num = num + 1
        print('split_{}.jpg 保存完成'.format(str(num)))
    cap.release()


split_frames("camera_video.mp4")