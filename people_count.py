import cv2
import imutils
import datetime

width = 800
textIn = 0
textOut = 0


def testIntersectionIn(x, y):
    res = -450 * x + 400 * y + 157500
    if ((res >= -550) and (res < 550)):
        print(str(res))
        return True
    return False


def testIntersectionOut(x, y):
    res = -450 * x + 400 * y + 180000
    if ((res >= -550) and (res <= 550)):
        print(str(res))
        return True
    return False


cap = cv2.VideoCapture("videos/example_01.mp4")
firstFrame = None

while True:
    ret, frame = cap.read()
    text = "Unoccupied"

    if not ret:
        break

    frame = imutils.resize(frame, width=width)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    # absolute difference between the current frame and first frame
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 12000:
            continue
        # compute the bounding box for the contour, draw it on the frame, and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.line(frame, (width // 2, 0), (width, 450), (250, 0, 1), 2)
        cv2.line(frame, (width // 2 - 50, 0), (width - 50, 450), (0, 0, 255), 2)

        rectagleCenterPont = ((x + x + w) // 2, (y + y + h) // 2)
        cv2.circle(frame, rectagleCenterPont, 1, (0, 0, 255), 5)

        if (testIntersectionIn((x + x + w) // 2, (y + y + h) // 2)):
            textIn += 1

        if (testIntersectionOut((x + x + w) // 2, (y + y + h) // 2)):
            textOut += 1
        cv2.imshow("Thresh", thresh)
        cv2.imshow("Frame Delta", frameDelta)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.putText(frame, "In: {}".format(str(textIn)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "Out: {}".format(str(textOut)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.imshow("Security Feed", frame)

cap.release()
cv2.destroyAllWindows()
