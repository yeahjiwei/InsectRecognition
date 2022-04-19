import os
import csv
from PIL import Image


def graph_size(txt_name):
    """
    获取图片尺寸
    """
    graphPath = './testimages/' + txt_name + ".jpg"
    img = Image.open(graphPath)
    width = img.width
    height = img.height
    return width, height


def convert(x_center, y_center, xmax, xmin, ymax, ymin):
    """
    计算yolo数据
    """
    # 图片宽度、高度
    width, height = graph_size(txt_name)
    x = x_center / int(width)
    y = y_center / int(height)
    w = (xmax - xmin) / int(width)
    h = (ymax - ymin) / int(height)
    return x, y, w, h

def class_id(classId):
    """
    虫子编号处理
    """
    if classId == '6':
        classId = '1'
    elif classId == '7':
        classId = '2'
    elif classId == '8':
        classId = '3'
    elif classId == '9':
        classId = '4'
    elif classId == '10':
        classId = '5'
    elif classId == '25':
        classId = '6'
    elif classId == '41':
        classId = '7'
    elif classId == '105':
        classId = '8'
    elif classId == '110':
        classId = '9'
    elif classId == '115':
        classId = '10'
    elif classId == '148':
        classId = '11'
    elif classId == '156':
        classId = '12'
    elif classId == '222':
        classId = '13'
    elif classId == '228':
        classId = '14'
    elif classId == '235':
        classId = '15'
    elif classId == '256':
        classId = '16'
    elif classId == '280':
        classId = '17'
    elif classId == '310':
        classId = '18'
    elif classId == '387':
        classId = '19'
    elif classId == '392':
        classId = '20'
    elif classId == '394':
        classId = '21'
    elif classId == '398':
        classId = '22'
    elif classId == '401':
        classId = '23'
    elif classId == '402':
        classId = '24'
    elif classId == '430':
        classId = '25'
    elif classId == '480':
        classId = '26'
    elif classId == '485':
        classId = '27'
    elif classId == '673':
        classId = '28'
    return classId


path = "./"
dirs = os.listdir(path)
for x in dirs:
    if os.path.splitext(x)[1] == ".csv":
        filePath = x
        break


with open(x, 'r') as f:
    data = csv.reader(f)
    for i in data:
        print(i)
        if i[0] != '序号':
            # print(i)
            if i[4] != '':
                # 中心点x坐标
                x_center = float(i[4])
                # 中心点y坐标
                y_center = float(i[5])

                xmax = float(i[8])
                xmin = float(i[6])
                ymax = float(i[9])
                ymin = float(i[7])
                x, y, w, h = convert(x_center, y_center, xmax, xmin, ymax, ymin)
            else:
                x, y, w, h = float(1), float(1), float(1), float(1)
            # 虫子编号
            classId = i[2]
            classId = class_id(classId)
            # 文件名
            splitext = os.path.splitext(i[1])
            txt_name = splitext[0]

            file = open('./labels/' + txt_name + '.txt', 'a+')
            file.write(str(classId) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)+'\n')
            file.close()

    print("done")
