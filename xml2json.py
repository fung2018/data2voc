
import xmltodict
from PIL import Image
import json
import os
import path_and_files as pf


def xml2json(xml_path):
    xml_file = open(xml_path, 'rb')
    xml_str = xml_file.read()

    json_file = xmltodict.parse(xml_str)
    json_file = json.loads(json.dumps(json_file))

    return json_file


def save_json(path, name, data):
    with open(path + name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
        json_file.close()


def batch2json(xml_path, save_path):
    file_type = '.xml'
    xml_files = pf.get_file_path_with_type(xml_path, file_type)

    for xml_file in xml_files:
        xml_name = pf.get_file_name(xml_file)
        data = xml2json(xml_file)
        json_name = xml_name + '.json'

        temp_list = data['annotation']['object']
        #     print(temp_list)
        #     print(type(temp_list))
        new_dict = {}
        new_list = []

        if isinstance(temp_list, list):
            for i in range(len(temp_list)):
                dict_cell = {}
                dict_cell['name'] = temp_list[i]['name']
                #         print(dict_cell['label_name'])
                #         str to int
                x1 = int(temp_list[i]['bndbox']['xmin'])
                y1 = int(temp_list[i]['bndbox']['ymin'])
                x2 = int(temp_list[i]['bndbox']['xmax'])
                y2 = int(temp_list[i]['bndbox']['ymax'])
                dict_cell['x1'] = x1
                dict_cell['y1'] = y1
                dict_cell['x2'] = x2
                dict_cell['y2'] = y2

                new_list.append(dict_cell)
        else:
            dict_cell = {}
            dict_cell['name'] = temp_list['name']
            x1 = int(temp_list['bndbox']['xmin'])
            y1 = int(temp_list['bndbox']['ymin'])
            x2 = int(temp_list['bndbox']['xmax'])
            y2 = int(temp_list['bndbox']['ymax'])
            dict_cell['x1'] = x1
            dict_cell['y1'] = y1
            dict_cell['x2'] = x2
            dict_cell['y2'] = y2

            new_list.append(dict_cell)

        new_dict.update(labels=new_list)
        # return new_dict

        save_json(save_path, json_name, new_dict)
        print(json_name)


if __name__ == '__main__':

    xml_path_ = '/Users/a/Desktop/test_set/test_anno/'
    save_path_ = '/Users/a/Desktop/test_set/test_json/'
    save_path_ = pf.check_path(save_path_)

    batch2json(xml_path_, save_path_)










