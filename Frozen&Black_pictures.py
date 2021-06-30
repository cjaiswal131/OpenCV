import cv2
import os


# function to check given image is black image or frozen image
def black_and_frozen_image():
    # image path on my local directory
    path1 = 'images/frozen4.jpeg'
    frozen_img = cv2.imread(path1, 1)

    for file_type in ['neg']:
        for img in os.listdir(file_type):
            try:
                current_image_path = str(file_type) + '/' + str(img)
                match = cv2.imread(current_image_path)

                if frozen_img.shape == match.shape:
                    cv2.imshow('frozen_image', frozen_img)
                else:
                    cv2.imshow('black_image', match)

            except Exception as e:
                print(str(e))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    black_and_frozen_image()
