# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def __init__(self):
        self.ms = QMessageBox()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(629, 504)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setAcceptDrops(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 631, 461))
        self.p_info = QWidget()
        self.p_info.setObjectName(u"p_info")
        self.layoutWidget = QWidget(self.p_info)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 30, 351, 31))
        self.search_hor = QHBoxLayout(self.layoutWidget)
        self.search_hor.setObjectName(u"search_hor")
        self.search_hor.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.search_hor.addWidget(self.lineEdit)

        self.search_but = QPushButton(self.p_info)
        self.search_but.setObjectName(u"search_but")
        self.search_but.setGeometry(QRect(10, 30, 93, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(8)
        self.search_but.setFont(font)
        self.search_but.setAutoDefault(False)
        self.search_but.setFlat(False)
        self.layoutWidget_2 = QWidget(self.p_info)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(200, 90, 411, 321))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_w_country = QLabel(self.layoutWidget_2)
        self.lbl_w_country.setObjectName(u"lbl_w_country")
        font1 = QFont()
        font1.setPointSize(9)
        self.lbl_w_country.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_country, 2, 0, 1, 1)

        self.lbl_w_birth = QLabel(self.layoutWidget_2)
        self.lbl_w_birth.setObjectName(u"lbl_w_birth")
        self.lbl_w_birth.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_birth, 1, 0, 1, 1)

        self.lbl_w_name = QLabel(self.layoutWidget_2)
        self.lbl_w_name.setObjectName(u"lbl_w_name")
        self.lbl_w_name.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_name, 0, 0, 1, 1)

        self.lbl_w_money = QLabel(self.layoutWidget_2)
        self.lbl_w_money.setObjectName(u"lbl_w_money")
        self.lbl_w_money.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_money, 6, 0, 1, 1)

        self.lbl_w_role = QLabel(self.layoutWidget_2)
        self.lbl_w_role.setObjectName(u"lbl_w_role")
        self.lbl_w_role.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_role, 5, 0, 1, 1)

        self.lbl_w_team = QLabel(self.layoutWidget_2)
        self.lbl_w_team.setObjectName(u"lbl_w_team")
        self.lbl_w_team.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_team, 4, 0, 1, 1)

        self.lbl_w_hero = QLabel(self.layoutWidget_2)
        self.lbl_w_hero.setObjectName(u"lbl_w_hero")
        self.lbl_w_hero.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_hero, 7, 0, 1, 1)

        self.lbl_w_id = QLabel(self.layoutWidget_2)
        self.lbl_w_id.setObjectName(u"lbl_w_id")
        self.lbl_w_id.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_id, 8, 0, 1, 1)

        self.lbl_w_status = QLabel(self.layoutWidget_2)
        self.lbl_w_status.setObjectName(u"lbl_w_status")
        self.lbl_w_status.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_w_status, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.p_info)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(490, 30, 111, 31))
        self.layoutWidget_3 = QWidget(self.p_info)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 90, 191, 321))
        self.gridLayout = QGridLayout(self.layoutWidget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_name = QLabel(self.layoutWidget_3)
        self.lbl_name.setObjectName(u"lbl_name")
        font2 = QFont()
        font2.setPointSize(10)
        self.lbl_name.setFont(font2)

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)

        self.lbl_birth = QLabel(self.layoutWidget_3)
        self.lbl_birth.setObjectName(u"lbl_birth")
        self.lbl_birth.setFont(font2)

        self.gridLayout.addWidget(self.lbl_birth, 1, 0, 1, 1)

        self.lbl_country = QLabel(self.layoutWidget_3)
        self.lbl_country.setObjectName(u"lbl_country")
        self.lbl_country.setFont(font2)

        self.gridLayout.addWidget(self.lbl_country, 2, 0, 1, 1)

        self.lbl_status = QLabel(self.layoutWidget_3)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setFont(font2)

        self.gridLayout.addWidget(self.lbl_status, 3, 0, 1, 1)

        self.lbl_team = QLabel(self.layoutWidget_3)
        self.lbl_team.setObjectName(u"lbl_team")
        self.lbl_team.setFont(font2)

        self.gridLayout.addWidget(self.lbl_team, 4, 0, 1, 1)

        self.lbl_role = QLabel(self.layoutWidget_3)
        self.lbl_role.setObjectName(u"lbl_role")
        self.lbl_role.setFont(font2)

        self.gridLayout.addWidget(self.lbl_role, 5, 0, 1, 1)

        self.lbl_money = QLabel(self.layoutWidget_3)
        self.lbl_money.setObjectName(u"lbl_money")
        self.lbl_money.setFont(font2)

        self.gridLayout.addWidget(self.lbl_money, 6, 0, 1, 1)

        self.lbl_hero = QLabel(self.layoutWidget_3)
        self.lbl_hero.setObjectName(u"lbl_hero")
        self.lbl_hero.setFont(font2)

        self.gridLayout.addWidget(self.lbl_hero, 7, 0, 1, 1)

        self.lbl_id = QLabel(self.layoutWidget_3)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setFont(font2)

        self.gridLayout.addWidget(self.lbl_id, 8, 0, 1, 1)

        self.tabWidget.addTab(self.p_info, "")
        self.Achiv = QWidget()
        self.Achiv.setObjectName(u"Achiv")
        self.listWidget = QListWidget(self.Achiv)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 0, 601, 431))
        self.tabWidget.addTab(self.Achiv, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 629, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.search_but)
        QWidget.setTabOrder(self.search_but, self.listWidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.search_but.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Finder", None))
        self.search_but.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lbl_w_country.setText("")
        self.lbl_w_birth.setText("")
        self.lbl_w_name.setText("")
        self.lbl_w_money.setText("")
        self.lbl_w_role.setText("")
        self.lbl_w_team.setText("")
        self.lbl_w_hero.setText("")
        self.lbl_w_id.setText("")
        self.lbl_w_status.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dota 2", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"League of Legends", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Rainbow Six", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Counter-Strike", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"VALORANT", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"PUBG", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Overwatch", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Apex Legends", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Rocket League", None))

        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.lbl_birth.setText(QCoreApplication.translate("MainWindow", u"Birth :", None))
        self.lbl_country.setText(QCoreApplication.translate("MainWindow", u"Country :", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.lbl_team.setText(QCoreApplication.translate("MainWindow", u"Team :", None))
        self.lbl_role.setText(QCoreApplication.translate("MainWindow", u"Role(s) :", None))
        self.lbl_money.setText(QCoreApplication.translate("MainWindow", u"Approx. Total Earnings :", None))
        self.lbl_hero.setText(QCoreApplication.translate("MainWindow", u"Signature Hero :", None))
        self.lbl_id.setText(QCoreApplication.translate("MainWindow", u"Alternate IDs :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.p_info), QCoreApplication.translate("MainWindow", u"Personal Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Achiv), QCoreApplication.translate("MainWindow", u"Achievements", None))
    # retranslateUi

