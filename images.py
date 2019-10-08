import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('data/haarcascade_eye.xml')
    img = cv.imread('data/face.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0),
                         2)
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imwrite('data/face_detected.jpg', img)
    plt.imshow(rgb)
    plt.show()
