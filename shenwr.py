# --** coding="UTF-8" **--
#


import os
import re
import sys
import math
import ffmpeg
import threading
import subprocess
from moviepy.editor import *


#文件大小的转换
__all__ = ['size_dx']


def size_dx(size, dot=2):
    size = float(size)
    # 位 比特 bit
    if 0 <= size < 1:
        human_size = str(round(size / 0.125, dot)) + 'b'
    # 字节 字节 Byte
    elif 1 <= size < 1024:
        human_size = str(round(size, dot)) + 'B'
    # 千字节 千字节 Kilo Byte
    elif math.pow(1024, 1) <= size < math.pow(1024, 2):
        human_size = str(round(size / math.pow(1024, 1), dot)) #+ 'KB'
    # 兆字节 兆 Mega Byte
    elif math.pow(1024, 2) <= size < math.pow(1024, 3):
        human_size = str(round(size / math.pow(1024, 2), dot)) #+ 'MB'
    # 吉字节 吉 Giga Byte
    elif math.pow(1024, 3) <= size < math.pow(1024, 4):
        human_size = str(round(size / math.pow(1024, 3), dot)) #+ 'GB'
    # 太字节 太 Tera Byte
    elif math.pow(1024, 4) <= size < math.pow(1024, 5):
        human_size = str(round(size / math.pow(1024, 4), dot)) #+ 'TB'
    # 拍字节 拍 Peta Byte
    elif math.pow(1024, 5) <= size < math.pow(1024, 6):
        human_size = str(round(size / math.pow(1024, 5), dot)) + 'PB'
    # 艾字节 艾 Exa Byte
    elif math.pow(1024, 6) <= size < math.pow(1024, 7):
        human_size = str(round(size / math.pow(1024, 6), dot)) + 'EB'
    # 泽它字节 泽 Zetta Byte
    elif math.pow(1024, 7) <= size < math.pow(1024, 8):
        human_size = str(round(size / math.pow(1024, 7), dot)) + 'ZB'
    # 尧它字节 尧 Yotta Byte
    elif math.pow(1024, 8) <= size < math.pow(1024, 9):
        human_size = str(round(size / math.pow(1024, 8), dot)) + 'YB'
    # 千亿亿亿字节 Bront Byte
    elif math.pow(1024, 9) <= size < math.pow(1024, 10):
        human_size = str(round(size / math.pow(1024, 9), dot)) + 'BB'
    # 百万亿亿亿字节 Dogga Byte
    elif math.pow(1024, 10) <= size < math.pow(1024, 11):
        human_size = str(round(size / math.pow(1024, 10), dot)) + 'NB'
    # 十亿亿亿亿字节 Dogga Byte
    elif math.pow(1024, 11) <= size < math.pow(1024, 12):
        human_size = str(round(size / math.pow(1024, 11), dot)) + 'DB'
    # 万亿亿亿亿字节 Corydon Byte
    elif math.pow(1024, 12) <= size:
        human_size = str(round(size / math.pow(1024, 12), dot)) + 'CB'
    # 负数
    else:
        raise ValueError('{}() takes number than or equal to 0, but less than 0 given.'.format(pybyte.__name__))
    return human_size

#重命名
def rename(path,banben):
    # 对目录下的文件进行遍历

    conghu8 = 1
    conghu3 = 1
    conghu9 = 1

   # path = os.getcwd()  # 获取当面路径
    fileList = os.listdir(path)  # 获取当前路径下文件

    for file in fileList:

        # 判断是否是视频（以.mp4结尾）
        if (file.endswith(".mp4")):
            print("重命名：" + file)

            # 设置新文件名
            file = path + '\\' + file
            prefix = os.path.splitext(file)[0]  # os.path.splitext() 将文件名和扩展名分开
            fix = os.path.splitext(file)[1]  # os.path.splitext() 获取扩展名

            filesize = os.path.getsize(file)       # 获取文件的大小（字节）
            filesize = float(size_dx(filesize))    # 把 字节 换算成 兆

            if (filesize < 30.00 ) :

                Name1 = prefix.rpartition('-')  # 获取版号跟命名
                Name = Name1[0] + "-" + banben + "(30M)"
                newName = Name + fix

                if newName == file :            #如果原文件名是否正确，不替换
                    continue

                if newName in fileList:
                    newName = Name + "-有重复"+ str(conghu3) + fix       #判断是否会重复命名，会的命名标出
                    conghu3 += 1

                os.rename(os.path.join(path, file), os.path.join(path, newName))

            elif(30.00 <filesize<80.00):

                Name1 = prefix.rpartition('-')  # 获取版号跟命名
                Name = Name1[0] + "-" + banben + "(80M)"
                newName = Name + fix

                if newName == file :            #如果原文件名是否正确，不替换
                    continue

                if newName in fileList:
                    newName = Name + "-有重复" + str(conghu8) + fix  # 判断是否会重复命名，会的命名标出
                    conghu8 += 1

                os.rename(os.path.join(path, file), os.path.join(path, newName))

            else:

                Name1 = prefix.rpartition('-')  # 获取版号跟命名
                Name = Name1[0] + "-超过80M"
                newName =Name + fix

                if newName == file :            #如果原文件名是否正确，不替换
                    continue

                if newName in fileList:
                    newName = Name + "-有重复"+ str(conghu9) + fix
                    conghu9 += 1
                os.rename(os.path.join(path, file), os.path.join(path, newName))

