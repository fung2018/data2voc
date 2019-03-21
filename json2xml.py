# -*- coding:utf-8 -*-

import xml.dom.minidom
import json
import os
import datetime
import cv2


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


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


def read_json(json_path):

    with open(json_path, 'r', encoding='utf-8') as json_file:
        temp = json.load(json_file)
        json_file.close()

    temp_list = temp['labels']
    return temp_list


def get_date():
    time_now = datetime.datetime.now()
    year = str(time_now.year)
    month = str(time_now.month)
    day = str(time_now.day)
    date_format = str(year + '-' + month + '-' + day)
    return date_format


def json_to_xml(file_path, save_path):
    file_paths = get_file_path_with_type(file_path, '.json')
    
    image_paths = file_paths
    json_paths = file_paths

    

#     for path_i in file_paths:
#         if '.DS_Store' in path_i:
#             file_paths.pop(file_paths.index(path_i))

#     image_paths = file_paths[0::2]
#     json_paths = file_paths[1::2]

    i = 0
    for json_path in json_paths:
        print(json_path)

        doc = xml.dom.minidom.Document()
        root = doc.createElement('annotation')
        doc.appendChild(root)

        node_folder = doc.createElement('folder')
        node_folder.appendChild(doc.createTextNode(get_date()))
        root.appendChild(node_folder)

        image_name = os.path.basename(image_paths[i])
        common_name = os.path.splitext(image_name)[0]

        node_filename = doc.createElement('filename')
        node_filename.appendChild(doc.createTextNode(image_name))
        root.appendChild(node_filename)

        node_path = doc.createElement('path')
        node_path.appendChild(doc.createTextNode(image_paths[i]))
        root.appendChild(node_path)

        node_source = doc.createElement('source')
        node_database = doc.createElement('database')
        node_database.appendChild(doc.createTextNode('Unknown'))
        node_source.appendChild(node_database)
        root.appendChild(node_source)

        print(image_paths[i])
#         img = cv2.imread(image_paths[i])
#         width, height, channels = img.shape
        
        width, height, channels = [800, 600, 3]

        node_size = doc.createElement('size')
        node_width = doc.createElement('width')
        node_width.appendChild(doc.createTextNode(str(width)))
        node_height = doc.createElement('height')
        node_height.appendChild(doc.createTextNode(str(height)))
        node_depth = doc.createElement('depth')
        node_depth.appendChild(doc.createTextNode(str(channels)))
        node_size.appendChild(node_width)
        node_size.appendChild(node_height)
        node_size.appendChild(node_depth)
        root.appendChild(node_size)

        node_segmented = doc.createElement('segmented')
        node_segmented.appendChild(doc.createTextNode('0'))
        root.appendChild(node_segmented)

        label_content = read_json(json_path)

        for label_num in range(len(label_content)):

            name = label_content[label_num]['name']

            node_object = doc.createElement('object')
            node_name = doc.createElement('name')
            node_name.appendChild(doc.createTextNode(name))
            node_pose = doc.createElement('pose')
            node_pose.appendChild(doc.createTextNode('Unspecified'))
            node_truncated = doc.createElement('truncated')
            node_truncated.appendChild(doc.createTextNode('0'))
            node_difficult = doc.createElement('difficult')
            node_difficult.appendChild(doc.createTextNode('0'))

            node_object.appendChild(node_name)
            node_object.appendChild(node_pose)
            node_object.appendChild(node_truncated)
            node_object.appendChild(node_difficult)

            xmin = str(label_content[label_num]['x1'])
            ymin = str(label_content[label_num]['y1'])
            xmax = str(label_content[label_num]['x2'])
            ymax = str(label_content[label_num]['y2'])

            node_bndbox = doc.createElement('bndbox')
            node_xmin = doc.createElement('xmin')
            node_xmin.appendChild(doc.createTextNode(xmin))
            node_ymin = doc.createElement('ymin')
            node_ymin.appendChild(doc.createTextNode(ymin))
            node_xmax = doc.createElement('xmax')
            node_xmax.appendChild(doc.createTextNode(xmax))
            node_ymax = doc.createElement('ymax')
            node_ymax.appendChild(doc.createTextNode(ymax))
            node_bndbox.appendChild(node_xmin)
            node_bndbox.appendChild(node_ymin)
            node_bndbox.appendChild(node_xmax)
            node_bndbox.appendChild(node_ymax)

            node_object.appendChild(node_bndbox)

            root.appendChild(node_object)

        xml_path = save_path + common_name + '.xml'
        xml_file = open(xml_path, 'w')
        doc.writexml(xml_file, addindent='\t', newl='\n', encoding="utf-8")

        i += 1


if __name__ == '__main__':

    json_path_ = '/xxxxxxx/'
    save_path_ = '/xxxxxxx/'
    save_path_ = check_path(save_path_)
    del_file(save_path_)

    json_to_xml(json_path_, save_path_)
    print("done!")

