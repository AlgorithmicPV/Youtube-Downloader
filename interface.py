import pytube
from pytube import YouTube
import time

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerStNFci.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 622)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(71, 61))
        self.label_11.setMaximumSize(QSize(71, 61))
        self.label_11.setPixmap(QPixmap(u":/icons/download-alt-3-svgrepo-com.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame_15)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(48)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_8.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color:rgb(255, 0, 0);")

        self.horizontalLayout_8.addWidget(self.label_9, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"border-radius:18%;\n"
"background-color: rgba(255, 255, 255, 0.173);\n"
"padding:5px;")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton:hover{\n"
"	background-color:rgba(255, 255, 255, 0.173);\n"
"	border-radius:18%;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.226);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_5)

        self.toolButton_2 = QToolButton(self.frame_4)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setStyleSheet(u"QToolButton:hover{\n"
"	background-color:rgba(255, 255, 255, 0.173);\n"
"	border-radius:15%;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.toolButton_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout.addWidget(self.label_4)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.226);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 49, 16))
        self.toolButton_4 = QToolButton(self.frame_6)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(70, 10, 21, 22))
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(60, 60, 120, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.toolButton_5 = QToolButton(self.frame_7)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(70, 10, 21, 22))
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 138, 45))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_9)

        self.toolButton_6 = QToolButton(self.frame_8)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.horizontalLayout_3.addWidget(self.toolButton_6)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_16)

        self.toolButton_10 = QToolButton(self.frame_12)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setStyleSheet(u"QToolButton:hover{\n"
"	background-color:rgba(255, 255, 255, 0.173);\n"
"	border-radius:15%;\n"
"}")
        self.toolButton_10.setIcon(icon1)
        self.toolButton_10.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.toolButton_10)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_13)

        self.toolButton_8 = QToolButton(self.frame_10)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setStyleSheet(u"QToolButton:hover{\n"
"	background-color:rgba(255, 255, 255, 0.173);\n"
"	border-radius:15%;\n"
"}")
        self.toolButton_8.setIcon(icon1)
        self.toolButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.toolButton_8)


        self.verticalLayout.addWidget(self.frame_10)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color:rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.label_10.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube Downloader", None))
        
        self.label_11.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Downloader", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Keywords or paste Youtube link here", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Download", None))
#endif // QT_CONFIG(statustip)
        self.toolButton.setText("")
#if QT_CONFIG(shortcut)
        self.toolButton.setShortcut(QCoreApplication.translate("MainWindow", u"Enter, Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Download", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.toolButton_4.setText("")
        self.toolButton_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1080p (.mp4)", None))
        self.toolButton_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"360 (.mp4)", None))
#if QT_CONFIG(tooltip)
        self.toolButton_10.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton_10.setStatusTip(QCoreApplication.translate("MainWindow", u"Download", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_10.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"720p (.mp4)", None))
#if QT_CONFIG(tooltip)
        self.toolButton_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton_8.setStatusTip(QCoreApplication.translate("MainWindow", u"Download", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_8.setText("")
        self.label_12.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Powered by G.A.Pasindu Vidunitha", None))
    # retranslateUi




##################################backend program#########################################
##########################################################################################
##########################################################################################
        
        self.toolButton_10.setEnabled(False)
        self.toolButton_2.setEnabled(False)
        self.toolButton_4.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        self.toolButton_6.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        self.toolButton_8.setEnabled(False)


        self.toolButton.clicked.connect(self.convert)
        self.toolButton_2.clicked.connect(self.mp3converter)
        self.toolButton_10.clicked.connect(self.mp4converter360)
        self.toolButton_8.clicked.connect(self.mp4converter720)
    
    def convert(self):
        self.toolButton_10.setEnabled(True)
        self.toolButton_2.setEnabled(True)
        self.toolButton_4.setEnabled(True)
        self.toolButton_5.setEnabled(True)
        self.toolButton_6.setEnabled(True)
        self.toolButton_5.setEnabled(True)
        self.toolButton_8.setEnabled(True)

        utubelink = self.lineEdit.text()

        yt = YouTube(utubelink)

    def mp3converter(self):
        filepath = "D:/YoutubeDownloader/"
        url = self.lineEdit.text()

        try:
                video = YouTube(url)
                audio_stream = video.streams.filter(only_audio=True, file_extension="mp4").first()
        
                if not audio_stream:
                    raise ValueError("No MP3 stream available for this video.")
        
                audio_stream.download(output_path=filepath, filename=f"{video.title}.mp3")
                self.label_12.setText("The audio is downloaded in MP3")
        except ValueError as ve:
                self.label_12.setText(str(ve))
        except Exception as e:
               self.label_12.setText(f"Error: {str(e)}")
        finally:
                self.lineEdit.clear()
                self.toolButton_10.setEnabled(False)
                self.toolButton_2.setEnabled(False)
                self.toolButton_4.setEnabled(False)
                self.toolButton_5.setEnabled(False)
                self.toolButton_6.setEnabled(False)
                self.toolButton_5.setEnabled(False)
                self.toolButton_8.setEnabled(False)

        
    def mp4converter360(self):
        filepath = "D:/YoutubeDownloader/"
        url = self.lineEdit.text()

        try:
            video = YouTube(url)
            stream = video.streams.filter(file_extension="mp4", resolution="720p").first()
            stream.download(output_path=filepath, filename=f"{video.title}.mp4")
            self.label_12.setText("The video is downloaded in MP4 (360)")
        except Exception as e:
            self.label_12.setText(f"Error: {e}")
        self.lineEdit.clear()
        self.toolButton_10.setEnabled(False)
        self.toolButton_2.setEnabled(False)
        self.toolButton_4.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        self.toolButton_6.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        self.toolButton_8.setEnabled(False)


    
    def mp4converter720(self):
        filepath = "D:/YoutubeDownloader/"
        url = self.lineEdit.text()

        try:
            video = YouTube(url)
            stream = video.streams.filter(file_extension="mp4", resolution="720p").first()
            stream.download(output_path=filepath,filename=f"{video.title}.mp4")
            self.label_12.setText("The video is downloaded in MP4 (720)")
        except Exception as e:
            self.label_12.setText(f"Error: {e}")
        self.lineEdit.clear()
        self.toolButton_10.setEnabled(False)
        self.toolButton_2.setEnabled(False)
        self.toolButton_4.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        self.toolButton_6.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        self.toolButton_8.setEnabled(False)



