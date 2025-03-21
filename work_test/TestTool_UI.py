# -*- coding: utf-8 -*-


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPlainTextEdit,
                               QPushButton, QSizePolicy, QStatusBar, QWidget)


class Ui_Testtool(object):
    def setupUi(self, Testtool):
        if not Testtool.objectName():
            Testtool.setObjectName(u"Testtool")
        Testtool.resize(510, 451)
        self.centralwidget = QWidget(Testtool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.choose_roll_back = QPlainTextEdit(self.centralwidget)
        self.choose_roll_back.setObjectName(u"choose_roll_back")
        self.choose_roll_back.setGeometry(QRect(260, 60, 151, 31))
        self.choose_roll_back.setCursorWidth(0)
        self.date = QPlainTextEdit(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(260, 140, 151, 31))
        self.commit_id = QPlainTextEdit(self.centralwidget)
        self.commit_id.setObjectName(u"commit_id")
        self.commit_id.setGeometry(QRect(260, 100, 151, 31))
        self.umdkmddownload = QPushButton(self.centralwidget)
        self.umdkmddownload.setObjectName(u"umdkmddownload")
        self.umdkmddownload.setGeometry(QRect(310, 200, 101, 24))
        self.logoutput = QPlainTextEdit(self.centralwidget)
        self.logoutput.setObjectName(u"logoutput")
        self.logoutput.setGeometry(QRect(10, 30, 211, 381))
        self.logoutput.setReadOnly(True)
        self.kerneldownload = QPushButton(self.centralwidget)
        self.kerneldownload.setObjectName(u"kerneldownload")
        self.kerneldownload.setGeometry(QRect(310, 230, 101, 24))
        self.uefidownload = QPushButton(self.centralwidget)
        self.uefidownload.setObjectName(u"uefidownload")
        self.uefidownload.setGeometry(QRect(310, 260, 101, 24))
        Testtool.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Testtool)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 510, 22))
        Testtool.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Testtool)
        self.statusbar.setObjectName(u"statusbar")
        Testtool.setStatusBar(self.statusbar)

        self.retranslateUi(Testtool)
        self.choose_roll_back.windowIconTextChanged.connect(self.umdkmddownload.click)

        QMetaObject.connectSlotsByName(Testtool)

    # setupUi

    def retranslateUi(self, Testtool):
        Testtool.setWindowTitle(QCoreApplication.translate("Testtool", u"MainWindow", None))
        self.choose_roll_back.setPlainText(QCoreApplication.translate("Testtool", u"umd/kmd/kernel/uefi", None))
        self.date.setPlainText(QCoreApplication.translate("Testtool", u"\u8bf7\u8f93\u5165\u65e5\u671f", None))
        self.commit_id.setPlainText(QCoreApplication.translate("Testtool", u"commit id ", None))
        self.umdkmddownload.setText(QCoreApplication.translate("Testtool", u"umd/kmd \u4e0b\u8f7d", None))
        self.kerneldownload.setText(QCoreApplication.translate("Testtool", u"kernel \u4e0b\u8f7d", None))
        self.uefidownload.setText(QCoreApplication.translate("Testtool", u"uefi \u4e0b\u8f7d", None))
    # retranslateUi
