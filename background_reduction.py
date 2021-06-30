import cv2

# reading video clip
cap = cv2.VideoCapture('videos/tum hi ho.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    if ret == True:
        cv2.imshow("original", frame)
        cv2.imshow("fg", fgmask)
    else:
        ret = False

    if cv2.waitKey(30) == 27:
        break

# releasing video capturing and destroying reading windows
cap.release()
cv2.destroyAllWindows()
