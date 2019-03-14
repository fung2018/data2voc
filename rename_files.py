# -*- coding:utf-8 -*-

import cv2
import os


def get_file_path(file_path):
    filenames = []
    sorted_path = os.listdir(file_path)
    sorted_path.sort()

    for filename in sorted_path:
        filename = os.path.join(file_path, filename)
        filenames.append(filename)
    return filenames


def check_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


def rename_image(image_paths, save_path):
    save_type = '.jpg'
    start_num = 1
    for image_path in image_paths:
        img = cv2.imread(image_path)
        # image_name = os.path.basename(image_path)
        # common_name = os.path.splitext(image_name)[0]
        num_update = ("{:0>6d}".format(start_num))
        new_path = os.path.join(save_path, num_update + save_type)
        print(new_path)
        # os.rename(image_path, new_path)
        cv2.imwrite(new_path, img)
        start_num += 1


def rename_file(file_paths, save_path):
    save_type = '.xml'
    start_num = 1
    for file_path in file_paths:
        num_update = ("{:0>6d}".format(start_num))
        new_path = os.path.join(save_path, num_update + save_type)
        print(new_path)
        os.rename(file_path, new_path)
        start_num += 1


if __name__ == '__main__':

    file_path = '/xxxxxx/'
    image_save_path = '/xxxxxxx/'
    image_save_path = check_path(image_save_path)

    file_paths = get_file_path(file_path)
    image_paths = file_paths[0::2]
    # json_paths = file_paths[1::2]

    xml_path = '/xxxxxx/'
    xml_save_path = '/xxxxxx/'
    xml_save_path = check_path(xml_save_path)
    xml_paths = get_file_path(xml_path)

    rename_image(image_paths, image_save_path)
    rename_file(xml_paths, xml_save_path)

    print("done!")
