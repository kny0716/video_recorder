import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)
video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

target_format = "avi"
target_fourcc = "XVID"

result = None
recordig = False

fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)


while True:
    vaild, img = video.read()
    if not vaild:
        break

    img_display = img.copy()

    if recordig:
        cv.circle(img_display,(50, 50), 20, (0, 0, 255), -1 )
        if result is None:
            result = cv.VideoWriter("result." + target_format, cv.VideoWriter_fourcc(*target_fourcc), video.get(cv.CAP_PROP_FPS), (img.shape[1], img.shape[0]))
        else:
            result.write(img)

    cv.imshow("video_recorder", img_display)

    key = cv.waitKey(wait_msec)
    if key == ord(" "):
        if recordig: # preview모드로 변경
            recordig = False  
        else: # record 모드로 변경
            recordig = True
    elif key == 27: # ESC 키를 누르면 종료
        break
   

video.release()
if result is not None:
    result.release()
cv.destroyAllWindows()