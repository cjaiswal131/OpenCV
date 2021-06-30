import cv2


# function to find hand gesture in images
def main():
    img = cv2.imread('images/hand.png')
    hand_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, th = cv2.threshold(hand_img, 75, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    hull = [cv2.convexHull(c) for c in contours]
    final = cv2.drawContours(hand_img, hull, -1, (255, 0, 0))

    cv2.imshow('original', img)
    cv2.imshow('thresholded', th)
    cv2.imshow('final', final)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
