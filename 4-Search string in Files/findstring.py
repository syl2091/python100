# coding=utf-8
import os
import sys


text = input("请输入搜索词:")
path = input("请输入路径:")


# 获取文件
def getfiles(path):
    f = 0
    # 路径集合
    arr = []
    os.chdir(path)
    files = os.listdir()
    # print(files)
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, 'r', encoding='UTF-8')
            if text in f.read():
                f = 1
                final_path = os.path.abspath(file_name)
                arr.append(final_path)
    if f == 0:
        print(text + "not found")
    if f == 1:
        print(text + "found in")
        print(arr)


getfiles(path)
