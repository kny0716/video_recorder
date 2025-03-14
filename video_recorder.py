import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)
video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

target_format = "avi"
target_fourcc = "XVID"

result = None
recording = False
flip_mode = False
negative_mode = False

fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)


while True:
    vaild, img = video.read()
    if not vaild:
        break

    img_display = img.copy()

    if negative_mode: 
        img_display = 255 - img_display
        img = 255 - img

    if recording:
        cv.circle(img_display,(40, 40), 15, (0, 0, 255), -1 )
        cv.putText(img_display, "REC", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA) 
        result.write(img)

    cv.imshow("video_recorder", img_display)

    key = cv.waitKey(wait_msec)
    if key == ord(" "):
        if recording: 
            recording = False  
        else: 
            recording = True
            if result is None:
                result = cv.VideoWriter("result." + target_format, cv.VideoWriter_fourcc(*target_fourcc), video.get(cv.CAP_PROP_FPS), (img.shape[1], img.shape[0]))
    elif key == ord("n"): 
        if negative_mode:
            negative_mode = False
        else:
            negative_mode = True
    elif key == 27: 
        break
   

video.release()
if result is not None:
    result.release()
cv.destroyAllWindows()