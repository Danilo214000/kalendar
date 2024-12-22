from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(10, 20, 371, 241))
        self.calendar.setGridVisible(True)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(False)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setObjectName("calendar")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(410, 20, 143, 37))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.video = QVideoWidget(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(10, 280, 561, 401))
        self.video.setObjectName("video")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.video)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(410, 80, 143, 37))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.autostart = QtWidgets.QCheckBox(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(410, 140, 124, 29))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.autostart.setFont(font)
        self.autostart.setObjectName("autostart")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Старт"))
        self.stop.setText(_translate("MainWindow", "Стоп"))
        self.autostart.setText(_translate("MainWindow", "Автостарт"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())