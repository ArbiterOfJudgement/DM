# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 725)
        MainWindow.setMinimumSize(QtCore.QSize(500, 725))
        MainWindow.setMaximumSize(QtCore.QSize(500, 725))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 701))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.TSA_tab = QtWidgets.QWidget()
        self.TSA_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TSA_tab.setObjectName("TSA_tab")
        self.tabWidget.addTab(self.TSA_tab, "")
        self.MDC_tab = QtWidgets.QWidget()
        self.MDC_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MDC_tab.setObjectName("MDC_tab")
        self.tabWidget.addTab(self.MDC_tab, "")
        self.DBSCAN_tab = QtWidgets.QWidget()
        self.DBSCAN_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DBSCAN_tab.setObjectName("DBSCAN_tab")
        self.tabWidget.addTab(self.DBSCAN_tab, "")
        self.RNN_tab = QtWidgets.QWidget()
        self.RNN_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.RNN_tab.setObjectName("RNN_tab")
        self.tabWidget.addTab(self.RNN_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.administrator_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.administrator_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.administrator_button.setObjectName("administrator_button")
        self.horizontalLayout.addWidget(self.administrator_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.language_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.language_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.language_comboBox.setObjectName("language_comboBox")
        self.horizontalLayout.addWidget(self.language_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TSA_tab), _translate("MainWindow", "Анализ временных рядов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MDC_tab), _translate("MainWindow", "Сжатие данных"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DBSCAN_tab), _translate("MainWindow", "DBSACN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RNN_tab), _translate("MainWindow", "Прогнозирование качества"))
        self.administrator_button.setText(_translate("MainWindow", "Настройка моделей"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())