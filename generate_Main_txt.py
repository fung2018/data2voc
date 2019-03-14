# -*- coding:utf-8 -*-

import os
import random


def check_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


# 标准的voc2007应该都是50%
train_val_percent = 0.66
train_percent = 0.5

txt_save_path = '/xxxxxx/'
txt_save_path = check_path(txt_save_path)
xml_path = '/xxxxxx/'
xml_path = check_path(xml_path)

xml_name_list = os.listdir(xml_path)
xml_num = len(xml_name_list)
xml_range = range(xml_num)

tv = int(xml_num * train_val_percent)
tr = int(xml_num * train_percent)

train_val = random.sample(xml_range, tv)
train = random.sample(train_val, tr)

file_train_val = open(txt_save_path+'trainval.txt', 'w')
file_test = open(txt_save_path+'test.txt', 'w')
file_train = open(txt_save_path+'train.txt', 'w')
file_val = open(txt_save_path+'val.txt', 'w')

for i in xml_range:
    name = xml_name_list[i][:-4]+'\n'
    if i in train_val:
        file_train_val.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_train_val.close()
file_train.close()
file_val.close()
file_test.close()

print("done!")



