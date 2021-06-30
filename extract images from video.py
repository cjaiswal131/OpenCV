import cv2
import os

try:
    # creating a folder named data
    print('folder created')
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

cam = cv2.VideoCapture("/home/hinclude/opencv_project/videos/tum hi ho.mp4")
currentframe = 0
while True:
    ret, frame = cam.read()
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()