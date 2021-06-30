# importing libraries
import numpy as np
import cv2


def detect(frame, step_size, feature_scale, frame_vound):
    detector = cv2.FastFeatureDetector_create()
    return detector.detect(frame)

# capturing live video
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while True:
    ret, frame = cap.read()
    frame_sift = np.copy(frame)
    gray_frame = cv2.cvtColor(frame_sift, cv2.COLOR_BGR2GRAY)
    keypoints = detect(frame, 20, 20, 5)
    dense_frame = cv2.drawKeypoints(gray_frame, keypoints, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('original frame', frame)
    cv2.imshow('dense frame', dense_frame)

    if cv2.waitKey(1) == 27:
        break

#  releasing video capturing variable and destroying video window
cap.release()
cv2.destroyAllWindows()
