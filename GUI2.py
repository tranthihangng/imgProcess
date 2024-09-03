# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/PiMageGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PiMage(object):
    def setupUi(self, PiMage):
        PiMage.setObjectName("PiMage")
        PiMage.resize(1009, 718)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PiMage.sizePolicy().hasHeightForWidth())
        PiMage.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(PiMage)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(10, 10, 741, 421))
        self.imageLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageLabel.setLineWidth(1)
        self.imageLabel.setText("")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.rightToolsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.rightToolsGroupBox.setGeometry(QtCore.QRect(760, 10, 201, 421))
        self.rightToolsGroupBox.setObjectName("rightToolsGroupBox")
        self.applyButton = QtWidgets.QPushButton(self.rightToolsGroupBox)
        self.applyButton.setGeometry(QtCore.QRect(50, 380, 101, 31))
        self.applyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.applyButton.setObjectName("applyButton")
        self.revertButton = QtWidgets.QPushButton(self.rightToolsGroupBox)
        self.revertButton.setGeometry(QtCore.QRect(50, 340, 101, 31))
        self.revertButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.revertButton.setObjectName("revertButton")
        self.enhancementTextLabel = QtWidgets.QLabel(self.rightToolsGroupBox)
        self.enhancementTextLabel.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.enhancementTextLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.enhancementTextLabel.setObjectName("enhancementTextLabel")
        self.contrastTextLabel = QtWidgets.QLabel(self.rightToolsGroupBox)
        self.contrastTextLabel.setGeometry(QtCore.QRect(20, 130, 51, 16))
        self.contrastTextLabel.setObjectName("contrastTextLabel")
        self.brightnessSlider = QtWidgets.QSlider(self.rightToolsGroupBox)
        self.brightnessSlider.setGeometry(QtCore.QRect(20, 90, 160, 22))
        self.brightnessSlider.setMinimum(-200)
        self.brightnessSlider.setMaximum(200)
        self.brightnessSlider.setProperty("value", 0)
        self.brightnessSlider.setSliderPosition(0)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.contrastSlider = QtWidgets.QSlider(self.rightToolsGroupBox)
        self.contrastSlider.setGeometry(QtCore.QRect(20, 160, 160, 22))
        self.contrastSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.contrastSlider.setMinimum(1)
        self.contrastSlider.setMaximum(30)
        self.contrastSlider.setSingleStep(1)
        self.contrastSlider.setProperty("value", 10)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")
        self.brightnessTextLabel = QtWidgets.QLabel(self.rightToolsGroupBox)
        self.brightnessTextLabel.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.brightnessTextLabel.setObjectName("brightnessTextLabel")
        self.histogramNormalButton = QtWidgets.QPushButton(self.rightToolsGroupBox)
        self.histogramNormalButton.setGeometry(QtCore.QRect(10, 260, 181, 31))
        self.histogramNormalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.histogramNormalButton.setObjectName("histogramNormalButton")
        self.autoEnhancementTextLabel = QtWidgets.QLabel(self.rightToolsGroupBox)
        self.autoEnhancementTextLabel.setGeometry(QtCore.QRect(20, 240, 161, 20))
        self.autoEnhancementTextLabel.setObjectName("autoEnhancementTextLabel")
        self.contrastEnhancementButton = QtWidgets.QPushButton(self.rightToolsGroupBox)
        self.contrastEnhancementButton.setGeometry(QtCore.QRect(10, 300, 181, 31))
        self.contrastEnhancementButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.contrastEnhancementButton.setObjectName("contrastEnhancementButton")
        self.inverseButton = QtWidgets.QPushButton(self.rightToolsGroupBox)
        self.inverseButton.setGeometry(QtCore.QRect(60, 200, 81, 31))
        self.inverseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inverseButton.setObjectName("inverseButton")
        self.brightnessValueLabel = QtWidgets.QLabel(self.rightToolsGroupBox)
        self.brightnessValueLabel.setGeometry(QtCore.QRect(150, 60, 31, 20))
        self.brightnessValueLabel.setObjectName("brightnessValueLabel")
        self.contrastValueLabel = QtWidgets.QLabel(self.rightToolsGroupBox)
        self.contrastValueLabel.setGeometry(QtCore.QRect(150, 130, 31, 20))
        self.contrastValueLabel.setObjectName("contrastValueLabel")
        self.applyManuelButton = QtWidgets.QPushButton(self.rightToolsGroupBox)
        self.applyManuelButton.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.applyManuelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.applyManuelButton.setObjectName("applyManuelButton")
        self.filtersGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.filtersGroupBox.setGeometry(QtCore.QRect(10, 440, 951, 231))
        self.filtersGroupBox.setObjectName("filtersGroupBox")
        self.listWidget = QtWidgets.QListWidget(self.filtersGroupBox)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 951, 201))
        self.listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        PiMage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PiMage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRotate = QtWidgets.QMenu(self.menuEdit)
        self.menuRotate.setObjectName("menuRotate")
        self.menuFlip = QtWidgets.QMenu(self.menuEdit)
        self.menuFlip.setObjectName("menuFlip")
        self.menuShare = QtWidgets.QMenu(self.menubar)
        self.menuShare.setObjectName("menuShare")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        PiMage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PiMage)
        self.statusbar.setObjectName("statusbar")
        PiMage.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(PiMage)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(PiMage)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(PiMage)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(PiMage)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRemove = QtWidgets.QAction(PiMage)
        self.actionRemove.setObjectName("actionRemove")
        self.actionRemove_Image = QtWidgets.QAction(PiMage)
        self.actionRemove_Image.setObjectName("actionRemove_Image")
        self.actionCrop = QtWidgets.QAction(PiMage)
        self.actionCrop.setObjectName("actionCrop")
        self.actionResize = QtWidgets.QAction(PiMage)
        self.actionResize.setObjectName("actionResize")
        self.actionVertical = QtWidgets.QAction(PiMage)
        self.actionVertical.setObjectName("actionVertical")
        self.actionHorizontal = QtWidgets.QAction(PiMage)
        self.actionHorizontal.setObjectName("actionHorizontal")
        self.actionVertical_Horizontal = QtWidgets.QAction(PiMage)
        self.actionVertical_Horizontal.setObjectName("actionVertical_Horizontal")
        self.action90 = QtWidgets.QAction(PiMage)
        self.action90.setObjectName("action90")
        self.action180 = QtWidgets.QAction(PiMage)
        self.action180.setObjectName("action180")
        self.action270 = QtWidgets.QAction(PiMage)
        self.action270.setObjectName("action270")
        self.actionGet_link = QtWidgets.QAction(PiMage)
        self.actionGet_link.setObjectName("actionGet_link")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRemove_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRotate.addAction(self.action90)
        self.menuRotate.addAction(self.action180)
        self.menuRotate.addAction(self.action270)
        self.menuFlip.addAction(self.actionVertical)
        self.menuFlip.addAction(self.actionHorizontal)
        self.menuFlip.addAction(self.actionVertical_Horizontal)
        self.menuEdit.addAction(self.actionCrop)
        self.menuEdit.addAction(self.menuRotate.menuAction())
        self.menuEdit.addAction(self.menuFlip.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuShare.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())

        self.retranslateUi(PiMage)
        QtCore.QMetaObject.connectSlotsByName(PiMage)

    def retranslateUi(self, PiMage):
        _translate = QtCore.QCoreApplication.translate
        PiMage.setWindowTitle(_translate("PiMage", "PiMage"))
        self.rightToolsGroupBox.setTitle(_translate("PiMage", "Other Tools"))
        self.applyButton.setToolTip(_translate("PiMage", "<html><head/><body><p>Applies only selected filter to the image.</p></body></html>"))
        self.applyButton.setText(_translate("PiMage", "Apply Filter"))
        self.revertButton.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.revertButton.setText(_translate("PiMage", "Revert Changes"))
        self.enhancementTextLabel.setText(_translate("PiMage", "Enhancement:"))
        self.contrastTextLabel.setText(_translate("PiMage", "Contrast:"))
        self.brightnessTextLabel.setText(_translate("PiMage", "Brightness:"))
        self.histogramNormalButton.setText(_translate("PiMage", "Histogram Normalization"))
        self.autoEnhancementTextLabel.setText(_translate("PiMage", "Automatic Enhancement:"))
        self.contrastEnhancementButton.setText(_translate("PiMage", "Contrast Enhancement"))
        self.inverseButton.setText(_translate("PiMage", "Inverse"))
        self.brightnessValueLabel.setText(_translate("PiMage", "0"))
        self.contrastValueLabel.setText(_translate("PiMage", "1"))
        self.applyManuelButton.setToolTip(_translate("PiMage", "<html><head/><body><p>Applies only brightness and contrast changes.</p></body></html>"))
        self.applyManuelButton.setText(_translate("PiMage", "Apply"))
        self.filtersGroupBox.setTitle(_translate("PiMage", "Filters"))
        self.menuFile.setTitle(_translate("PiMage", "File"))
        self.menuEdit.setTitle(_translate("PiMage", "Edit"))
        self.menuRotate.setTitle(_translate("PiMage", "Rotate"))
        self.menuFlip.setTitle(_translate("PiMage", "Flip"))
        self.menuShare.setTitle(_translate("PiMage", "Share"))
        self.menuAdd.setTitle(_translate("PiMage", "Add"))
        self.actionOpen.setText(_translate("PiMage", "Open"))
        self.actionSave.setText(_translate("PiMage", "Save"))
        self.actionSave_as.setText(_translate("PiMage", "Save as.."))
        self.actionQuit.setText(_translate("PiMage", "Quit"))
        self.actionRemove.setText(_translate("PiMage", "Remove"))
        self.actionRemove_Image.setText(_translate("PiMage", "Remove Image"))
        self.actionCrop.setText(_translate("PiMage", "Crop"))
        self.actionResize.setText(_translate("PiMage", "Resize"))
        self.actionVertical.setText(_translate("PiMage", "Vertical"))
        self.actionHorizontal.setText(_translate("PiMage", "Horizontal"))
        self.actionVertical_Horizontal.setText(_translate("PiMage", "Vertical and Horizontal"))
        self.action90.setText(_translate("PiMage", "90"))
        self.action180.setText(_translate("PiMage", "180"))
        self.action270.setText(_translate("PiMage", "270"))
        self.actionGet_link.setText(_translate("PiMage", "Get link"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PiMage = QtWidgets.QMainWindow()
    ui = Ui_PiMage()
    ui.setupUi(PiMage)
    PiMage.show()
    sys.exit(app.exec_())
