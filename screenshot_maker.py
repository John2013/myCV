from os import remove, listdir
from os.path import join

import cv2 as cv


def clear_all(image_dir_paths, dat_paths):
    for image_dir_path in image_dir_paths:
        for image in listdir(image_dir_path):
            remove(join(image_dir_path, image))

    for dat_path in dat_paths:
        with open(dat_path, 'w') as _:
            pass


def save_bad(frame, count, image_dir_path, dat_path):
    image_name = f"{count}.jpg"
    path = join(image_dir_path, image_name)

    cv.imwrite(path, frame)

    with open(dat_path, 'a') as dat_file:
        path = join("bad", image_name)
        dat_file.write(f"{path}\n")


def cancel_bad(count, image_dir_path, dat_path):
    count -= 1

    image_name = f"{count}.jpg"
    path = join(image_dir_path, image_name)

    remove(path)

    with open(dat_path, 'r+') as dat_file:
        lines = dat_file.readlines()
        lines = lines[:-1]
        dat_file.writelines(lines)


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
global_frame = None


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False

        # draw a rectangle around the region of interest
        cv.rectangle(global_frame, refPt[0], refPt[1], (0, 255, 0), 2)
        cv.imshow("frame", global_frame)


if __name__ == '__main__':
    cap = cv.VideoCapture('data/piter2-720p.mp4')
    images_paths = [
        'learning/peoples/bad',
        'learning/peoples/good'
    ]
    dat_paths = [
        'learning/peoples/bad.dat',
        'learning/peoples/good.dat'
    ]

    esc, g, b, n, enter = 27, 103, 98, 110, 13

    good_cnt, bad_cnt = 0, 0

    clear_all(images_paths, dat_paths)

    cv.namedWindow("frame")
    cv.setMouseCallback("frame", click_and_crop)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv.imshow('frame', frame)
        key = cv.waitKey(30) & 0xff

        if key == esc:
            break
        elif key == g:
            global_frame = frame
            while True:
                key2 = cv.waitKey(30) & 0xff
                if key2 == enter:
                    break

        elif key == b:
            save_bad(frame, bad_cnt, images_paths[0], dat_paths[0])
            bad_cnt += 1
            print('bad count:', bad_cnt)
        elif key == n:
            cancel_bad(bad_cnt, images_paths[0], dat_paths[0])
            bad_cnt -= 1
            print('removed bad', bad_cnt)
        elif key != 255:
            print('key:', key)

    cap.release()
    cv.destroyAllWindows()
