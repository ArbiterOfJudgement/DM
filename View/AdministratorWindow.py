# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Administrator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdministratorWindow(object):
    def setupUi(self, AdministratorWindow):
        AdministratorWindow.setObjectName("AdministratorWindow")
        AdministratorWindow.resize(400, 725)
        self.verticalLayoutWidget = QtWidgets.QWidget(AdministratorWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TSA_group = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.TSA_group.setObjectName("TSA_group")
        self.verticalLayout.addWidget(self.TSA_group)
        self.RNN_group = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.RNN_group.setObjectName("RNN_group")
        self.verticalLayout.addWidget(self.RNN_group)
        self.DBSCAN_group = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.DBSCAN_group.setObjectName("DBSCAN_group")
        self.verticalLayout.addWidget(self.DBSCAN_group)
        self.MDC_group = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.MDC_group.setObjectName("MDC_group")
        self.verticalLayout.addWidget(self.MDC_group)

        self.retranslateUi(AdministratorWindow)
        QtCore.QMetaObject.connectSlotsByName(AdministratorWindow)

    def retranslateUi(self, AdministratorWindow):
        _translate = QtCore.QCoreApplication.translate
        AdministratorWindow.setWindowTitle(_translate("AdministratorWindow", "AdministratorWindow"))
        self.TSA_group.setTitle(_translate("AdministratorWindow", "Анализ временных рядов"))
        self.RNN_group.setTitle(_translate("AdministratorWindow", "Прогнозирование качества"))
        self.DBSCAN_group.setTitle(_translate("AdministratorWindow", "DBSCAN"))
        self.MDC_group.setTitle(_translate("AdministratorWindow", "Сжатие данных"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdministratorWindow = QtWidgets.QWidget()
    ui = Ui_AdministratorWindow()
    ui.setupUi(AdministratorWindow)
    AdministratorWindow.show()
    sys.exit(app.exec_())