#压缩
def compress(path,fileList):

    for filename in fileList:

        if filename.endswith(".mp4"):
            print("开始压缩：" + filename)
            path_file = '"' + path +"\\" + filename + '"'        #文件的绝对地址

            path_file1 = path + "\\" + filename

            prefix = os.path.splitext(filename)[0]  # 将文件名和扩展名分开
            fix = os.path.splitext(filename)[1]    # 获取扩展名


             #获取视频属性
            info = ffmpeg.probe(path_file1)  # 获取文件信息

            for c in info['streams']:
                if c['codec_type'] == 'video':  # 匹配视频部分属性
                    vs = c
                    codec_name = vs['codec_name']  # 编码方式
                    duration = float(vs['duration'])  # 时长
                    fps = vs['r_frame_rate']  # 帧数
                    width = vs['width']
                    height = vs['height']
                    profile = vs['profile']  # 编码档次

                if c['codec_type'] == 'audio':  # 匹配音频部分
                    vs = c
                    au_bit = float(vs['bit_rate']) / 1000.00
                    # 获取音频码率,换算成 kb,如果衡量带宽（数据传输速率）即每秒钟传输的二进制位数，则1kb/s=1000b/s，是十进制的。
                    # 如果表示数据存储，则1Kb=1024b，是二进制的。

            filesize1 = float(info['format']['size'])  # 获取大小，换算成 M
            filesize = float(size_dx(filesize1))

            #计算新码率
            if filesize > 30.00 :
                new_bit = (30.00 * 8.00 / duration * 1024.00 - au_bit)       #为了确保压缩后肯定小于30M，所以这里除以1024，而不是除以1000
                new_bit = str(new_bit) + 'k'
                print('new_bit30:' + new_bit)

                newpath_file = '"' + path + "\\" + prefix + "压缩30M" + fix + '"'  # 压缩后的名字和路径

                #2pass压缩
                compress1 = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 1 -an -f mp4 -y NUL".format(path_file,new_bit, )
                os.system(compress1)

                compress = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 2 {}".format(path_file,new_bit, newpath_file)
                os.system(compress)

            if filesize > 80.00 :

                new_bit8 = (80.00 * 8.00 / duration * 1024.00 - au_bit)
                new_bit8 = str(new_bit8) + 'k'
                newpath_file8 = '"' + path + "\\" + prefix + "压缩80M" + fix + '"'  # 压缩后的名字和路径

                compress1 = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 1 -an -f mp4 -y NUL".format(path_file, new_bit8, )
                os.system(compress1)

                compress = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 2 {}".format(path_file, new_bit8, newpath_file8)
                os.system(compress)


    #删除第一次编码生成的视频解析文件

    fileList2 = os.listdir(path)

    for filename2 in fileList2:
        if filename2.endswith(".log"):

            path1 =path + "\\" + "ffmpeg2pass-0.log"
            path2 =path + "\\" + "ffmpeg2pass-0.log.mbtree"

            os.remove(path1)
            os.remove(path2)

