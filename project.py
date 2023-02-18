from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt6.uic import load_ui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 678)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dashbord = QtWidgets.QWidget(parent=self.centralwidget)
        self.dashbord.setGeometry(QtCore.QRect(0, 0, 931, 651))
        self.dashbord.setObjectName("dashbord")
        self.VIEW = QtWidgets.QWidget(parent=self.dashbord)
        self.VIEW.setGeometry(QtCore.QRect(20, 50, 881, 491))
        self.VIEW.setObjectName("VIEW")
        self.CROP = QtWidgets.QPushButton(parent=self.dashbord)
        self.CROP.setGeometry(QtCore.QRect(290, 610, 41, 28))
        self.CROP.setObjectName("CROP")
        self.FILTERS = QtWidgets.QPushButton(parent=self.dashbord)
        self.FILTERS.setGeometry(QtCore.QRect(460, 580, 61, 28))
        self.FILTERS.setObjectName("FILTERS")
        self.ROTATE = QtWidgets.QPushButton(parent=self.dashbord)
        self.ROTATE.setGeometry(QtCore.QRect(540, 580, 61, 28))
        self.ROTATE.setObjectName("ROTATE")
        self.Height = QtWidgets.QDoubleSpinBox(parent=self.dashbord)
        self.Height.setGeometry(QtCore.QRect(240, 580, 62, 22))
        self.Height.setObjectName("Height")
        self.Width = QtWidgets.QDoubleSpinBox(parent=self.dashbord)
        self.Width.setGeometry(QtCore.QRect(320, 580, 62, 22))
        self.Width.setObjectName("Width")
        self.Height_label = QtWidgets.QLabel(parent=self.dashbord)
        self.Height_label.setGeometry(QtCore.QRect(240, 560, 41, 16))
        self.Height_label.setObjectName("Height_label")
        self.Width_label = QtWidgets.QLabel(parent=self.dashbord)
        self.Width_label.setGeometry(QtCore.QRect(320, 560, 51, 16))
        self.Width_label.setObjectName("Width_label")
        self.Open = QtWidgets.QPushButton(parent=self.dashbord)
        self.Open.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.Open.setObjectName("Open")
        self.Save = QtWidgets.QPushButton(parent=self.dashbord)
        self.Save.setGeometry(QtCore.QRect(120, 10, 93, 28))
        self.Save.setObjectName("Save")
        self.SaveAs = QtWidgets.QPushButton(parent=self.dashbord)
        self.SaveAs.setGeometry(QtCore.QRect(230, 10, 93, 28))
        self.SaveAs.setObjectName("SaveAs")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CROP.setText(_translate("MainWindow", "CROP"))
        self.FILTERS.setText(_translate("MainWindow", "FILTER"))
        self.ROTATE.setText(_translate("MainWindow", "ROTATE"))
        self.Height_label.setText(_translate("MainWindow", "Height"))
        self.Width_label.setText(_translate("MainWindow", "Width"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.SaveAs.setText(_translate("MainWindow", "Save As"))
        self.Open.clicked.connect(self.open_file)
 
    def open_file(self):
        fname=QFileDialog.getOpenFileName()   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
