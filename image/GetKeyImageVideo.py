from PIL import Image
import cv2


def split_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    num = 1
    while True:
        success, data = cap.read()
        if not success:
            break
        im = Image.fromarray(data)
        im.save(str(num) + '.jpg')
        num = num + 1
        print("")
    cap.release()


split_frames("camera_video.mp4")