# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created: Wed Dec 25 21:03:49 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(656, 536)
        self.tabWidget = QtGui.QTabWidget(notepad)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 521))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Enrollment = QtGui.QWidget()
        self.Enrollment.setObjectName(_fromUtf8("Enrollment"))
        self.groupBox = QtGui.QGroupBox(self.Enrollment)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 401, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 40, 243, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Username = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Username.setPlaceholderText(_fromUtf8(""))
        self.Username.setObjectName(_fromUtf8("Username"))
        self.horizontalLayout_2.addWidget(self.Username)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Userage = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.Userage.setMaximum(100)
        self.Userage.setProperty("value", 20)
        self.Userage.setObjectName(_fromUtf8("Userage"))
        self.horizontalLayout_3.addWidget(self.Userage)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.Usersex = QtGui.QComboBox(self.verticalLayoutWidget)
        self.Usersex.setObjectName(_fromUtf8("Usersex"))
        self.Usersex.addItem(_fromUtf8(""))
        self.Usersex.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.Usersex)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 131, 151))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Userimage = QtGui.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Userimage.sizePolicy().hasHeightForWidth())
        self.Userimage.setSizePolicy(sizePolicy)
        self.Userimage.setText(_fromUtf8(""))
        self.Userimage.setObjectName(_fromUtf8("Userimage"))
        self.verticalLayout_2.addWidget(self.Userimage)
        self.UploadImage = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.UploadImage.setObjectName(_fromUtf8("UploadImage"))
        self.verticalLayout_2.addWidget(self.UploadImage)
        self.groupBox_2 = QtGui.QGroupBox(self.Enrollment)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 601, 241))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Textreading = QtGui.QTextBrowser(self.groupBox_2)
        self.Textreading.setGeometry(QtCore.QRect(0, 60, 581, 101))
        self.Textreading.setObjectName(_fromUtf8("Textreading"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(0, 30, 431, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Animation = QtGui.QLabel(self.groupBox_2)
        self.Animation.setGeometry(QtCore.QRect(10, 180, 61, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Animation.sizePolicy().hasHeightForWidth())
        self.Animation.setSizePolicy(sizePolicy)
        self.Animation.setText(_fromUtf8(""))
        self.Animation.setObjectName(_fromUtf8("Animation"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 180, 491, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Startrecord = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Startrecord.setObjectName(_fromUtf8("Startrecord"))
        self.horizontalLayout.addWidget(self.Startrecord)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.Choose_file = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Choose_file.setObjectName(_fromUtf8("Choose_file"))
        self.horizontalLayout.addWidget(self.Choose_file)
        self.Filename = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.Filename.setObjectName(_fromUtf8("Filename"))
        self.horizontalLayout.addWidget(self.Filename)
        self.Upload = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Upload.setObjectName(_fromUtf8("Upload"))
        self.horizontalLayout.addWidget(self.Upload)
        self.tabWidget.addTab(self.Enrollment, _fromUtf8(""))
        self.Recognition = QtGui.QWidget()
        self.Recognition.setObjectName(_fromUtf8("Recognition"))
        self.groupBox_3 = QtGui.QGroupBox(self.Recognition)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 561, 431))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(270, 40, 271, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.Claimname = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.Claimname.setObjectName(_fromUtf8("Claimname"))
        self.horizontalLayout_6.addWidget(self.Claimname)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 251, 51))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Startrecord_2 = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.Startrecord_2.setObjectName(_fromUtf8("Startrecord_2"))
        self.horizontalLayout_7.addWidget(self.Startrecord_2)
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget_4)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_7.addWidget(self.progressBar)
        self.Verificationimage = QtGui.QGraphicsView(self.groupBox_3)
        self.Verificationimage.setGeometry(QtCore.QRect(320, 160, 131, 131))
        self.Verificationimage.setObjectName(_fromUtf8("Verificationimage"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(160, 160, 121, 131))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Username_2 = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Username_2.sizePolicy().hasHeightForWidth())
        self.Username_2.setSizePolicy(sizePolicy)
        self.Username_2.setObjectName(_fromUtf8("Username_2"))
        self.verticalLayout_3.addWidget(self.Username_2)
        self.EditInfo = QtGui.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditInfo.sizePolicy().hasHeightForWidth())
        self.EditInfo.setSizePolicy(sizePolicy)
        self.EditInfo.setObjectName(_fromUtf8("EditInfo"))
        self.verticalLayout_3.addWidget(self.EditInfo)
        self.Clear = QtGui.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clear.sizePolicy().hasHeightForWidth())
        self.Clear.setSizePolicy(sizePolicy)
        self.Clear.setObjectName(_fromUtf8("Clear"))
        self.verticalLayout_3.addWidget(self.Clear)
        self.UserImage_2 = QtGui.QGraphicsView(self.groupBox_3)
        self.UserImage_2.setGeometry(QtCore.QRect(10, 160, 131, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserImage_2.sizePolicy().hasHeightForWidth())
        self.UserImage_2.setSizePolicy(sizePolicy)
        self.UserImage_2.setObjectName(_fromUtf8("UserImage_2"))
        self.tabWidget.addTab(self.Recognition, _fromUtf8(""))
        self.Conversation = QtGui.QWidget()
        self.Conversation.setObjectName(_fromUtf8("Conversation"))
        self.groupBox_4 = QtGui.QGroupBox(self.Conversation)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 170, 221, 301))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox_4)
        self.textBrowser.setGeometry(QtCore.QRect(0, 30, 191, 211))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.Saveas = QtGui.QPushButton(self.groupBox_4)
        self.Saveas.setGeometry(QtCore.QRect(0, 250, 96, 31))
        self.Saveas.setObjectName(_fromUtf8("Saveas"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(100, 250, 96, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_5 = QtGui.QGroupBox(self.Conversation)
        self.groupBox_5.setGeometry(QtCore.QRect(100, 170, 141, 211))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.UserImage_3 = QtGui.QGraphicsView(self.groupBox_5)
        self.UserImage_3.setGeometry(QtCore.QRect(0, 30, 131, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserImage_3.sizePolicy().hasHeightForWidth())
        self.UserImage_3.setSizePolicy(sizePolicy)
        self.UserImage_3.setObjectName(_fromUtf8("UserImage_3"))
        self.Username_3 = QtGui.QLineEdit(self.groupBox_5)
        self.Username_3.setGeometry(QtCore.QRect(0, 170, 131, 33))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Username_3.sizePolicy().hasHeightForWidth())
        self.Username_3.setSizePolicy(sizePolicy)
        self.Username_3.setObjectName(_fromUtf8("Username_3"))
        self.Startrecord_3 = QtGui.QPushButton(self.Conversation)
        self.Startrecord_3.setGeometry(QtCore.QRect(240, 70, 91, 31))
        self.Startrecord_3.setObjectName(_fromUtf8("Startrecord_3"))
        self.Recordtime = QtGui.QLabel(self.Conversation)
        self.Recordtime.setGeometry(QtCore.QRect(260, 120, 51, 21))
        self.Recordtime.setObjectName(_fromUtf8("Recordtime"))
        self.tabWidget.addTab(self.Conversation, _fromUtf8(""))
        self.Video = QtGui.QWidget()
        self.Video.setObjectName(_fromUtf8("Video"))
        self.mdiArea = QtGui.QMdiArea(self.Video)
        self.mdiArea.setGeometry(QtCore.QRect(30, 110, 301, 201))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.horizontalSlider = QtGui.QSlider(self.Video)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 310, 301, 51))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.OpenVideo = QtGui.QPushButton(self.Video)
        self.OpenVideo.setGeometry(QtCore.QRect(30, 60, 96, 31))
        self.OpenVideo.setObjectName(_fromUtf8("OpenVideo"))
        self.label_7 = QtGui.QLabel(self.Video)
        self.label_7.setGeometry(QtCore.QRect(180, 190, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.Video, _fromUtf8(""))

        self.retranslateUi(notepad)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "Speaker Recognition", None))
        self.groupBox.setTitle(_translate("notepad", "User Info", None))
        self.label_2.setText(_translate("notepad", "Name:", None))
        self.label_3.setText(_translate("notepad", "Age:   ", None))
        self.label_4.setText(_translate("notepad", "Sex:   ", None))
        self.Usersex.setItemText(0, _translate("notepad", "Male", None))
        self.Usersex.setItemText(1, _translate("notepad", "Female", None))
        self.UploadImage.setText(_translate("notepad", "Upload Photo", None))
        self.groupBox_2.setTitle(_translate("notepad", "Voice Enrollment", None))
        self.Textreading.setHtml(_translate("notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Youth is not a time of life; it is a state of mind; it is not a matter of rosy cheeks, red lips and supple knees; it is a matter of the will, a quality of the imagination, a vigor of the emotions; it is the freshness of the deep springs of life. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(_translate("notepad", "Press \"Record\" and read the following text as clearly as you can.", None))
        self.Startrecord.setText(_translate("notepad", "Record", None))
        self.label_6.setText(_translate("notepad", "Or", None))
        self.Choose_file.setText(_translate("notepad", "Choose File...", None))
        self.Upload.setText(_translate("notepad", "Upload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Enrollment), _translate("notepad", "Enrollment", None))
        self.groupBox_3.setTitle(_translate("notepad", "Recognition", None))
        self.label.setText(_translate("notepad", "Claim your identity:", None))
        self.Startrecord_2.setText(_translate("notepad", "Record", None))
        self.EditInfo.setText(_translate("notepad", "EditInfo", None))
        self.Clear.setText(_translate("notepad", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Recognition), _translate("notepad", "Recognition", None))
        self.groupBox_4.setTitle(_translate("notepad", "Conversation Info", None))
        self.Saveas.setText(_translate("notepad", "Save as..", None))
        self.pushButton.setText(_translate("notepad", "Clear", None))
        self.groupBox_5.setTitle(_translate("notepad", "Current Speaker", None))
        self.Startrecord_3.setText(_translate("notepad", "Record", None))
        self.Recordtime.setText(_translate("notepad", "00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Conversation), _translate("notepad", "Conversation Mode", None))
        self.OpenVideo.setText(_translate("notepad", "Open...", None))
        self.label_7.setText(_translate("notepad", "This page is under construction", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Video), _translate("notepad", "Video Mode", None))

