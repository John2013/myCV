import numpy as np
import cv2 as cv

if __name__ == '__main__':
    # Load an color image in grayscale
    img = cv.imread('data/r3.jpg', 0)

    # cv.namedWindow('image', cv.WINDOW_NORMAL)
    # cv.imshow('image', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    cv.imwrite('data/r3_copy.png', img)

