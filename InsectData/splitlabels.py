"""
划分标签
"""

import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = ['无（不含虫子）','大螟','二化螟','稻纵卷叶螟','白背飞虱','褐飞虱属',
        '地老虎','蝼蛄','粘虫','草地螟','甜菜夜蛾','黄足猎蝽',
        '八点灰灯蛾','棉铃虫','二点委夜蛾','甘蓝夜蛾','蟋蟀','黄毒蛾',
        '稻螟蛉','紫条尺蛾','水螟蛾','线委夜蛾','甜菜白带野螟','歧角螟',
        '瓜绢野螟','豆野螟','石蛾','大黑鳃金龟','干纹冬夜蛾']
abs_path = os.getcwd()
print(abs_path)

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h

def convert_annotation(image_id):
    in_file = open('./annotations/%s.xml' % (image_id), encoding='gb2312')
    out_file = open('./labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # difficult = obj.find('Difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()
for image_set in sets:
    if not os.path.exists('./labels/'):
        os.makedirs('./labels/')
    image_ids = open('./imagesets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('./%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(abs_path + '/trainvalimages/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
