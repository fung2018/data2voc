
import os


def get_file_path(file_path):
    filenames = []
    sorted_path = os.listdir(file_path)
    sorted_path.sort()

    for filename in sorted_path:
        filename = os.path.join(file_path, filename)
        filenames.append(filename)
    return filenames


def get_file_path_with_type(file_path, file_type):
    filenames = []
    sorted_path = os.listdir(file_path)
    sorted_path.sort()

    for filename in sorted_path:
        if os.path.splitext(filename)[1] == file_type:
            filename = os.path.join(file_path, filename)
            filenames.append(filename)
    return filenames


def check_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


def get_file_name(file_path):
    file_full_name = os.path.basename(file_path)
    file_name, extension_name = os.path.splitext(file_full_name)
    if os.path.isfile(file_path):
        return file_name
    else:
        return False

