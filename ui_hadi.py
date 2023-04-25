# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hadibjqDpP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1112, 725)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMaximumSize(QSize(80, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.main_logo = QLabel(self.icon_only_widget)
        self.main_logo.setObjectName(u"main_logo")
        self.main_logo.setMinimumSize(QSize(64, 64))
        self.main_logo.setMaximumSize(QSize(64, 64))
        self.main_logo.setPixmap(QPixmap(u":/icons/icons/logo.svg"))

        self.horizontalLayout_3.addWidget(self.main_logo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_small = QPushButton(self.icon_only_widget)
        self.info_small.setObjectName(u"info_small")
        self.info_small.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_small.setIcon(icon)
        self.info_small.setCheckable(True)
        self.info_small.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.info_small)

        self.rpc_small = QPushButton(self.icon_only_widget)
        self.rpc_small.setObjectName(u"rpc_small")
        self.rpc_small.setMaximumSize(QSize(16777215, 30))
        self.rpc_small.setIcon(icon)
        self.rpc_small.setCheckable(True)
        self.rpc_small.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.rpc_small)

        self.rpg_small = QPushButton(self.icon_only_widget)
        self.rpg_small.setObjectName(u"rpg_small")
        self.rpg_small.setMaximumSize(QSize(16777215, 30))
        self.rpg_small.setIcon(icon)
        self.rpg_small.setCheckable(True)
        self.rpg_small.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.rpg_small)

        self.rrg_small = QPushButton(self.icon_only_widget)
        self.rrg_small.setObjectName(u"rrg_small")
        self.rrg_small.setMaximumSize(QSize(16777215, 30))
        self.rrg_small.setIcon(icon)
        self.rrg_small.setCheckable(True)
        self.rrg_small.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.rrg_small)

        self.result_small = QPushButton(self.icon_only_widget)
        self.result_small.setObjectName(u"result_small")
        self.result_small.setMaximumSize(QSize(16777215, 30))
        self.result_small.setIcon(icon)
        self.result_small.setCheckable(True)
        self.result_small.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.result_small)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_small = QPushButton(self.icon_only_widget)
        self.exit_small.setObjectName(u"exit_small")
        self.exit_small.setIcon(icon)

        self.verticalLayout_3.addWidget(self.exit_small)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.side_menu = QWidget(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        self.verticalLayout_4 = QVBoxLayout(self.side_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.side_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/logo.svg"))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.side_menu)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.information = QPushButton(self.side_menu)
        self.information.setObjectName(u"information")
        self.information.setMaximumSize(QSize(16777215, 30))
        self.information.setIcon(icon)
        self.information.setCheckable(True)
        self.information.setAutoRepeat(False)
        self.information.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.information)

        self.rpc = QPushButton(self.side_menu)
        self.rpc.setObjectName(u"rpc")
        self.rpc.setMaximumSize(QSize(16777215, 30))
        self.rpc.setIcon(icon)
        self.rpc.setCheckable(True)
        self.rpc.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.rpc)

        self.rpg = QPushButton(self.side_menu)
        self.rpg.setObjectName(u"rpg")
        self.rpg.setMaximumSize(QSize(16777215, 30))
        self.rpg.setIcon(icon)
        self.rpg.setCheckable(True)
        self.rpg.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.rpg)

        self.rrg = QPushButton(self.side_menu)
        self.rrg.setObjectName(u"rrg")
        self.rrg.setMaximumSize(QSize(16777215, 30))
        self.rrg.setIcon(icon)
        self.rrg.setCheckable(True)
        self.rrg.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.rrg)

        self.results = QPushButton(self.side_menu)
        self.results.setObjectName(u"results")
        self.results.setMaximumSize(QSize(16777215, 30))
        self.results.setIcon(icon)
        self.results.setCheckable(True)
        self.results.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.results)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 301, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit = QPushButton(self.side_menu)
        self.exit.setObjectName(u"exit")
        self.exit.setIcon(icon)

        self.verticalLayout_4.addWidget(self.exit)


        self.gridLayout.addWidget(self.side_menu, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(40, 40))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QHBoxLayout()
        self.top_bar.setSpacing(0)
        self.top_bar.setObjectName(u"top_bar")
        self.menu_toggle = QPushButton(self.widget)
        self.menu_toggle.setObjectName(u"menu_toggle")
        self.menu_toggle.setIcon(icon)
        self.menu_toggle.setCheckable(True)

        self.top_bar.addWidget(self.menu_toggle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_bar.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.top_bar)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.info_page_2 = QWidget()
        self.info_page_2.setObjectName(u"info_page_2")
        self.gridLayout_2 = QGridLayout(self.info_page_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.info_page_in = QWidget(self.info_page_2)
        self.info_page_in.setObjectName(u"info_page_in")
        self.verticalLayout_27 = QVBoxLayout(self.info_page_in)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, -1, 0, 0)
        self.label = QLabel(self.info_page_in)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"Monospace")
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout_27.addWidget(self.label)

        self.scrollArea = QScrollArea(self.info_page_in)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -588, 1200, 1200))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(1200, 1200))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 100))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.widget_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_22.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_22.addWidget(self.lineEdit_2)


        self.verticalLayout_26.addWidget(self.widget_5)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 100))
        self.widget_8.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_23 = QVBoxLayout(self.widget_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_23.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.widget_8)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_23.addWidget(self.lineEdit)


        self.verticalLayout_26.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 100))
        self.widget_9.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_24 = QVBoxLayout(self.widget_9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_24.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.widget_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_24.addWidget(self.lineEdit_3)


        self.verticalLayout_26.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 100))
        self.widget_10.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_21 = QVBoxLayout(self.widget_10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_21.addWidget(self.label_9)

        self.dateEdit = QDateEdit(self.widget_10)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_21.addWidget(self.dateEdit)


        self.verticalLayout_26.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_25 = QVBoxLayout(self.widget_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_25.addWidget(self.label_10)

        self.frame = QFrame(self.widget_11)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_5 = QRadioButton(self.frame)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.frame)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.frame)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout.addWidget(self.radioButton_7)


        self.verticalLayout_25.addWidget(self.frame)


        self.verticalLayout_26.addWidget(self.widget_11)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.label_11)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 100))
        self.widget_12.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_28 = QVBoxLayout(self.widget_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_12 = QLabel(self.widget_12)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_28.addWidget(self.label_12)

        self.frame_2 = QFrame(self.widget_12)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_8 = QRadioButton(self.frame_2)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout_6.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.frame_2)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_6.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.frame_2)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_6.addWidget(self.radioButton_10)


        self.verticalLayout_28.addWidget(self.frame_2)


        self.verticalLayout_26.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_29 = QVBoxLayout(self.widget_13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_13 = QLabel(self.widget_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_29.addWidget(self.label_13)

        self.frame_3 = QFrame(self.widget_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_15 = QRadioButton(self.frame_3)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.horizontalLayout_7.addWidget(self.radioButton_15)

        self.radioButton_14 = QRadioButton(self.frame_3)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.horizontalLayout_7.addWidget(self.radioButton_14)

        self.radioButton_11 = QRadioButton(self.frame_3)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_7.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.frame_3)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_7.addWidget(self.radioButton_12)

        self.radioButton_13 = QRadioButton(self.frame_3)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.horizontalLayout_7.addWidget(self.radioButton_13)


        self.verticalLayout_29.addWidget(self.frame_3)


        self.verticalLayout_26.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_30 = QVBoxLayout(self.widget_14)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_14 = QLabel(self.widget_14)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_30.addWidget(self.label_14)

        self.frame_4 = QFrame(self.widget_14)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_16 = QRadioButton(self.frame_4)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.horizontalLayout_8.addWidget(self.radioButton_16)

        self.radioButton_17 = QRadioButton(self.frame_4)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.horizontalLayout_8.addWidget(self.radioButton_17)

        self.radioButton_18 = QRadioButton(self.frame_4)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.horizontalLayout_8.addWidget(self.radioButton_18)

        self.radioButton_19 = QRadioButton(self.frame_4)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.horizontalLayout_8.addWidget(self.radioButton_19)

        self.radioButton_20 = QRadioButton(self.frame_4)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.horizontalLayout_8.addWidget(self.radioButton_20)


        self.verticalLayout_30.addWidget(self.frame_4)


        self.verticalLayout_26.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_31 = QVBoxLayout(self.widget_15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_15 = QLabel(self.widget_15)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_31.addWidget(self.label_15)

        self.frame_5 = QFrame(self.widget_15)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_21 = QRadioButton(self.frame_5)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.horizontalLayout_9.addWidget(self.radioButton_21)

        self.radioButton_22 = QRadioButton(self.frame_5)
        self.radioButton_22.setObjectName(u"radioButton_22")

        self.horizontalLayout_9.addWidget(self.radioButton_22)

        self.radioButton_23 = QRadioButton(self.frame_5)
        self.radioButton_23.setObjectName(u"radioButton_23")

        self.horizontalLayout_9.addWidget(self.radioButton_23)

        self.radioButton_24 = QRadioButton(self.frame_5)
        self.radioButton_24.setObjectName(u"radioButton_24")

        self.horizontalLayout_9.addWidget(self.radioButton_24)

        self.radioButton_25 = QRadioButton(self.frame_5)
        self.radioButton_25.setObjectName(u"radioButton_25")

        self.horizontalLayout_9.addWidget(self.radioButton_25)


        self.verticalLayout_31.addWidget(self.frame_5)


        self.verticalLayout_26.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_32 = QVBoxLayout(self.widget_16)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_16 = QLabel(self.widget_16)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_32.addWidget(self.label_16)

        self.lineEdit_4 = QLineEdit(self.widget_16)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_32.addWidget(self.lineEdit_4)


        self.verticalLayout_26.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_33 = QVBoxLayout(self.widget_17)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_17 = QLabel(self.widget_17)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_33.addWidget(self.label_17)

        self.lineEdit_5 = QLineEdit(self.widget_17)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_33.addWidget(self.lineEdit_5)


        self.verticalLayout_26.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_34 = QVBoxLayout(self.widget_18)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_18 = QLabel(self.widget_18)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_34.addWidget(self.label_18)

        self.lineEdit_6 = QLineEdit(self.widget_18)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_34.addWidget(self.lineEdit_6)


        self.verticalLayout_26.addWidget(self.widget_18)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_26.addWidget(self.pushButton_13)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_27.addWidget(self.scrollArea)


        self.gridLayout_2.addWidget(self.info_page_in, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.info_page_2)
        self.rpc_page = QWidget()
        self.rpc_page.setObjectName(u"rpc_page")
        self.gridLayout_3 = QGridLayout(self.rpc_page)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.rpc_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(200, 16777215))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.widget_2)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.pushButton_6)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.pushButton_10)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.pushButton_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.rpc_page_in = QWidget(self.rpc_page)
        self.rpc_page_in.setObjectName(u"rpc_page_in")
        self.verticalLayout_6 = QVBoxLayout(self.rpc_page_in)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.rpc_stack = QStackedWidget(self.rpc_page_in)
        self.rpc_stack.setObjectName(u"rpc_stack")
        self.rpc_original = QWidget()
        self.rpc_original.setObjectName(u"rpc_original")
        self.gridLayout_6 = QGridLayout(self.rpc_original)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_2 = QScrollArea(self.rpc_original)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -236, 1200, 1200))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(1200, 1200))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_25.setFont(font1)

        self.verticalLayout_35.addWidget(self.label_25)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_35.addWidget(self.label_19)

        self.widget_19 = QWidget(self.scrollAreaWidgetContents)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_36 = QVBoxLayout(self.widget_19)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_20 = QLabel(self.widget_19)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_36.addWidget(self.label_20)

        self.lineEdit_7 = QLineEdit(self.widget_19)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_36.addWidget(self.lineEdit_7)


        self.verticalLayout_35.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_37 = QVBoxLayout(self.widget_20)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_21 = QLabel(self.widget_20)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_37.addWidget(self.label_21)

        self.lineEdit_8 = QLineEdit(self.widget_20)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_37.addWidget(self.lineEdit_8)


        self.verticalLayout_35.addWidget(self.widget_20)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_35.addWidget(self.label_22)

        self.widget_21 = QWidget(self.scrollAreaWidgetContents)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_38 = QVBoxLayout(self.widget_21)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_23 = QLabel(self.widget_21)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_38.addWidget(self.label_23)

        self.lineEdit_9 = QLineEdit(self.widget_21)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_38.addWidget(self.lineEdit_9)


        self.verticalLayout_35.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.scrollAreaWidgetContents)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_39 = QVBoxLayout(self.widget_22)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_24 = QLabel(self.widget_22)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_39.addWidget(self.label_24)

        self.lineEdit_10 = QLineEdit(self.widget_22)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_39.addWidget(self.lineEdit_10)


        self.verticalLayout_35.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.scrollAreaWidgetContents)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_40 = QVBoxLayout(self.widget_23)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_26 = QLabel(self.widget_23)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_40.addWidget(self.label_26)

        self.frame_6 = QFrame(self.widget_23)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radioButton_26 = QRadioButton(self.frame_6)
        self.radioButton_26.setObjectName(u"radioButton_26")

        self.horizontalLayout_10.addWidget(self.radioButton_26)

        self.radioButton_28 = QRadioButton(self.frame_6)
        self.radioButton_28.setObjectName(u"radioButton_28")

        self.horizontalLayout_10.addWidget(self.radioButton_28)

        self.radioButton_27 = QRadioButton(self.frame_6)
        self.radioButton_27.setObjectName(u"radioButton_27")

        self.horizontalLayout_10.addWidget(self.radioButton_27)

        self.radioButton_29 = QRadioButton(self.frame_6)
        self.radioButton_29.setObjectName(u"radioButton_29")

        self.horizontalLayout_10.addWidget(self.radioButton_29)


        self.verticalLayout_40.addWidget(self.frame_6)


        self.verticalLayout_35.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.scrollAreaWidgetContents)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_41 = QVBoxLayout(self.widget_24)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_27 = QLabel(self.widget_24)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_41.addWidget(self.label_27)

        self.lineEdit_11 = QLineEdit(self.widget_24)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_41.addWidget(self.lineEdit_11)


        self.verticalLayout_35.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.scrollAreaWidgetContents)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_42 = QVBoxLayout(self.widget_25)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_28 = QLabel(self.widget_25)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_42.addWidget(self.label_28)

        self.lineEdit_12 = QLineEdit(self.widget_25)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_42.addWidget(self.lineEdit_12)


        self.verticalLayout_35.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.scrollAreaWidgetContents)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_43 = QVBoxLayout(self.widget_26)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_29 = QLabel(self.widget_26)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_43.addWidget(self.label_29)

        self.lineEdit_13 = QLineEdit(self.widget_26)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_43.addWidget(self.lineEdit_13)


        self.verticalLayout_35.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.scrollAreaWidgetContents)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_44 = QVBoxLayout(self.widget_27)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_30 = QLabel(self.widget_27)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_44.addWidget(self.label_30)

        self.lineEdit_14 = QLineEdit(self.widget_27)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_44.addWidget(self.lineEdit_14)


        self.verticalLayout_35.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.scrollAreaWidgetContents)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_45 = QVBoxLayout(self.widget_28)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_31 = QLabel(self.widget_28)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_45.addWidget(self.label_31)

        self.lineEdit_15 = QLineEdit(self.widget_28)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.verticalLayout_45.addWidget(self.lineEdit_15)


        self.verticalLayout_35.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.scrollAreaWidgetContents)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_46 = QVBoxLayout(self.widget_29)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_32 = QLabel(self.widget_29)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_46.addWidget(self.label_32)

        self.lineEdit_16 = QLineEdit(self.widget_29)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.verticalLayout_46.addWidget(self.lineEdit_16)


        self.verticalLayout_35.addWidget(self.widget_29)

        self.pushButton_19 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_35.addWidget(self.pushButton_19)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_original)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_47 = QVBoxLayout(self.page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.scrollArea_4 = QScrollArea(self.page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 0))
        self.scrollArea_4.setWidgetResizable(False)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -493, 1200, 1200))
        self.scrollAreaWidgetContents_4.setMinimumSize(QSize(1200, 1200))
        self.verticalLayout_54 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_40 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 40))
        self.label_40.setFont(font1)

        self.verticalLayout_54.addWidget(self.label_40)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_54.addWidget(self.label_41)

        self.widget_35 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_35.setObjectName(u"widget_35")
        self.verticalLayout_55 = QVBoxLayout(self.widget_35)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_42 = QLabel(self.widget_35)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_55.addWidget(self.label_42)

        self.lineEdit_22 = QLineEdit(self.widget_35)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.verticalLayout_55.addWidget(self.lineEdit_22)


        self.verticalLayout_54.addWidget(self.widget_35)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_54.addWidget(self.label_46)

        self.widget_36 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_56 = QVBoxLayout(self.widget_36)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_43 = QLabel(self.widget_36)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_56.addWidget(self.label_43)

        self.lineEdit_23 = QLineEdit(self.widget_36)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.verticalLayout_56.addWidget(self.lineEdit_23)


        self.verticalLayout_54.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_57 = QVBoxLayout(self.widget_37)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_44 = QLabel(self.widget_37)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_57.addWidget(self.label_44)

        self.lineEdit_24 = QLineEdit(self.widget_37)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.verticalLayout_57.addWidget(self.lineEdit_24)


        self.verticalLayout_54.addWidget(self.widget_37)

        self.widget_38 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_58 = QVBoxLayout(self.widget_38)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_45 = QLabel(self.widget_38)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_58.addWidget(self.label_45)

        self.lineEdit_25 = QLineEdit(self.widget_38)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.verticalLayout_58.addWidget(self.lineEdit_25)


        self.verticalLayout_54.addWidget(self.widget_38)

        self.label_47 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_54.addWidget(self.label_47)

        self.widget_39 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_59 = QVBoxLayout(self.widget_39)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_48 = QLabel(self.widget_39)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_59.addWidget(self.label_48)

        self.frame_7 = QFrame(self.widget_39)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_30 = QRadioButton(self.frame_7)
        self.radioButton_30.setObjectName(u"radioButton_30")

        self.horizontalLayout_11.addWidget(self.radioButton_30)

        self.radioButton_31 = QRadioButton(self.frame_7)
        self.radioButton_31.setObjectName(u"radioButton_31")

        self.horizontalLayout_11.addWidget(self.radioButton_31)

        self.radioButton_32 = QRadioButton(self.frame_7)
        self.radioButton_32.setObjectName(u"radioButton_32")

        self.horizontalLayout_11.addWidget(self.radioButton_32)

        self.radioButton_33 = QRadioButton(self.frame_7)
        self.radioButton_33.setObjectName(u"radioButton_33")

        self.horizontalLayout_11.addWidget(self.radioButton_33)


        self.verticalLayout_59.addWidget(self.frame_7)


        self.verticalLayout_54.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_60 = QVBoxLayout(self.widget_40)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_49 = QLabel(self.widget_40)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_60.addWidget(self.label_49)

        self.lineEdit_26 = QLineEdit(self.widget_40)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.verticalLayout_60.addWidget(self.lineEdit_26)


        self.verticalLayout_54.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_61 = QVBoxLayout(self.widget_41)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_50 = QLabel(self.widget_41)
        self.label_50.setObjectName(u"label_50")

        self.verticalLayout_61.addWidget(self.label_50)

        self.lineEdit_27 = QLineEdit(self.widget_41)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.verticalLayout_61.addWidget(self.lineEdit_27)


        self.verticalLayout_54.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_62 = QVBoxLayout(self.widget_42)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_51 = QLabel(self.widget_42)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_62.addWidget(self.label_51)

        self.lineEdit_28 = QLineEdit(self.widget_42)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.verticalLayout_62.addWidget(self.lineEdit_28)


        self.verticalLayout_54.addWidget(self.widget_42)

        self.widget_43 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_63 = QVBoxLayout(self.widget_43)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_52 = QLabel(self.widget_43)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_63.addWidget(self.label_52)

        self.lineEdit_29 = QLineEdit(self.widget_43)
        self.lineEdit_29.setObjectName(u"lineEdit_29")

        self.verticalLayout_63.addWidget(self.lineEdit_29)


        self.verticalLayout_54.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_64 = QVBoxLayout(self.widget_44)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_53 = QLabel(self.widget_44)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_64.addWidget(self.label_53)

        self.lineEdit_30 = QLineEdit(self.widget_44)
        self.lineEdit_30.setObjectName(u"lineEdit_30")

        self.verticalLayout_64.addWidget(self.lineEdit_30)


        self.verticalLayout_54.addWidget(self.widget_44)

        self.widget_45 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_65 = QVBoxLayout(self.widget_45)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_54 = QLabel(self.widget_45)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_65.addWidget(self.label_54)

        self.lineEdit_31 = QLineEdit(self.widget_45)
        self.lineEdit_31.setObjectName(u"lineEdit_31")

        self.verticalLayout_65.addWidget(self.lineEdit_31)


        self.verticalLayout_54.addWidget(self.widget_45)

        self.pushButton_20 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_54.addWidget(self.pushButton_20)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_47.addWidget(self.scrollArea_4)

        self.rpc_stack.addWidget(self.page)
        self.rpc_1_1 = QWidget()
        self.rpc_1_1.setObjectName(u"rpc_1_1")
        self.gridLayout_7 = QGridLayout(self.rpc_1_1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea_3 = QScrollArea(self.rpc_1_1)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 600, 600))
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_34 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 30))
        self.label_34.setFont(font1)

        self.verticalLayout_48.addWidget(self.label_34)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_33.setFont(font2)

        self.verticalLayout_48.addWidget(self.label_33)

        self.widget_30 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_49 = QVBoxLayout(self.widget_30)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_35 = QLabel(self.widget_30)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_49.addWidget(self.label_35)

        self.lineEdit_17 = QLineEdit(self.widget_30)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_49.addWidget(self.lineEdit_17)


        self.verticalLayout_48.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_50 = QVBoxLayout(self.widget_31)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_36 = QLabel(self.widget_31)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_50.addWidget(self.label_36)

        self.lineEdit_18 = QLineEdit(self.widget_31)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_50.addWidget(self.lineEdit_18)


        self.verticalLayout_48.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_51 = QVBoxLayout(self.widget_32)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_37 = QLabel(self.widget_32)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_51.addWidget(self.label_37)

        self.lineEdit_19 = QLineEdit(self.widget_32)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_51.addWidget(self.lineEdit_19)


        self.verticalLayout_48.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_33.setObjectName(u"widget_33")
        self.verticalLayout_52 = QVBoxLayout(self.widget_33)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_38 = QLabel(self.widget_33)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_52.addWidget(self.label_38)

        self.lineEdit_20 = QLineEdit(self.widget_33)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_52.addWidget(self.lineEdit_20)


        self.verticalLayout_48.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_53 = QVBoxLayout(self.widget_34)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_39 = QLabel(self.widget_34)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_53.addWidget(self.label_39)

        self.lineEdit_21 = QLineEdit(self.widget_34)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_53.addWidget(self.lineEdit_21)


        self.verticalLayout_48.addWidget(self.widget_34)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_48.addWidget(self.pushButton_14)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_7.addWidget(self.scrollArea_3, 0, 1, 1, 1)

        self.rpc_stack.addWidget(self.rpc_1_1)
        self.rpc_1_2 = QWidget()
        self.rpc_1_2.setObjectName(u"rpc_1_2")
        self.gridLayout_8 = QGridLayout(self.rpc_1_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_5 = QScrollArea(self.rpc_1_2)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -537, 524, 1200))
        self.scrollAreaWidgetContents_5.setMinimumSize(QSize(0, 1200))
        self.verticalLayout_66 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_55 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_66.addWidget(self.label_55)

        self.widget_46 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_46.setObjectName(u"widget_46")
        self.verticalLayout_67 = QVBoxLayout(self.widget_46)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_56 = QLabel(self.widget_46)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_67.addWidget(self.label_56)

        self.frame_9 = QFrame(self.widget_46)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.radioButton_38 = QRadioButton(self.frame_9)
        self.radioButton_38.setObjectName(u"radioButton_38")

        self.horizontalLayout_13.addWidget(self.radioButton_38)

        self.radioButton_39 = QRadioButton(self.frame_9)
        self.radioButton_39.setObjectName(u"radioButton_39")

        self.horizontalLayout_13.addWidget(self.radioButton_39)


        self.verticalLayout_67.addWidget(self.frame_9)


        self.verticalLayout_66.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_68 = QVBoxLayout(self.widget_47)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_57 = QLabel(self.widget_47)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_68.addWidget(self.label_57)

        self.lineEdit_37 = QLineEdit(self.widget_47)
        self.lineEdit_37.setObjectName(u"lineEdit_37")

        self.verticalLayout_68.addWidget(self.lineEdit_37)


        self.verticalLayout_66.addWidget(self.widget_47)

        self.widget_48 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_69 = QVBoxLayout(self.widget_48)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_58 = QLabel(self.widget_48)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_69.addWidget(self.label_58)

        self.lineEdit_36 = QLineEdit(self.widget_48)
        self.lineEdit_36.setObjectName(u"lineEdit_36")

        self.verticalLayout_69.addWidget(self.lineEdit_36)


        self.verticalLayout_66.addWidget(self.widget_48)

        self.label_64 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_66.addWidget(self.label_64)

        self.widget_49 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_70 = QVBoxLayout(self.widget_49)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_59 = QLabel(self.widget_49)
        self.label_59.setObjectName(u"label_59")

        self.verticalLayout_70.addWidget(self.label_59)

        self.lineEdit_35 = QLineEdit(self.widget_49)
        self.lineEdit_35.setObjectName(u"lineEdit_35")

        self.verticalLayout_70.addWidget(self.lineEdit_35)


        self.verticalLayout_66.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_50.setObjectName(u"widget_50")
        self.verticalLayout_71 = QVBoxLayout(self.widget_50)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_60 = QLabel(self.widget_50)
        self.label_60.setObjectName(u"label_60")

        self.verticalLayout_71.addWidget(self.label_60)

        self.lineEdit_34 = QLineEdit(self.widget_50)
        self.lineEdit_34.setObjectName(u"lineEdit_34")

        self.verticalLayout_71.addWidget(self.lineEdit_34)


        self.verticalLayout_66.addWidget(self.widget_50)

        self.label_65 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_66.addWidget(self.label_65)

        self.widget_51 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_51.setObjectName(u"widget_51")
        self.verticalLayout_72 = QVBoxLayout(self.widget_51)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.label_61 = QLabel(self.widget_51)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_72.addWidget(self.label_61)

        self.frame_8 = QFrame(self.widget_51)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_37 = QRadioButton(self.frame_8)
        self.radioButton_37.setObjectName(u"radioButton_37")

        self.horizontalLayout_12.addWidget(self.radioButton_37)

        self.radioButton_36 = QRadioButton(self.frame_8)
        self.radioButton_36.setObjectName(u"radioButton_36")

        self.horizontalLayout_12.addWidget(self.radioButton_36)

        self.radioButton_34 = QRadioButton(self.frame_8)
        self.radioButton_34.setObjectName(u"radioButton_34")

        self.horizontalLayout_12.addWidget(self.radioButton_34)

        self.radioButton_35 = QRadioButton(self.frame_8)
        self.radioButton_35.setObjectName(u"radioButton_35")

        self.horizontalLayout_12.addWidget(self.radioButton_35)


        self.verticalLayout_72.addWidget(self.frame_8)


        self.verticalLayout_66.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_52.setObjectName(u"widget_52")
        self.verticalLayout_73 = QVBoxLayout(self.widget_52)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_62 = QLabel(self.widget_52)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_73.addWidget(self.label_62)

        self.lineEdit_33 = QLineEdit(self.widget_52)
        self.lineEdit_33.setObjectName(u"lineEdit_33")

        self.verticalLayout_73.addWidget(self.lineEdit_33)


        self.verticalLayout_66.addWidget(self.widget_52)

        self.widget_53 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_74 = QVBoxLayout(self.widget_53)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.label_63 = QLabel(self.widget_53)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_74.addWidget(self.label_63)

        self.lineEdit_32 = QLineEdit(self.widget_53)
        self.lineEdit_32.setObjectName(u"lineEdit_32")

        self.verticalLayout_74.addWidget(self.lineEdit_32)


        self.verticalLayout_66.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_54.setObjectName(u"widget_54")
        self.verticalLayout_75 = QVBoxLayout(self.widget_54)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.label_66 = QLabel(self.widget_54)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout_75.addWidget(self.label_66)

        self.lineEdit_38 = QLineEdit(self.widget_54)
        self.lineEdit_38.setObjectName(u"lineEdit_38")

        self.verticalLayout_75.addWidget(self.lineEdit_38)


        self.verticalLayout_66.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_76 = QVBoxLayout(self.widget_55)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_67 = QLabel(self.widget_55)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout_76.addWidget(self.label_67)

        self.lineEdit_39 = QLineEdit(self.widget_55)
        self.lineEdit_39.setObjectName(u"lineEdit_39")

        self.verticalLayout_76.addWidget(self.lineEdit_39)


        self.verticalLayout_66.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_56.setObjectName(u"widget_56")
        self.verticalLayout_77 = QVBoxLayout(self.widget_56)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_68 = QLabel(self.widget_56)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_77.addWidget(self.label_68)

        self.lineEdit_40 = QLineEdit(self.widget_56)
        self.lineEdit_40.setObjectName(u"lineEdit_40")

        self.verticalLayout_77.addWidget(self.lineEdit_40)


        self.verticalLayout_66.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_57.setObjectName(u"widget_57")
        self.verticalLayout_78 = QVBoxLayout(self.widget_57)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.label_69 = QLabel(self.widget_57)
        self.label_69.setObjectName(u"label_69")

        self.verticalLayout_78.addWidget(self.label_69)

        self.lineEdit_41 = QLineEdit(self.widget_57)
        self.lineEdit_41.setObjectName(u"lineEdit_41")

        self.verticalLayout_78.addWidget(self.lineEdit_41)


        self.verticalLayout_66.addWidget(self.widget_57)

        self.pushButton_23 = QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout_66.addWidget(self.pushButton_23)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_8.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_1_2)
        self.rpc_2 = QWidget()
        self.rpc_2.setObjectName(u"rpc_2")
        self.gridLayout_9 = QGridLayout(self.rpc_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea_6 = QScrollArea(self.rpc_2)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, -537, 524, 1200))
        self.scrollAreaWidgetContents_6.setMinimumSize(QSize(0, 1200))
        self.verticalLayout_79 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_70 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_79.addWidget(self.label_70)

        self.widget_58 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_58.setObjectName(u"widget_58")
        self.verticalLayout_80 = QVBoxLayout(self.widget_58)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.label_71 = QLabel(self.widget_58)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_80.addWidget(self.label_71)

        self.lineEdit_46 = QLineEdit(self.widget_58)
        self.lineEdit_46.setObjectName(u"lineEdit_46")

        self.verticalLayout_80.addWidget(self.lineEdit_46)


        self.verticalLayout_79.addWidget(self.widget_58)

        self.label_77 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_77.setObjectName(u"label_77")

        self.verticalLayout_79.addWidget(self.label_77)

        self.widget_59 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_59.setObjectName(u"widget_59")
        self.verticalLayout_81 = QVBoxLayout(self.widget_59)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.label_72 = QLabel(self.widget_59)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_81.addWidget(self.label_72)

        self.lineEdit_45 = QLineEdit(self.widget_59)
        self.lineEdit_45.setObjectName(u"lineEdit_45")

        self.verticalLayout_81.addWidget(self.lineEdit_45)


        self.verticalLayout_79.addWidget(self.widget_59)

        self.widget_60 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_60.setObjectName(u"widget_60")
        self.verticalLayout_82 = QVBoxLayout(self.widget_60)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.label_73 = QLabel(self.widget_60)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_82.addWidget(self.label_73)

        self.lineEdit_44 = QLineEdit(self.widget_60)
        self.lineEdit_44.setObjectName(u"lineEdit_44")

        self.verticalLayout_82.addWidget(self.lineEdit_44)


        self.verticalLayout_79.addWidget(self.widget_60)

        self.label_78 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_78.setObjectName(u"label_78")

        self.verticalLayout_79.addWidget(self.label_78)

        self.widget_61 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_85 = QVBoxLayout(self.widget_61)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.label_76 = QLabel(self.widget_61)
        self.label_76.setObjectName(u"label_76")

        self.verticalLayout_85.addWidget(self.label_76)

        self.frame_10 = QFrame(self.widget_61)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radioButton_40 = QRadioButton(self.frame_10)
        self.radioButton_40.setObjectName(u"radioButton_40")

        self.horizontalLayout_14.addWidget(self.radioButton_40)

        self.radioButton_41 = QRadioButton(self.frame_10)
        self.radioButton_41.setObjectName(u"radioButton_41")

        self.horizontalLayout_14.addWidget(self.radioButton_41)

        self.radioButton_42 = QRadioButton(self.frame_10)
        self.radioButton_42.setObjectName(u"radioButton_42")

        self.horizontalLayout_14.addWidget(self.radioButton_42)

        self.radioButton_43 = QRadioButton(self.frame_10)
        self.radioButton_43.setObjectName(u"radioButton_43")

        self.horizontalLayout_14.addWidget(self.radioButton_43)


        self.verticalLayout_85.addWidget(self.frame_10)


        self.verticalLayout_79.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_62.setObjectName(u"widget_62")
        self.verticalLayout_83 = QVBoxLayout(self.widget_62)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_74 = QLabel(self.widget_62)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_83.addWidget(self.label_74)

        self.lineEdit_43 = QLineEdit(self.widget_62)
        self.lineEdit_43.setObjectName(u"lineEdit_43")

        self.verticalLayout_83.addWidget(self.lineEdit_43)


        self.verticalLayout_79.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_63.setObjectName(u"widget_63")
        self.verticalLayout_84 = QVBoxLayout(self.widget_63)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.label_75 = QLabel(self.widget_63)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_84.addWidget(self.label_75)

        self.lineEdit_42 = QLineEdit(self.widget_63)
        self.lineEdit_42.setObjectName(u"lineEdit_42")

        self.verticalLayout_84.addWidget(self.lineEdit_42)


        self.verticalLayout_79.addWidget(self.widget_63)

        self.widget_64 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_64.setObjectName(u"widget_64")
        self.verticalLayout_86 = QVBoxLayout(self.widget_64)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.label_79 = QLabel(self.widget_64)
        self.label_79.setObjectName(u"label_79")

        self.verticalLayout_86.addWidget(self.label_79)

        self.label_80 = QLabel(self.widget_64)
        self.label_80.setObjectName(u"label_80")

        self.verticalLayout_86.addWidget(self.label_80)

        self.lineEdit_47 = QLineEdit(self.widget_64)
        self.lineEdit_47.setObjectName(u"lineEdit_47")

        self.verticalLayout_86.addWidget(self.lineEdit_47)

        self.label_81 = QLabel(self.widget_64)
        self.label_81.setObjectName(u"label_81")

        self.verticalLayout_86.addWidget(self.label_81)

        self.lineEdit_48 = QLineEdit(self.widget_64)
        self.lineEdit_48.setObjectName(u"lineEdit_48")

        self.verticalLayout_86.addWidget(self.lineEdit_48)


        self.verticalLayout_79.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_65.setObjectName(u"widget_65")
        self.verticalLayout_87 = QVBoxLayout(self.widget_65)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.label_82 = QLabel(self.widget_65)
        self.label_82.setObjectName(u"label_82")

        self.verticalLayout_87.addWidget(self.label_82)

        self.label_84 = QLabel(self.widget_65)
        self.label_84.setObjectName(u"label_84")

        self.verticalLayout_87.addWidget(self.label_84)

        self.lineEdit_49 = QLineEdit(self.widget_65)
        self.lineEdit_49.setObjectName(u"lineEdit_49")

        self.verticalLayout_87.addWidget(self.lineEdit_49)

        self.label_83 = QLabel(self.widget_65)
        self.label_83.setObjectName(u"label_83")

        self.verticalLayout_87.addWidget(self.label_83)

        self.lineEdit_50 = QLineEdit(self.widget_65)
        self.lineEdit_50.setObjectName(u"lineEdit_50")

        self.verticalLayout_87.addWidget(self.lineEdit_50)


        self.verticalLayout_79.addWidget(self.widget_65)

        self.widget_66 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_66.setObjectName(u"widget_66")
        self.verticalLayout_88 = QVBoxLayout(self.widget_66)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_85 = QLabel(self.widget_66)
        self.label_85.setObjectName(u"label_85")

        self.verticalLayout_88.addWidget(self.label_85)

        self.label_87 = QLabel(self.widget_66)
        self.label_87.setObjectName(u"label_87")

        self.verticalLayout_88.addWidget(self.label_87)

        self.lineEdit_51 = QLineEdit(self.widget_66)
        self.lineEdit_51.setObjectName(u"lineEdit_51")

        self.verticalLayout_88.addWidget(self.lineEdit_51)

        self.label_86 = QLabel(self.widget_66)
        self.label_86.setObjectName(u"label_86")

        self.verticalLayout_88.addWidget(self.label_86)

        self.lineEdit_52 = QLineEdit(self.widget_66)
        self.lineEdit_52.setObjectName(u"lineEdit_52")

        self.verticalLayout_88.addWidget(self.lineEdit_52)


        self.verticalLayout_79.addWidget(self.widget_66)

        self.widget_67 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_67.setObjectName(u"widget_67")
        self.verticalLayout_89 = QVBoxLayout(self.widget_67)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.label_88 = QLabel(self.widget_67)
        self.label_88.setObjectName(u"label_88")

        self.verticalLayout_89.addWidget(self.label_88)

        self.label_90 = QLabel(self.widget_67)
        self.label_90.setObjectName(u"label_90")

        self.verticalLayout_89.addWidget(self.label_90)

        self.lineEdit_53 = QLineEdit(self.widget_67)
        self.lineEdit_53.setObjectName(u"lineEdit_53")

        self.verticalLayout_89.addWidget(self.lineEdit_53)

        self.label_89 = QLabel(self.widget_67)
        self.label_89.setObjectName(u"label_89")

        self.verticalLayout_89.addWidget(self.label_89)

        self.lineEdit_54 = QLineEdit(self.widget_67)
        self.lineEdit_54.setObjectName(u"lineEdit_54")

        self.verticalLayout_89.addWidget(self.lineEdit_54)


        self.verticalLayout_79.addWidget(self.widget_67)

        self.pushButton_26 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.verticalLayout_79.addWidget(self.pushButton_26)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_9.addWidget(self.scrollArea_6, 0, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_2)
        self.rpc_3 = QWidget()
        self.rpc_3.setObjectName(u"rpc_3")
        self.gridLayout_10 = QGridLayout(self.rpc_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.checkBox_2 = QCheckBox(self.rpc_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_10.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.rpc_3)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout_10.addWidget(self.pushButton_29, 1, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.rpc_3)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_10.addWidget(self.pushButton_30, 2, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_3)
        self.rpc_4_1 = QWidget()
        self.rpc_4_1.setObjectName(u"rpc_4_1")
        self.gridLayout_11 = QGridLayout(self.rpc_4_1)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.buttonBox = QDialogButtonBox(self.rpc_4_1)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_11.addWidget(self.buttonBox, 0, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_4_1)
        self.rpc_4_2 = QWidget()
        self.rpc_4_2.setObjectName(u"rpc_4_2")
        self.gridLayout_12 = QGridLayout(self.rpc_4_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_31 = QPushButton(self.rpc_4_2)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.gridLayout_12.addWidget(self.pushButton_31, 0, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_4_2)
        self.rpc_4_3 = QWidget()
        self.rpc_4_3.setObjectName(u"rpc_4_3")
        self.horizontalLayout_2 = QHBoxLayout(self.rpc_4_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_33 = QPushButton(self.rpc_4_3)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.horizontalLayout_2.addWidget(self.pushButton_33)

        self.pushButton_32 = QPushButton(self.rpc_4_3)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.horizontalLayout_2.addWidget(self.pushButton_32)

        self.rpc_stack.addWidget(self.rpc_4_3)
        self.rpc_4_4 = QWidget()
        self.rpc_4_4.setObjectName(u"rpc_4_4")
        self.gridLayout_13 = QGridLayout(self.rpc_4_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.toolButton_2 = QToolButton(self.rpc_4_4)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout_13.addWidget(self.toolButton_2, 0, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.rpc_4_4)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.gridLayout_13.addWidget(self.pushButton_34, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.rpc_4_4)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_13.addWidget(self.radioButton, 1, 1, 1, 1)

        self.rpc_stack.addWidget(self.rpc_4_4)
        self.rpc_4_5 = QWidget()
        self.rpc_4_5.setObjectName(u"rpc_4_5")
        self.gridLayout_14 = QGridLayout(self.rpc_4_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.toolButton_3 = QToolButton(self.rpc_4_5)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.gridLayout_14.addWidget(self.toolButton_3, 0, 0, 1, 1)

        self.pushButton_35 = QPushButton(self.rpc_4_5)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.gridLayout_14.addWidget(self.pushButton_35, 1, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.rpc_4_5)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout_14.addWidget(self.commandLinkButton, 2, 0, 1, 1)

        self.rpc_stack.addWidget(self.rpc_4_5)

        self.verticalLayout_6.addWidget(self.rpc_stack)


        self.gridLayout_3.addWidget(self.rpc_page_in, 0, 2, 1, 1)

        self.rpc_menu_1_1 = QWidget(self.rpc_page)
        self.rpc_menu_1_1.setObjectName(u"rpc_menu_1_1")
        self.rpc_menu_1_1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.rpc_menu_1_1)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.rpc_sub_menu1 = QWidget(self.rpc_menu_1_1)
        self.rpc_sub_menu1.setObjectName(u"rpc_sub_menu1")
        self.rpc_sub_menu1.setMinimumSize(QSize(0, 72))
        self.verticalLayout_12 = QVBoxLayout(self.rpc_sub_menu1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_11 = QPushButton(self.rpc_sub_menu1)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.rpc_sub_menu1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.pushButton_12)


        self.verticalLayout_14.addWidget(self.rpc_sub_menu1)

        self.rpc_sub_mnu_2 = QWidget(self.rpc_menu_1_1)
        self.rpc_sub_mnu_2.setObjectName(u"rpc_sub_mnu_2")
        self.rpc_sub_mnu_2.setMinimumSize(QSize(0, 180))
        self.verticalLayout_15 = QVBoxLayout(self.rpc_sub_mnu_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.pushButton_4 = QPushButton(self.rpc_sub_mnu_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_15.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.rpc_sub_mnu_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_15.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.rpc_sub_mnu_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_15.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.rpc_sub_mnu_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_15.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.rpc_sub_mnu_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_15.addWidget(self.pushButton_3)


        self.verticalLayout_14.addWidget(self.rpc_sub_mnu_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addWidget(self.rpc_menu_1_1, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.rpc_page)
        self.rpg_page = QWidget()
        self.rpg_page.setObjectName(u"rpg_page")
        self.verticalLayout_8 = QVBoxLayout(self.rpg_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.rpg_page_2 = QWidget(self.rpg_page)
        self.rpg_page_2.setObjectName(u"rpg_page_2")
        self.gridLayout_4 = QGridLayout(self.rpg_page_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.rpg_page_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 6, 0, 0)
        self.pushButton_17 = QPushButton(self.widget_4)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.pushButton_17)

        self.pushButton_15 = QPushButton(self.widget_4)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.pushButton_16)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)


        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)

        self.rpg_side_menu = QWidget(self.rpg_page_2)
        self.rpg_side_menu.setObjectName(u"rpg_side_menu")
        self.rpg_side_menu.setMaximumSize(QSize(205, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.rpg_side_menu)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.rpg_side_menu)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_18 = QPushButton(self.widget_6)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.pushButton_18)


        self.verticalLayout_16.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.rpg_side_menu)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_17 = QVBoxLayout(self.widget_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_21 = QPushButton(self.widget_7)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_7)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.pushButton_22)

        self.pushButton_24 = QPushButton(self.widget_7)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.widget_7)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.pushButton_25)


        self.verticalLayout_16.addWidget(self.widget_7)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)


        self.gridLayout_4.addWidget(self.rpg_side_menu, 0, 1, 1, 1)

        self.rpg_stack = QStackedWidget(self.rpg_page_2)
        self.rpg_stack.setObjectName(u"rpg_stack")
        self.rpg_page_1 = QWidget()
        self.rpg_page_1.setObjectName(u"rpg_page_1")
        self.gridLayout_15 = QGridLayout(self.rpg_page_1)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.scrollArea_7 = QScrollArea(self.rpg_page_1)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, -556, 554, 1200))
        self.scrollAreaWidgetContents_7.setMinimumSize(QSize(0, 1200))
        self.verticalLayout_90 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.label_91 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_91.setObjectName(u"label_91")

        self.verticalLayout_90.addWidget(self.label_91)

        self.widget_68 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_68.setObjectName(u"widget_68")
        self.verticalLayout_96 = QVBoxLayout(self.widget_68)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.label_94 = QLabel(self.widget_68)
        self.label_94.setObjectName(u"label_94")

        self.verticalLayout_96.addWidget(self.label_94)

        self.lineEdit_55 = QLineEdit(self.widget_68)
        self.lineEdit_55.setObjectName(u"lineEdit_55")

        self.verticalLayout_96.addWidget(self.lineEdit_55)


        self.verticalLayout_90.addWidget(self.widget_68)

        self.widget_69 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_97 = QVBoxLayout(self.widget_69)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_95 = QLabel(self.widget_69)
        self.label_95.setObjectName(u"label_95")

        self.verticalLayout_97.addWidget(self.label_95)

        self.lineEdit_56 = QLineEdit(self.widget_69)
        self.lineEdit_56.setObjectName(u"lineEdit_56")

        self.verticalLayout_97.addWidget(self.lineEdit_56)


        self.verticalLayout_90.addWidget(self.widget_69)

        self.label_92 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_92.setObjectName(u"label_92")

        self.verticalLayout_90.addWidget(self.label_92)

        self.widget_70 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_70.setObjectName(u"widget_70")
        self.verticalLayout_95 = QVBoxLayout(self.widget_70)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.label_96 = QLabel(self.widget_70)
        self.label_96.setObjectName(u"label_96")

        self.verticalLayout_95.addWidget(self.label_96)

        self.lineEdit_57 = QLineEdit(self.widget_70)
        self.lineEdit_57.setObjectName(u"lineEdit_57")

        self.verticalLayout_95.addWidget(self.lineEdit_57)


        self.verticalLayout_90.addWidget(self.widget_70)

        self.widget_71 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_71.setObjectName(u"widget_71")
        self.verticalLayout_94 = QVBoxLayout(self.widget_71)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.label_97 = QLabel(self.widget_71)
        self.label_97.setObjectName(u"label_97")

        self.verticalLayout_94.addWidget(self.label_97)

        self.lineEdit_58 = QLineEdit(self.widget_71)
        self.lineEdit_58.setObjectName(u"lineEdit_58")

        self.verticalLayout_94.addWidget(self.lineEdit_58)


        self.verticalLayout_90.addWidget(self.widget_71)

        self.label_93 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_93.setObjectName(u"label_93")

        self.verticalLayout_90.addWidget(self.label_93)

        self.widget_72 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_72.setObjectName(u"widget_72")
        self.verticalLayout_93 = QVBoxLayout(self.widget_72)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.label_98 = QLabel(self.widget_72)
        self.label_98.setObjectName(u"label_98")

        self.verticalLayout_93.addWidget(self.label_98)

        self.frame_11 = QFrame(self.widget_72)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.radioButton_44 = QRadioButton(self.frame_11)
        self.radioButton_44.setObjectName(u"radioButton_44")

        self.horizontalLayout_15.addWidget(self.radioButton_44)

        self.radioButton_45 = QRadioButton(self.frame_11)
        self.radioButton_45.setObjectName(u"radioButton_45")

        self.horizontalLayout_15.addWidget(self.radioButton_45)

        self.radioButton_46 = QRadioButton(self.frame_11)
        self.radioButton_46.setObjectName(u"radioButton_46")

        self.horizontalLayout_15.addWidget(self.radioButton_46)

        self.radioButton_47 = QRadioButton(self.frame_11)
        self.radioButton_47.setObjectName(u"radioButton_47")

        self.horizontalLayout_15.addWidget(self.radioButton_47)


        self.verticalLayout_93.addWidget(self.frame_11)


        self.verticalLayout_90.addWidget(self.widget_72)

        self.widget_73 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_73.setObjectName(u"widget_73")
        self.verticalLayout_92 = QVBoxLayout(self.widget_73)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.label_99 = QLabel(self.widget_73)
        self.label_99.setObjectName(u"label_99")

        self.verticalLayout_92.addWidget(self.label_99)

        self.lineEdit_60 = QLineEdit(self.widget_73)
        self.lineEdit_60.setObjectName(u"lineEdit_60")

        self.verticalLayout_92.addWidget(self.lineEdit_60)


        self.verticalLayout_90.addWidget(self.widget_73)

        self.widget_74 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_74.setObjectName(u"widget_74")
        self.verticalLayout_91 = QVBoxLayout(self.widget_74)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_100 = QLabel(self.widget_74)
        self.label_100.setObjectName(u"label_100")

        self.verticalLayout_91.addWidget(self.label_100)

        self.lineEdit_61 = QLineEdit(self.widget_74)
        self.lineEdit_61.setObjectName(u"lineEdit_61")

        self.verticalLayout_91.addWidget(self.lineEdit_61)


        self.verticalLayout_90.addWidget(self.widget_74)

        self.widget_75 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_75.setObjectName(u"widget_75")
        self.verticalLayout_98 = QVBoxLayout(self.widget_75)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.label_101 = QLabel(self.widget_75)
        self.label_101.setObjectName(u"label_101")

        self.verticalLayout_98.addWidget(self.label_101)

        self.lineEdit_59 = QLineEdit(self.widget_75)
        self.lineEdit_59.setObjectName(u"lineEdit_59")

        self.verticalLayout_98.addWidget(self.lineEdit_59)


        self.verticalLayout_90.addWidget(self.widget_75)

        self.widget_76 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_76.setObjectName(u"widget_76")
        self.verticalLayout_99 = QVBoxLayout(self.widget_76)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.label_102 = QLabel(self.widget_76)
        self.label_102.setObjectName(u"label_102")

        self.verticalLayout_99.addWidget(self.label_102)

        self.lineEdit_62 = QLineEdit(self.widget_76)
        self.lineEdit_62.setObjectName(u"lineEdit_62")

        self.verticalLayout_99.addWidget(self.lineEdit_62)


        self.verticalLayout_90.addWidget(self.widget_76)

        self.widget_77 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_77.setObjectName(u"widget_77")
        self.verticalLayout_100 = QVBoxLayout(self.widget_77)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.label_103 = QLabel(self.widget_77)
        self.label_103.setObjectName(u"label_103")

        self.verticalLayout_100.addWidget(self.label_103)

        self.lineEdit_63 = QLineEdit(self.widget_77)
        self.lineEdit_63.setObjectName(u"lineEdit_63")

        self.verticalLayout_100.addWidget(self.lineEdit_63)


        self.verticalLayout_90.addWidget(self.widget_77)

        self.widget_78 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_78.setObjectName(u"widget_78")
        self.verticalLayout_101 = QVBoxLayout(self.widget_78)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.label_104 = QLabel(self.widget_78)
        self.label_104.setObjectName(u"label_104")

        self.verticalLayout_101.addWidget(self.label_104)

        self.lineEdit_64 = QLineEdit(self.widget_78)
        self.lineEdit_64.setObjectName(u"lineEdit_64")

        self.verticalLayout_101.addWidget(self.lineEdit_64)


        self.verticalLayout_90.addWidget(self.widget_78)

        self.pushButton_27 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_90.addWidget(self.pushButton_27)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_15.addWidget(self.scrollArea_7, 0, 0, 1, 1)

        self.rpg_stack.addWidget(self.rpg_page_1)
        self.rpg_2 = QWidget()
        self.rpg_2.setObjectName(u"rpg_2")
        self.verticalLayout_19 = QVBoxLayout(self.rpg_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea_8 = QScrollArea(self.rpg_2)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, -531, 554, 1200))
        self.scrollAreaWidgetContents_8.setMinimumSize(QSize(0, 1200))
        self.verticalLayout_107 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.label_105 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_105.setObjectName(u"label_105")

        self.verticalLayout_107.addWidget(self.label_105)

        self.widget_80 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_80.setObjectName(u"widget_80")
        self.verticalLayout_102 = QVBoxLayout(self.widget_80)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.label_107 = QLabel(self.widget_80)
        self.label_107.setObjectName(u"label_107")

        self.verticalLayout_102.addWidget(self.label_107)

        self.lineEdit_65 = QLineEdit(self.widget_80)
        self.lineEdit_65.setObjectName(u"lineEdit_65")

        self.verticalLayout_102.addWidget(self.lineEdit_65)


        self.verticalLayout_107.addWidget(self.widget_80)

        self.label_108 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_108.setObjectName(u"label_108")

        self.verticalLayout_107.addWidget(self.label_108)

        self.widget_81 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_81.setObjectName(u"widget_81")
        self.verticalLayout_104 = QVBoxLayout(self.widget_81)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.label_109 = QLabel(self.widget_81)
        self.label_109.setObjectName(u"label_109")

        self.verticalLayout_104.addWidget(self.label_109)

        self.lineEdit_67 = QLineEdit(self.widget_81)
        self.lineEdit_67.setObjectName(u"lineEdit_67")

        self.verticalLayout_104.addWidget(self.lineEdit_67)


        self.verticalLayout_107.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_82.setObjectName(u"widget_82")
        self.verticalLayout_105 = QVBoxLayout(self.widget_82)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.label_110 = QLabel(self.widget_82)
        self.label_110.setObjectName(u"label_110")

        self.verticalLayout_105.addWidget(self.label_110)

        self.lineEdit_68 = QLineEdit(self.widget_82)
        self.lineEdit_68.setObjectName(u"lineEdit_68")

        self.verticalLayout_105.addWidget(self.lineEdit_68)


        self.verticalLayout_107.addWidget(self.widget_82)

        self.widget_79 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_79.setObjectName(u"widget_79")

        self.verticalLayout_107.addWidget(self.widget_79)

        self.label_111 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_111.setObjectName(u"label_111")

        self.verticalLayout_107.addWidget(self.label_111)

        self.widget_83 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_83.setObjectName(u"widget_83")
        self.verticalLayout_106 = QVBoxLayout(self.widget_83)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.label_112 = QLabel(self.widget_83)
        self.label_112.setObjectName(u"label_112")

        self.verticalLayout_106.addWidget(self.label_112)

        self.frame_12 = QFrame(self.widget_83)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.radioButton_48 = QRadioButton(self.frame_12)
        self.radioButton_48.setObjectName(u"radioButton_48")

        self.horizontalLayout_17.addWidget(self.radioButton_48)

        self.radioButton_49 = QRadioButton(self.frame_12)
        self.radioButton_49.setObjectName(u"radioButton_49")

        self.horizontalLayout_17.addWidget(self.radioButton_49)

        self.radioButton_50 = QRadioButton(self.frame_12)
        self.radioButton_50.setObjectName(u"radioButton_50")

        self.horizontalLayout_17.addWidget(self.radioButton_50)

        self.radioButton_51 = QRadioButton(self.frame_12)
        self.radioButton_51.setObjectName(u"radioButton_51")

        self.horizontalLayout_17.addWidget(self.radioButton_51)


        self.verticalLayout_106.addWidget(self.frame_12)


        self.verticalLayout_107.addWidget(self.widget_83)

        self.widget_84 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_84.setObjectName(u"widget_84")
        self.verticalLayout_108 = QVBoxLayout(self.widget_84)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.label_113 = QLabel(self.widget_84)
        self.label_113.setObjectName(u"label_113")

        self.verticalLayout_108.addWidget(self.label_113)

        self.lineEdit_69 = QLineEdit(self.widget_84)
        self.lineEdit_69.setObjectName(u"lineEdit_69")

        self.verticalLayout_108.addWidget(self.lineEdit_69)


        self.verticalLayout_107.addWidget(self.widget_84)

        self.widget_85 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_85.setObjectName(u"widget_85")
        self.verticalLayout_109 = QVBoxLayout(self.widget_85)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.label_114 = QLabel(self.widget_85)
        self.label_114.setObjectName(u"label_114")

        self.verticalLayout_109.addWidget(self.label_114)

        self.lineEdit_70 = QLineEdit(self.widget_85)
        self.lineEdit_70.setObjectName(u"lineEdit_70")

        self.verticalLayout_109.addWidget(self.lineEdit_70)


        self.verticalLayout_107.addWidget(self.widget_85)

        self.widget_86 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_86.setObjectName(u"widget_86")
        self.verticalLayout_103 = QVBoxLayout(self.widget_86)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.label_106 = QLabel(self.widget_86)
        self.label_106.setObjectName(u"label_106")

        self.verticalLayout_103.addWidget(self.label_106)

        self.label_115 = QLabel(self.widget_86)
        self.label_115.setObjectName(u"label_115")

        self.verticalLayout_103.addWidget(self.label_115)

        self.lineEdit_66 = QLineEdit(self.widget_86)
        self.lineEdit_66.setObjectName(u"lineEdit_66")

        self.verticalLayout_103.addWidget(self.lineEdit_66)

        self.label_116 = QLabel(self.widget_86)
        self.label_116.setObjectName(u"label_116")

        self.verticalLayout_103.addWidget(self.label_116)

        self.lineEdit_71 = QLineEdit(self.widget_86)
        self.lineEdit_71.setObjectName(u"lineEdit_71")

        self.verticalLayout_103.addWidget(self.lineEdit_71)


        self.verticalLayout_107.addWidget(self.widget_86)

        self.widget_87 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_87.setObjectName(u"widget_87")
        self.verticalLayout_110 = QVBoxLayout(self.widget_87)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.label_117 = QLabel(self.widget_87)
        self.label_117.setObjectName(u"label_117")

        self.verticalLayout_110.addWidget(self.label_117)

        self.label_119 = QLabel(self.widget_87)
        self.label_119.setObjectName(u"label_119")

        self.verticalLayout_110.addWidget(self.label_119)

        self.lineEdit_72 = QLineEdit(self.widget_87)
        self.lineEdit_72.setObjectName(u"lineEdit_72")

        self.verticalLayout_110.addWidget(self.lineEdit_72)

        self.label_118 = QLabel(self.widget_87)
        self.label_118.setObjectName(u"label_118")

        self.verticalLayout_110.addWidget(self.label_118)

        self.lineEdit_73 = QLineEdit(self.widget_87)
        self.lineEdit_73.setObjectName(u"lineEdit_73")

        self.verticalLayout_110.addWidget(self.lineEdit_73)


        self.verticalLayout_107.addWidget(self.widget_87)

        self.widget_88 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_88.setObjectName(u"widget_88")
        self.verticalLayout_111 = QVBoxLayout(self.widget_88)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.label_122 = QLabel(self.widget_88)
        self.label_122.setObjectName(u"label_122")

        self.verticalLayout_111.addWidget(self.label_122)

        self.label_120 = QLabel(self.widget_88)
        self.label_120.setObjectName(u"label_120")

        self.verticalLayout_111.addWidget(self.label_120)

        self.lineEdit_74 = QLineEdit(self.widget_88)
        self.lineEdit_74.setObjectName(u"lineEdit_74")

        self.verticalLayout_111.addWidget(self.lineEdit_74)

        self.label_121 = QLabel(self.widget_88)
        self.label_121.setObjectName(u"label_121")

        self.verticalLayout_111.addWidget(self.label_121)

        self.lineEdit_75 = QLineEdit(self.widget_88)
        self.lineEdit_75.setObjectName(u"lineEdit_75")

        self.verticalLayout_111.addWidget(self.lineEdit_75)


        self.verticalLayout_107.addWidget(self.widget_88)

        self.widget_89 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_89.setObjectName(u"widget_89")
        self.verticalLayout_112 = QVBoxLayout(self.widget_89)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.label_123 = QLabel(self.widget_89)
        self.label_123.setObjectName(u"label_123")

        self.verticalLayout_112.addWidget(self.label_123)

        self.label_124 = QLabel(self.widget_89)
        self.label_124.setObjectName(u"label_124")

        self.verticalLayout_112.addWidget(self.label_124)

        self.lineEdit_76 = QLineEdit(self.widget_89)
        self.lineEdit_76.setObjectName(u"lineEdit_76")

        self.verticalLayout_112.addWidget(self.lineEdit_76)

        self.label_125 = QLabel(self.widget_89)
        self.label_125.setObjectName(u"label_125")

        self.verticalLayout_112.addWidget(self.label_125)

        self.lineEdit_77 = QLineEdit(self.widget_89)
        self.lineEdit_77.setObjectName(u"lineEdit_77")

        self.verticalLayout_112.addWidget(self.lineEdit_77)


        self.verticalLayout_107.addWidget(self.widget_89)

        self.pushButton_28 = QPushButton(self.scrollAreaWidgetContents_8)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.verticalLayout_107.addWidget(self.pushButton_28)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_19.addWidget(self.scrollArea_8)

        self.rpg_stack.addWidget(self.rpg_2)
        self.rpg_2_1 = QWidget()
        self.rpg_2_1.setObjectName(u"rpg_2_1")
        self.gridLayout_19 = QGridLayout(self.rpg_2_1)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.pushButton_40 = QPushButton(self.rpg_2_1)
        self.pushButton_40.setObjectName(u"pushButton_40")

        self.gridLayout_19.addWidget(self.pushButton_40, 0, 0, 1, 1)

        self.toolButton_5 = QToolButton(self.rpg_2_1)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.gridLayout_19.addWidget(self.toolButton_5, 1, 0, 1, 1)

        self.toolButton_6 = QToolButton(self.rpg_2_1)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.gridLayout_19.addWidget(self.toolButton_6, 2, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.rpg_2_1)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_19.addWidget(self.radioButton_4, 3, 0, 1, 2)

        self.rpg_stack.addWidget(self.rpg_2_1)
        self.rpg_2_2 = QWidget()
        self.rpg_2_2.setObjectName(u"rpg_2_2")
        self.gridLayout_18 = QGridLayout(self.rpg_2_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.buttonBox_2 = QDialogButtonBox(self.rpg_2_2)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_18.addWidget(self.buttonBox_2, 0, 0, 1, 1)

        self.buttonBox_3 = QDialogButtonBox(self.rpg_2_2)
        self.buttonBox_3.setObjectName(u"buttonBox_3")
        self.buttonBox_3.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_18.addWidget(self.buttonBox_3, 1, 0, 1, 1)

        self.rpg_stack.addWidget(self.rpg_2_2)
        self.rpg_2_3 = QWidget()
        self.rpg_2_3.setObjectName(u"rpg_2_3")
        self.verticalLayout_20 = QVBoxLayout(self.rpg_2_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.radioButton_2 = QRadioButton(self.rpg_2_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_20.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.rpg_2_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_20.addWidget(self.radioButton_3)

        self.rpg_stack.addWidget(self.rpg_2_3)
        self.rpg_2_4 = QWidget()
        self.rpg_2_4.setObjectName(u"rpg_2_4")
        self.gridLayout_17 = QGridLayout(self.rpg_2_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.checkBox_4 = QCheckBox(self.rpg_2_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_17.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.rpg_2_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_17.addWidget(self.checkBox_3, 1, 1, 1, 1)

        self.rpg_stack.addWidget(self.rpg_2_4)
        self.rpg_2_5 = QWidget()
        self.rpg_2_5.setObjectName(u"rpg_2_5")
        self.gridLayout_16 = QGridLayout(self.rpg_2_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_39 = QPushButton(self.rpg_2_5)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.gridLayout_16.addWidget(self.pushButton_39, 0, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.rpg_2_5)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.gridLayout_16.addWidget(self.toolButton_4, 1, 0, 1, 1)

        self.rpg_stack.addWidget(self.rpg_2_5)

        self.gridLayout_4.addWidget(self.rpg_stack, 0, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.rpg_page_2)

        self.stackedWidget.addWidget(self.rpg_page)
        self.rrg_page = QWidget()
        self.rrg_page.setObjectName(u"rrg_page")
        self.gridLayout_5 = QGridLayout(self.rrg_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.rrg_page_in = QWidget(self.rrg_page)
        self.rrg_page_in.setObjectName(u"rrg_page_in")
        self.verticalLayout_7 = QVBoxLayout(self.rrg_page_in)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.rrg_page_in)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)


        self.gridLayout_5.addWidget(self.rrg_page_in, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.rrg_page)
        self.results_page = QWidget()
        self.results_page.setObjectName(u"results_page")
        self.verticalLayout_10 = QVBoxLayout(self.results_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.result_page_in = QWidget(self.results_page)
        self.result_page_in.setObjectName(u"result_page_in")
        self.verticalLayout_9 = QVBoxLayout(self.result_page_in)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.result_page_in)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)


        self.verticalLayout_10.addWidget(self.result_page_in)

        self.stackedWidget.addWidget(self.results_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_toggle.toggled.connect(self.icon_only_widget.setVisible)
        self.menu_toggle.toggled.connect(self.side_menu.setHidden)
        self.info_small.toggled.connect(self.information.setChecked)
        self.rpc_small.toggled.connect(self.rpc.setChecked)
        self.rpg_small.toggled.connect(self.rpg.setChecked)
        self.rrg_small.toggled.connect(self.rrg.setChecked)
        self.result_small.toggled.connect(self.results.setChecked)
        self.information.toggled.connect(self.info_small.setChecked)
        self.rpc.toggled.connect(self.rpc_small.setChecked)
        self.rpg.toggled.connect(self.rpg_small.setChecked)
        self.rrg.toggled.connect(self.rrg_small.setChecked)
        self.results.toggled.connect(self.result_small.setChecked)
        self.exit.clicked.connect(MainWindow.close)
        self.exit_small.clicked.connect(MainWindow.close)
        self.rpc.toggled.connect(self.widget_2.setVisible)
        self.rpc_small.toggled.connect(self.widget_2.setVisible)
        self.pushButton_9.toggled.connect(self.rpc_menu_1_1.setVisible)
        self.pushButton_7.toggled.connect(self.rpc_sub_mnu_2.setVisible)
        self.pushButton_7.toggled.connect(self.rpc_menu_1_1.setVisible)
        self.pushButton_7.toggled.connect(self.rpc_sub_menu1.setHidden)
        self.pushButton_9.toggled.connect(self.rpc_sub_mnu_2.setHidden)
        self.pushButton_16.toggled.connect(self.rpg_side_menu.setVisible)
        self.pushButton_16.toggled.connect(self.widget_7.setVisible)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_logo.setText("")
        self.info_small.setText("")
        self.rpc_small.setText("")
        self.rpg_small.setText("")
        self.rrg_small.setText("")
        self.result_small.setText("")
        self.exit_small.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.information.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.rpc.setText(QCoreApplication.translate("MainWindow", u"RPC", None))
        self.rpg.setText(QCoreApplication.translate("MainWindow", u"RPG", None))
        self.rrg.setText(QCoreApplication.translate("MainWindow", u"RRG", None))
        self.results.setText(QCoreApplication.translate("MainWindow", u"Resultats", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nom de l'operateur", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nom du projet", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Identification du residu", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Date de melange", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contenant pour le moulage", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Section et hauteur", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Rayon et hauteur", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Longeur, largeur et hauteur", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Composante liant hydralique", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre de ciment pour le liant", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ciment 1", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"Ciment P50", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"Ciment CP10", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Slag", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Fly Ash", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"Chaud", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ciment 2", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"Ciment P50", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"Ciment CP10", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"Slag", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"Fly Ash", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"Chaud", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ciment 3", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"Ciment P50", None))
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"Ciment CP10", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"Slag", None))
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"Fly Ash", None))
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"Chaud", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fraction du ciment 1(%):", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fraction du ciment 2(%):", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Fraction du ciment 3 (%):", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Dosage Selon C/W%", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Methode-essaie-erreur", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Dosage selon le slump", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Dosage selon W/C", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Resultats", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RPC", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Composante eau de melange", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pourcentag solide massique fixe(%):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Degre de saturation (%):", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Composante rejets", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Masse volumique specifique du residu:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Teneur en eau massique du residu:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Nombre  de recettes de melange:", None))
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_29.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Quantite desiree (nombre de contenants) par recette:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Facteur de securite:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 1:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 2:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 3:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 4:", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Calculs le remblais en pates cimentes", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"RPC", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Composante eau de melange", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique solide fixe(%):", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Composante rejets", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Degre de saturation(%):", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Masse volumique specifique du residu", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Tneur en eau massique du residu", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Melange de remblai", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Nombre de recettes de melange", None))
        self.radioButton_30.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_31.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_32.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_33.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Quantite desiree (nombre de contenants) par recette:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Facteur de securite:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 1", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 2", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 3", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 4", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Calculs remblais en pates cimentes", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"RPC", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Ajustement pour slump", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ajout d'eau additionelle (g):", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Ajout de rejet additionel(g):", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ajout d'aggregat sc additionel co-mixing(g):", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Masse  volumique specifique aggregat co-mixing(g/cm3):", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Teneur en eau massique aggregat co-mixing(%):", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Calculs remblais en pates cimentes", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Composante eau de melange", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Type de cone", None))
        self.radioButton_38.setText(QCoreApplication.translate("MainWindow", u"Mini cone", None))
        self.radioButton_39.setText(QCoreApplication.translate("MainWindow", u"Grand cone", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Slump (mm):", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Degre de saturation (%):", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Compsante rejets", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Masse volumique specifique de residu", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Teneur en masssique du residu", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Melange de remblai", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Nombre de recettes de melange", None))
        self.radioButton_37.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_36.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_34.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_35.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Quantite desiree (nombre de contenants) par recette:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Facteur de securite", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 1", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 2", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 3", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Pourcentage massique de liant dans la recette 4", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Calculs remblais en pates cimentes", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Composante eau de melange", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Degre de saturation (%):", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Composante rejets", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Masse volumique specifique du residu", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Teneur en eau massique du residu", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Melange de remblai", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Nombre de recettes de melange", None))
        self.radioButton_40.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_41.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_42.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_43.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Quantitie desiree (nombre de contenants) par recette", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Facteur de securite", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Recette 1", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 1", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 1", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Recette 2", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 2", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 2", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Recette 3", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 3", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 3", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Recette 4", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 4", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 4", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Calculs remblais en pates cimentes", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Information sur le melange", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Ajustement pour le slump", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Information sur le melange", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Donnes du melange", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Parametres geotechniques 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Parametres geotechniques 2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Parametres geotechniques 3", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Dosage Selon Cw%", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Dosage selon W/C", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Resultats", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Information sur le melange", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Donnes du melange", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Parametres geotechniques 1", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Parametres geotechniques 2", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Parametres geotechniques 3", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Composante eau de melange", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Pourcentage solide massique fixe (%):", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Degre de saturation (%):", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Composante rejets", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Masse volumique specifique du residu", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Teneur en eau massique du residu", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Melange de remblai", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Nombre de recettes de melange", None))
        self.radioButton_44.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_45.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_46.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_47.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Quantite desiree (nombre de contenants) par recette:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Facteur de securite", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 1", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 2", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 3", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 4", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Calculs remblais en pate cimentes", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Composante eau de melange", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Degre de saturation (%):", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Composante rejets", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Masse volumique specifique du residu", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Teneur en eau massique du residu", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Melange de remblai", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Nombre de recettes de melange", None))
        self.radioButton_48.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_49.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_50.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_51.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Quantite desiree (nombre de contenants) par recette:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Facteur de securite", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Recette 1", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 1", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 1", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Recette 2", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 2", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 2", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Recette 3", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 3", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 3", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Recette 4", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Pourentage massique de liant dans la recette 4", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Rapport eau/ciment recette 4", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Calculs remblais en pates cimentes", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RRG Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Results Page", None))
    # retranslateUi

