import cv2
import numpy as np

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3, 3), np.uint8)

while True:
    ret, frame = cap.read()
    if (frame is None):
        print("camera is blocked")
        break
    else:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        a = 0
        bounding_rect = []
        fgmask = fgbg.apply(frame)
        fgmask = cv2.erode(fgmask, kernel, iterations=5)
        fgmask = cv2.dilate(fgmask, kernel, iterations=5)

        fm = variance_of_laplacian(gray_frame)
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i in range(0, len(contours)):
            bounding_rect.append(cv2.boundingRect(contours[i]))

        for i in range(0, len(contours)):
            if bounding_rect[i][2] >= 40 or bounding_rect[i][3] >= 40:
                a = a + (bounding_rect[i][2]) * bounding_rect[i][3]

            if fm < 40 or (a >= int(frame.shape[0]) * int(frame.shape[1]) / 3):
                cv2.putText(frame, "defocused", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                cv2.putText(frame, "{}: {:.2f}".format('blur degree', fm), (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            cv2.imshow('frame', frame)

        if cv2.waitKey(30) == 27 & 0xff:
            break
cap.release()
cv2.destroyAllWindows()