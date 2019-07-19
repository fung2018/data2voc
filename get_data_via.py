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


if __name__ == '__main__':
    json_path = 'via_project_19Jul2019_20h56m01s.json'
    save_folder = ''

    with open(json_path, 'r', encoding='utf-8') as f:
        temp = json.load(f)
        f.close()

    name_info = temp["file"]
    point_info = temp["metadata"]
    # print(name_info)
    name_list = []
    point_list = []
    for value in name_info.values():
        name_list.append(value)
        # print(value)

    for value in point_info.values():
        point_list.append(value)
        # print(value)

    for n in name_list:
        # print(n["fid"], n["fname"])
        img_name = n["fname"]
        name, _ = os.path.splitext(img_name)
        txt_name = name + '.txt'
        txt_path = os.path.join(save_folder, txt_name)
        for p in point_list:
            if n["fid"] == p["vid"]:
                # print(p["xy"][1:])
                points = p["xy"][1:]
                with open(txt_path, 'w', encoding='utf-8') as f:
                    f.write(img_name)
                    f.write('\n')
                    for i in range(0, len(points), 2):
                        f.writelines([str(points[i]), ',', str(points[i+1])])
                        f.write('\n')
            # print(p["vid"], p["xy"])
