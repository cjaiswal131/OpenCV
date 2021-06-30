# importing cv2 library
import cv2


# drawing rectangular boundary on face, mouth, eyes
def draw_boundary(img, classifier, scalFactor, minNeighbors, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scalFactor, minNeighbors)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords


# detecting face, mouth, nose, eyes
def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")

    if len(coords) == 4:
        roi_img = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]
        coords = draw_boundary(roi_img, eyeCascade, 1.1, 14, color['red'], "eye")
        coords = draw_boundary(roi_img, noseCascade, 1.1, 10, color['green'], "nose")
        coords = draw_boundary(roi_img, mouthCascade, 1.1, 20, color['white'], "mouth")
    return img


# different classifier path
faceCascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_eye.xml')
noseCascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/nariz.xml')
mouthCascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/mouth.xml')

cap = cv2.VideoCapture(-1)

while True:
    _, img = cap.read()
    img = detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade)
    cv2.imshow('face_detection', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()
