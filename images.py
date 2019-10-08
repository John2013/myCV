import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    face_cascade = cv.CascadeClassifier(
        'data/haarcascade_frontalface_default.xml')
    eye_left_cascade = cv.CascadeClassifier(
        'data/haarcascade_lefteye_2splits.xml')
    # eye_right_cascade = cv.CascadeClassifier(
    #     'data/haarcascade_righteye_2splits.xml')
    img = cv.imread('data/face2.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes_left = eye_left_cascade.detectMultiScale(roi_gray)
        # eyes_right = eye_right_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes_left:
            cv.rectangle(
                roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )
        # for (ex, ey, ew, eh) in eyes_right:
        #     cv.rectangle(
        #         roi_color,
        #         (ex, ey),
        #         (ex + ew, ey + eh),
        #         (127, 127, 0),
        #         2
        #     )
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imwrite('data/face_detected.jpg', img)
    plt.imshow(rgb)
    plt.show()
