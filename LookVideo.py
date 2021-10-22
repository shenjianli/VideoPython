import numpy as np
import cv2

cap = cv2.VideoCapture("o_reader_test.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2.imshow('0_reader_test', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
