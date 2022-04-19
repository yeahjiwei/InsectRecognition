
"""
将测试用的图片与训练图片分开
"""

import os
import shutil


# 移动文件
def remove_file(old_path, txtpath, new_path):
    print(old_path)
    print(new_path)
    filelist = os.listdir(old_path) #列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
    txtlist = os.listdir(txtpath)
    # print(filelist)

    for file in filelist:
        for txt in txtlist:

            if file[0:5] == txt[0:5]:
                src = os.path.join(old_path, file)
                dst = os.path.join(new_path, file)
                print('src:', src)
                print('dst:', dst)
                shutil.move(src, dst)


if __name__ == '__main__':
    remove_file(r"testimages", r"./labels", r"trainvalimages")


