# --** coding="UTF-8" **--

import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import math
import ffmpeg
from PyQt5.QtWidgets import *
import UI
import Class_shenwr
from UI import Ui_MainWindow
from Class_shenwr import Video_jiagong

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setup_ui(self):
        pass

    def ffmpeg_log_remove(self):
        path_exe = os.getcwd()  # 获取当面路径
        fileList_log = os.listdir(path_exe)  # 获取当前路径下文件

        for filename in fileList_log:
            if filename.endswith(".log"):
                path1 = path_exe + "\\" + "ffmpeg2pass-0.log"
                path2 = path_exe + "\\" + "ffmpeg2pass-0.log.mbtree"
                os.remove(path1)
                os.remove(path2)

    def btn_click_ysmm(self):

        path = self.lineEdit_dizhi.text()
        banben = self.lineEdit_banben.text()
        #print(path)

        Video_jiagong.qukongge(self,path)
        Video_jiagong.compress(self,path)
        Video_jiagong.rename(self,path,banben)

        self.ffmpeg_log_remove()

    def btn_click_ys(self):
        path = self.lineEdit_ysdizhi.text()
        size = self.lineEdit_size.text()
        # print(path)

        Video_jiagong.qukongge(self, path)
        Video_jiagong.yasuo(self,path,size)

        self.ffmpeg_log_remove()

    def btn_click_mm(self):
        path = self.lineEdit_mmdizhi.text()
        banben = self.lineEdit_mmbanben.text()
        # print(path)

        Video_jiagong.qukongge(self,path)
        Video_jiagong.rename(self,path,banben)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

