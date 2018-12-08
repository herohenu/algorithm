#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/24 下午7:46 
# @Author : lavin
# @File : exercises2.py
# Exercise (2). 定义文件 xx.tar.gz 的产生方式如下:
# 	• 以 xx 为文件名的文件通过 tar 和 gzip 打包压缩产生，该文件中以字符串的方式记录
# 了一个非负整数;
# 	• 或者以 xx 为名的目录通过 tar 和 gzip 打包压缩产生，该目录中包含若干 xx.tar.gz。
# 其中，x ∈ [0, 9]。现给定一个根据上述定义生成的文件 00.tar.gz (该文件从课程网站下 载)，请确定其中包含的以 xx 为文件名的文件个数以及这些文件中所记录的非负整数之和
import os
import tarfile

sum = 0
lineNum = 0
tarnum = 0

def travel_node(path):
    global tarnum
    if os.path.isdir(path):
        os.chdir(path)
        for file in os.listdir(path):
            if os.path.isdir(file):
                continue
            else:
                if ".tar.gz" in file:
                    unpack_path_file(path, file)
    else:
        readContent(path)


def readContent(file):
    global sum
    global lineNum
    f = open(file, 'r')
    for line in f:
        lineNum += 1
        line = line.replace("\n", "", -1)
        line = line.replace(" ", "", -1)
        if line.isdigit() and int(line) > 0:
            sum += int(line)
        else:
            continue


def unpack_path_file(path, zipfile):
    global tarnum
    tarnum += 1
    os.chdir(path)
    archive = tarfile.open(zipfile)
    for tarinfo in archive:
        archive.extract(tarinfo, os.getcwd())
    archive.close()
    i = zipfile.index(".tar.gz")
    newpath = os.getcwd() + os.sep + zipfile[:i]
    travel_node(newpath)


if __name__ == '__main__':
    unpack_path_file(".", "00.tar.gz")
    print("sum is ", sum)
    print("tarnum is:", tarnum)
