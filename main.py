import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check, print_frame = video.read()
    cv2.imshow("My video", print_frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
video.release()