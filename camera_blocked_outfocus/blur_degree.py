import cv2
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret =False

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray_frame)

    text = "focused"
    if fm < 50:
        text = 'defocused'
    cv2.putText(frame, text, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, "{}: {:.2f}".format('blur degree', fm), (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("frame", frame)
    if cv2.waitKey(30) == 27 & 0xff:
        break
cap.release()
cv2.destroyAllWindows()
