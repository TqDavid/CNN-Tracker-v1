import skvideo.io
import cv2

reader = skvideo.io.FFmpegReader("/Users/timomueller/Desktop/demo-video-single.avi");

frame = 100

i = 0
for img in reader.nextFrame():
    i=i+1
    if(i==frame):
        break

for img in reader.nextFrame():
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    # Continue until the user presses ESC key
    if cv2.waitKey(1) == 27:
        break