def yasuo(path,size):

    fileList = os.listdir(path)

    for filename in fileList:

        if filename.endswith(".mp4"):

            path_file = '"' + path + "\\" + filename + '"'  # 文件的绝对地址

            path_file1 = path + "\\" + filename

            prefix = os.path.splitext(filename)[0]  # 将文件名和扩展名分开
            fix = os.path.splitext(filename)[1]  # 获取扩展名

            # 获取视频属性
            info = ffmpeg.probe(path_file1)  # 获取文件信息

            for c in info['streams']:
                if c['codec_type'] == 'video':  # 匹配视频部分属性
                    vs = c
                    duration = float(vs['duration'])  # 时长

                if c['codec_type'] == 'audio':  # 匹配音频部分
                    vs = c
                    au_bit = float(vs['bit_rate']) / 1000.00
                    # 获取音频码率,换算成 kb,如果衡量带宽（数据传输速率）即每秒钟传输的二进制位数，则1kb/s=1000b/s，是十进制的。
                    # 如果表示数据存储，则1Kb=1024b，是二进制的。

            # 计算新码率
            size = float(size)
            new_bit = (size * 8.00 / duration * 1024.00 - au_bit)  # 为了确保压缩后肯定小于30M，所以这里除以1024，而不是除以1000
            new_bit = str(new_bit) + 'k'
            print('new_bit30:' + new_bit)

            newpath_file = '"' + path + "\\" + prefix + "-压缩" + fix + '"'  # 压缩后的名字和路径

            # 2pass压缩
            compress1 = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 1 -an -f mp4 -y NUL".format(path_file, new_bit)
            os.system(compress1)

            compress = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 2 {}".format(path_file, new_bit, newpath_file)
            os.system(compress)

#查看视频属性
def video_info(file):

    info = ffmpeg.probe(file)  # 获取文件信息

    print(info)
    print("---------------------------------")

    for c in info['streams']:
        if c['codec_type'] == 'video':  # 匹配视频部分属性
            vs = c
            codec_name = vs['codec_name']  # 编码方式
            duration = float(vs['duration'])  # 时长
            fps = vs['r_frame_rate']  # 帧数
            width = vs['width']
            height = vs['height']
            profile = vs['profile']            #编码档次


            print("\ncodec_name:{} \nduration:{} \nwidth:{} \nheight:{} \nfps：{} \nprofile :{}".format(codec_name,duration,width,height,fps,profile))

        if c['codec_type'] == 'audio':  # 匹配音频部分
            vs = c
            au_bit = int(vs['bit_rate']) / 1000  #获取音频码率,换算成 kb,如果衡量带宽（数据传输速率）即每秒钟传输的二进制位数，则1kb/s=1000b/s，是十进制的。如果表示数据存储，则1Kb=1024b，是二进制的。
            print("\naudio_bit_rate:{}".format(au_bit))

    filesize1 = int(info['format']['size'])  # 获取大小，换算成 M
    filesize = float(size_dx(filesize1))

    print("\nfilesize:{}".format(filesize))

#去掉文件名的空格
def qukongge(path,fileList):

    for file in fileList:
        # 判断是否是视频（以.mp4结尾）
        if file.endswith(".mp4"):
            newName = file.replace(" ",'')
            os.rename(os.path.join(path, file), os.path.join(path, newName))

#格式转换
def geshi(path):
    fileList = os.listdir(path)  # 获取当前路径下文件
    ges = [".mp4",".avi",".mkv",".mov",".flv",".wmv",".m4v"]

    for filename in fileList:
        fix = os.path.splitext(filename)[1]  # 获取扩展名

        if fix in ges:
            prefix = os.path.splitext(filename)[0]  # 将文件名和扩展名分开

            file_path = '"' + path + "\\" + filename + '"'
            newname = '"' + path + "\\" + prefix + ".mp4"+'"'

            compress = "ffmpeg -i {}  -vcodec libx264  -y {}".format(file_path, newname)
            os.system(compress)

#x序列帧重命名
def xulz(path):
    # 要修改什么类型的文件
    fileType = '.png'
    # 前缀
    # front = 'bsa_show'
   # front = input("请输出前缀：")
    # 后缀
    back = ''
    # 是否保留原文件名字 True False
    old = False

    fileList = os.listdir(path)
    # 名称变量
    num = 1
    # 遍历文件夹中所有文件
    for fileName in fileList:
        prefix = os.path.splitext(fileName)[0]  # os.path.splitext() 将文件名和扩展名分开
        fix = os.path.splitext(fileName)[1]  # os.path.splitext() 获取扩展名

        n = 4
        groups = prefix.split('_')
        prefix = '_'.join(groups[:n])
        newName =  path + "\\" + prefix + fix
        fileName = path + "\\" + fileName

        os.rename(fileName, newName)
        # 文件重新命名


    # 刷新
    sys.stdin.flush()
    print("修改后：" + str(os.listdir(path)))
    # 输出修改后文件夹中包含的文件名称
    # print("修改后：" + str(os.listdir(r"./neteasy_playlist_data3"))[1])

