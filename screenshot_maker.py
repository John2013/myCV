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

    esc, g, b, n = 27, 103, 98, 110

    good_cnt, bad_cnt = 0, 0

    clear_all(images_paths, dat_paths)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv.imshow('frame', frame)
        key = cv.waitKey(30) & 0xff

        if key == esc:
            break
        elif key == g:
            pass
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
