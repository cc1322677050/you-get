import webbrowser
import you_get

from v2.YouGetUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QWidget
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from you_get.extractors import *


class Main(QMainWindow,Ui_MainWindow,QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./image/icon.jpg'))
        self.btn_down.clicked.connect(self.download)
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

    def callbacklog(self, msg):
        print(msg)

    #设置背景
    def resizeEvent(self,QResizeEvent):
        palette = QtGui.QPalette()
        pix = QtGui.QPixmap("./image/background.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        self.setPalette(palette)
    #关于项目
    def aboutProject(self):
        webbrowser.open('https://github.com/soimort/you-get')
    #关于作者
    def aboutAuthor(self):
         QMessageBox.information(None,"关于作者","作者:chengcheng\n"
                                             "QQ:1322677050")
    #退出
    def aboutExec(self):
        sys.exit(app.exec_())
    #下载
    def download(self):
        url=self.edit_url.text()
        path=self.edit_path.text()
        if re.match(r'^https?:/{2}\w.+$', url):
            if path != '':
                try:
                    self.thread = Runthread(path,url)  # 创建线程
                    self.thread._signal.connect(self.callbacklog)  # 连接信号
                    self.thread.start()  # 开始线程
                except BaseException as e:
                    print(e)
                    QMessageBox.critical(None, "错误", "线程无法启动")
            else:
                QMessageBox.critical(None, "错误", "输出地址有误")
        else:
            QMessageBox.critical(None, "错误", "视频地址错误")

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))
    def flush(self):
        pass

# 继承QThread
class Runthread(QtCore.QThread):
    _signal = pyqtSignal(str)
    def __init__(self,path,url):
        super(Runthread, self).__init__()
        self.path = path
        self.url = url
    def __del__(self):
        self.wait()

    def run(self):
        sys.argv = ['you-get', '-o', self.path, self.url,"--debug"]
        you_get.main()
        self._signal.emit("1")


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