def taowei(path, wz_path, end_time):
    fileList1 = os.listdir(wz_path)
    for file1 in fileList1:
        # 如果后缀名为 .mp4
        if file1.endswith(".mp4"):
            wz_file = wz_path + "\\" + file1

    fileList = os.listdir(path)
    end_time = float(end_time)

    # 遍历所有文件
    for file in fileList:
        # 如果后缀名为 .mp4
        if file.endswith(".mp4"):

            prefix = os.path.splitext(file)[0]  # os.path.splitext() 将文件名和扩展名分开
            fix = os.path.splitext(file)[1]  # os.path.splitext() 获取扩展名

            # 拼接成完整路径
            filePath = path + "\\" + file
            qw_filePath = path + "\\" + prefix + "去尾文件" + fix

            # 获取视频属性
            info = ffmpeg.probe(filePath)  # 获取文件信息
            for c in info['streams']:
                if c['codec_type'] == 'video':  # 匹配视频部分属性
                    vs = c
                    duration = float(vs['duration'])  # 时长

            # 换尾
            vs_time = duration - end_time  # 尾帧开始的时间点

            clip = VideoFileClip(filePath).subclip(0, vs_time)
            # 把生成的视频导出到文件内
            clip.write_videofile(qw_filePath)

            # 合并新尾帧
            video1 = VideoFileClip(qw_filePath)
            video2 = VideoFileClip(wz_file)
            final_clip = concatenate_videoclips([video1, video2])

            new_file = path + "\\" + prefix + "换尾" + fix
            final_clip.to_videofile(new_file, fps=30, remove_temp=False)

        # 去除处理过程产生的mp4文件，在目标目录下
        fileList2 = os.listdir(path)

        for filename2 in fileList2:
            if filename2.endswith(".mp4"):
                if "去尾文件" in filename2:
                    mp_file = path + "\\"+filename2
                    os.remove(mp_file)

        # 去除处理过程产生的mp3文件,在程序目录下
        path1 = os.getcwd()  # 获取当面路径
        fileList = os.listdir(path1)  # 获取当前路径下文件

        for file in fileList:
            if file.endswith(".mp3"):
                os.remove(file)

def main():

    xuqiu = input("请根据需要输出数字 \n1、压缩重名 | 2、压缩 | 3、重命名 | 4、格式转换 | 5、序列帧重命名 | 6、批量换尾：")

    print("***************************************")

   # path = os.getcwd()  # 获取当面路径

    if xuqiu == "1":
        path = input("请输入文件夹地址：")
        banben = input("请输入版本名称：")
        fileList = os.listdir(path)  # 获取当前路径下文件
        qukongge(path,fileList)
        fileList = os.listdir(path)  # 获取当前路径下文件
        compress(path,fileList)
        rename(path,banben)

        path_exe = os.getcwd()  # 获取当面路径
        fileList_log = os.listdir(path_exe)  # 获取当前路径下文件

        for filename in fileList_log:
            if filename.endswith(".log"):
                path1 = path_exe + "\\" + "ffmpeg2pass-0.log"
                path2 = path_exe + "\\" + "ffmpeg2pass-0.log.mbtree"
                os.remove(path1)
                os.remove(path2)

    elif xuqiu == "2":
        path = input("请输入文件夹地址：")
        size = input("请输入所需大小（单位：M，输出数字即可）: ")
        fileList = os.listdir(path)  # 获取当前路径下文件
        qukongge(path,fileList)
        yasuo(path,size)

        path_exe = os.getcwd()  # 获取当面路径
        fileList_log = os.listdir(path_exe)  # 获取当前路径下文件

        for filename in fileList_log:
            if filename.endswith(".log"):
                path1 = path_exe + "\\" + "ffmpeg2pass-0.log"
                path2 = path_exe + "\\" + "ffmpeg2pass-0.log.mbtree"
                os.remove(path1)
                os.remove(path2)

    elif xuqiu == "3":
        path = input("请输入文件夹地址：")
        banben = input("请输入版本名称：")
        rename(path,banben)

    elif xuqiu == "4":
        path = input("请输入文件夹地址：")
        fileList = os.listdir(path)  # 获取当前路径下文件
        qukongge(path, fileList)
        geshi(path)

    elif xuqiu == "5":
        path = input("请输入文件夹地址：")
        xulz(path)


    elif xuqiu == "6":
        path = input("请输入文件夹地址：")
        end_time = input("请输入尾帧开始的时间点：")
        wz_path = input("请输入尾帧地址：")
        taowei(path,wz_path,end_time)

    else:
        print("请选择需求")

    # 结束
    print("————处理完成————")
    print("\n \n \n")


if __name__ == '__main__':
    while 1 :
        main()
