# --** coding="UTF-8" **--

import os
import math
import ffmpeg

class Video_jiagong() :

    def __init__(self,path):

        self.path = path
        self.fileList = os.listdir(path)

#命名去空格
    def qukongge(self,path):

        fileList = os.listdir(path)

        for file in fileList:
            # 判断是否是视频（以.mp4结尾）
            if file.endswith(".mp4"):
                newName = file.replace(" ", '')
                os.rename(os.path.join(path, file), os.path.join(path, newName))

#文件大小的转换
    def size_dx(self,size, dot=2):
        size = float(size)
        # 位 比特 bit
        if 0 <= size < 1:
            human_size = str(round(size / 0.125, dot)) + 'b'
        # 字节 字节 Byte
        elif 1 <= size < 1024:
            human_size = str(round(size, dot)) + 'B'
        # 千字节 千字节 Kilo Byte
        elif math.pow(1024, 1) <= size < math.pow(1024, 2):
            human_size = str(round(size / math.pow(1024, 1), dot))  # + 'KB'
        # 兆字节 兆 Mega Byte
        elif math.pow(1024, 2) <= size < math.pow(1024, 3):
            human_size = str(round(size / math.pow(1024, 2), dot))  # + 'MB'
        # 吉字节 吉 Giga Byte
        elif math.pow(1024, 3) <= size < math.pow(1024, 4):
            human_size = str(round(size / math.pow(1024, 3), dot))  # + 'GB'
        # 太字节 太 Tera Byte
        elif math.pow(1024, 4) <= size < math.pow(1024, 5):
            human_size = str(round(size / math.pow(1024, 4), dot))  # + 'TB'
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

#视频压缩
    def compress(self,path):

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
                filesize = float(filesize1/(1024*1024))

                # 计算新码率
                if filesize > 30.00:
                    new_bit = (30.00 * 8.00 / duration * 1024.00 - au_bit)  # 为了确保压缩后肯定小于30M，所以这里除以1024，而不是除以1000
                    new_bit = str(new_bit) + 'k'
                    print('new_bit30:' + new_bit)

                    newpath_file = '"' + path + "\\" + prefix + "压缩30M" + fix + '"'  # 压缩后的名字和路径

                    # 2pass压缩
                    compress1 = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 1 -an -f mp4 -y NUL".format(
                        path_file, new_bit, )
                    os.system(compress1)

                    compress = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 2 {}".format(
                        path_file, new_bit, newpath_file)
                    os.system(compress)

                if filesize > 80.00:
                    new_bit8 = (80.00 * 8.00 / duration * 1024.00 - au_bit)
                    new_bit8 = str(new_bit8) + 'k'
                    newpath_file8 = '"' + path + "\\" + prefix + "压缩80M" + fix + '"'  # 压缩后的名字和路径

                    compress1 = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 1 -an -f mp4 -y NUL".format(
                        path_file, new_bit8, )
                    os.system(compress1)

                    compress = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 2 {}".format(
                        path_file, new_bit8, newpath_file8)
                    os.system(compress)

        # 删除第一次编码生成的视频解析文件

        fileList2 = os.listdir(path)

        for filename2 in fileList2:
            if filename2.endswith(".log"):
                path1 = path + "\\" + "ffmpeg2pass-0.log"
                path2 = path + "\\" + "ffmpeg2pass-0.log.mbtree"

                os.remove(path1)
                os.remove(path2)

        print("————视频压缩完成————")


#重命名
    def rename(self,path,banben):

        conghu8 = 1
        conghu3 = 1
        conghu9 = 1

        # 对目录下的文件进行遍历
        fileList = os.listdir(path)  # 获取当前路径下文件
        for file in fileList:
            # 判断是否是视频（以.mp4结尾）
            if (file.endswith(".mp4")):
                # 设置新文件名
                prefix = os.path.splitext(file)[0]  # os.path.splitext() 将文件名和扩展名分开
                fix = os.path.splitext(file)[1]  # os.path.splitext() 获取扩展名

                path_file1 = path + "\\" + file    #获取大小用
                Filedx = os.path.getsize(path_file1)  # 获取文件的大小（字节）
                Filedx = float(Filedx / (1024 * 1024))  # 把 字节 换算成 兆

                if (Filedx < 30.00):

                    Name1 = prefix.rpartition('-')  # 获取版号跟命名
                    Name = Name1[0] + "-"+banben+"(30M)"
                    newName = Name + fix

                    if newName == file:  # 如果原文件名是否正确，不替换
                        continue

                    if newName in fileList:
                        newName = Name + "-有重复" + str(conghu3) + fix  # 判断是否会重复命名，会的命名标出
                        conghu3 += 1


                    os.rename(os.path.join(path, file), os.path.join(path,newName))


                elif (30.00 < Filedx < 80.00):

                    Name1 = prefix.rpartition('-')  # 获取版号跟命名
                    Name = Name1[0] + "-" + banben+"(80M)"
                    newName = Name + fix

                    if newName == file:  # 如果原文件名是否正确，不替换
                        continue

                    if newName in fileList:
                        newName = Name + "-有重复" + str(conghu8) + fix  # 判断是否会重复命名，会的命名标出
                        conghu8 += 1

                    os.rename(os.path.join(path, file), os.path.join(path, newName))

                else:

                    Name1 = prefix.rpartition('-')  # 获取版号跟命名
                    Name = Name1[0] + "-超过80M"
                    newName = Name + fix

                    if newName == file:  # 如果原文件名是否正确，不替换
                        continue

                    if newName in fileList:
                        newName = Name + "-有重复" + str(conghu9) + fix
                        conghu9 += 1
                    os.rename(os.path.join(path, file), os.path.join(path, newName))

        print("————视频处理完成————")


    def yasuo(self,path,size):

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

                # 计算新码率
                size = float(size)
                new_bit = (size  * 8.00 / duration * 1024.00 - au_bit)  # 为了确保压缩后肯定小于30M，所以这里除以1024，而不是除以1000
                new_bit = str(new_bit) + 'k'
                print('new_bit30:' + new_bit)

                newpath_file = '"' + path + "\\" + prefix + "-压缩" + fix + '"'  # 压缩后的名字和路径

                # 2pass压缩
                compress1 = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 1 -an -f mp4 -y NUL".format(
                    path_file, new_bit, )
                os.system(compress1)

                compress = "ffmpeg -i {}  -vcodec libx264 -preset slow -profile:v high -b:v {} -pass 2 {}".format(
                    path_file, new_bit, newpath_file)
                os.system(compress)


        # 删除第一次编码生成的视频解析文件

        fileList2 = os.listdir(path)

        for filename2 in fileList2:
            if filename2.endswith(".log"):
                path1 = path + "\\" + "ffmpeg2pass-0.log"
                path2 = path + "\\" + "ffmpeg2pass-0.log.mbtree"

                os.remove(path1)
                os.remove(path2)

        print("————视频压缩完成————")


