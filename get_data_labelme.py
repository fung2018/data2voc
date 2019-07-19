import os
import json


def get_file_path_with_type(file_path, file_type):
    file_paths = []
    root_dir = os.walk(file_path)

    for sub_dir, folder_name, file_list in root_dir:
        for file_name in file_list:
            file_path = os.path.join(sub_dir, file_name)
            if file_type in file_path:
                file_paths.append(file_path)
    file_paths = sorted(file_paths)
    return file_paths


def save_txt(json_path, save_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        temp = json.load(f)
        f.close()

    img_name = temp["imagePath"]
    points = temp["shapes"][0]['points']
    name, _ = os.path.splitext(img_name)
    txt_name = name + '.txt'
    txt_path = os.path.join(save_path, txt_name)

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(img_name)
        f.write('\n')
        for point in points:
            f.writelines([str(point[0]), ',', str(point[1])])
            f.write('\n')
    # return img_name


if __name__ == '__main__':
    folder = 'xxxxxxxxx'

    json_paths = get_file_path_with_type(folder, '.json')
    for path in json_paths:
        save_txt(path, folder)
