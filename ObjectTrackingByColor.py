import cv2
import numpy as np

# Tracking object by color in live video
def main():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([100, 50, 50])
        upper = np.array([130, 255, 255])
        image_mask = cv2.inRange(hsv, lower, upper)

        output = cv2.bitwise_and(frame, frame, mask=image_mask)

        # showing different image frame.
        cv2.imshow('roiginal frame', frame)
        cv2.imshow('image_mask', image_mask)
        cv2.imshow('color tracking', output)

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    main()
