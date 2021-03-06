from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 209)
        MainWindow.setWindowOpacity(2.0)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label_url.setFont(font)
        self.label_url.setTextFormat(QtCore.Qt.AutoText)
        self.label_url.setScaledContents(False)
        self.label_url.setObjectName("label_url")
        self.horizontalLayout.addWidget(self.label_url)
        #输入url
        self.edit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_url.setObjectName("edit_url")
        self.horizontalLayout.addWidget(self.edit_url)


        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.horizontalLayout_2.addWidget(self.label_path)

        #输入地址
        self.edit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_path.setObjectName("edit_path")
        self.horizontalLayout_2.addWidget(self.edit_path)

        #下载按钮
        self.btn_down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_down.setObjectName("btn_down")
        self.btn_down.clicked.connect(self.download)

        self.horizontalLayout_2.addWidget(self.btn_down)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(11)
        self.tip.setFont(font)
        self.tip.setWordWrap(True)
        self.tip.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tip.setObjectName("tip")
        self.verticalLayout.addWidget(self.tip)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)

        menu = self.menuBar.addMenu('菜单')
        #关于项目
        self.aboutProject_action = QAction(MainWindow)
        self.aboutProject_action.setCheckable(False)
        self.aboutProject_action.setObjectName('AboutProject')
        self.aboutProject_action.triggered.connect(self.aboutProject)
        self.aboutProject_action.setText('项目原理')
        #关于作者
        self.aboutAuthor_action = QAction(MainWindow)
        self.aboutAuthor_action.setCheckable(False)
        self.aboutAuthor_action.setObjectName('AboutAuthor')
        self.aboutAuthor_action.triggered.connect(self.aboutAuthor)
        self.aboutAuthor_action.setText('关于作者')
        #退出
        self.aboutExec_action = QAction(MainWindow)
        self.aboutExec_action.setCheckable(False)
        self.aboutExec_action.setObjectName('Exec')
        self.aboutExec_action.triggered.connect(self.aboutExec)
        self.aboutExec_action.setText('退出')

        menu.setFont(font)
        menu.addAction(self.aboutProject_action)
        menu.addAction(self.aboutAuthor_action)
        menu.addAction(self.aboutExec_action)

        MainWindow.setMenuBar(self.menuBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "you-get下载助手"))
        self.label_url.setText(_translate("MainWindow", "请输入下载地址:"))
        self.edit_url.setText(_translate("MainWindow","https://www.bilibili.com/video/av91031500?spm_id_from=333.851.b_7265706f7274466972737431.7"))
        self.label_path.setText(_translate("MainWindow", "请输入存放地址:"))
        self.edit_path.setText(_translate("MainWindow","D:\DownloadApp"))
        self.btn_down.setText(_translate("MainWindow", "下载"))
        self.tip.setText(_translate("MainWindow", "注意：支持youtube、twitter、腾讯、爱奇艺、优酷、bilibili等大部分主流网站视频下载、图片下载！"))



