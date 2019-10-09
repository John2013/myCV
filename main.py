import cv2 as cv

if __name__ == '__main__':
    cap = cv.VideoCapture('data/video.mkv')
    cars_cascade = cv.CascadeClassifier('haar/cars.xml')

    while True:
        ret, frame = cap.read()
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cars = cars_cascade.detectMultiScale(gray_frame, 1.3, 5)

        for (x, y, w, h) in cars:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv.imshow('frame', frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv.destroyAllWindows()
