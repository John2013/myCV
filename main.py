import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load an color image in grayscale
    img = cv.imread('data/r3.jpg', 0)
    cv.imshow('image', img)
    k = cv.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv.destroyAllWindows()
    elif k == ord('s'):  # wait for 's' key to save and exit
        cv.imwrite('data/r3_copy.png', img)
        cv.destroyAllWindows()
