import numpy as np
import cv2 as cv

if __name__ == '__main__':
    # Load an color image in grayscale
    img = cv.imread('data/r3.jpg', 0)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

