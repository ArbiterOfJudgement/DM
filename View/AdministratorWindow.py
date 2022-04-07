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
        AdministratorWindow.resize(500, 800)
        AdministratorWindow.setMinimumSize(QtCore.QSize(500, 800))
        AdministratorWindow.setMaximumSize(QtCore.QSize(500, 800))
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(AdministratorWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 501, 801))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.TSA_tab = QtWidgets.QWidget()
        self.TSA_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TSA_tab.setObjectName("TSA_tab")
        self.tabWidget_2.addTab(self.TSA_tab, "")
        self.MDC_tab = QtWidgets.QWidget()
        self.MDC_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MDC_tab.setObjectName("MDC_tab")
        self.tabWidget_2.addTab(self.MDC_tab, "")
        self.DBSCAN_tab = QtWidgets.QWidget()
        self.DBSCAN_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DBSCAN_tab.setObjectName("DBSCAN_tab")
        self.tabWidget_2.addTab(self.DBSCAN_tab, "")
        self.RNN_tab = QtWidgets.QWidget()
        self.RNN_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.RNN_tab.setObjectName("RNN_tab")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.RNN_tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 9, 491, 741))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ModelsDbGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.ModelsDbGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 170))
        self.ModelsDbGroupBoxRNN.setObjectName("ModelsDbGroupBoxRNN")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.ModelsDbGroupBoxRNN)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 20, 471, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ModelsTableWidgetRNN = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.ModelsTableWidgetRNN.setObjectName("ModelsTableWidgetRNN")
        self.ModelsTableWidgetRNN.setColumnCount(0)
        self.ModelsTableWidgetRNN.setRowCount(0)
        self.verticalLayout_2.addWidget(self.ModelsTableWidgetRNN)
        self.DeleteModelPushButtonRNN = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.DeleteModelPushButtonRNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeleteModelPushButtonRNN.setObjectName("DeleteModelPushButtonRNN")
        self.verticalLayout_2.addWidget(self.DeleteModelPushButtonRNN)
        self.verticalLayout_9.addWidget(self.ModelsDbGroupBoxRNN)
        self.ModelSettingsGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.ModelSettingsGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 80))
        self.ModelSettingsGroupBoxRNN.setObjectName("ModelSettingsGroupBoxRNN")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.ModelSettingsGroupBoxRNN)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 20, 471, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OptimizerGroupBoxRNN = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.OptimizerGroupBoxRNN.setObjectName("OptimizerGroupBoxRNN")
        self.OptimizerComboBoxRNN = QtWidgets.QComboBox(self.OptimizerGroupBoxRNN)
        self.OptimizerComboBoxRNN.setGeometry(QtCore.QRect(10, 20, 210, 22))
        self.OptimizerComboBoxRNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OptimizerComboBoxRNN.setObjectName("OptimizerComboBoxRNN")
        self.gridLayout_2.addWidget(self.OptimizerGroupBoxRNN, 0, 0, 1, 1)
        self.ActivationGroupBoxRNN = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.ActivationGroupBoxRNN.setObjectName("ActivationGroupBoxRNN")
        self.ActivationComboBoxRNN = QtWidgets.QComboBox(self.ActivationGroupBoxRNN)
        self.ActivationComboBoxRNN.setGeometry(QtCore.QRect(10, 20, 210, 22))
        self.ActivationComboBoxRNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ActivationComboBoxRNN.setObjectName("ActivationComboBoxRNN")
        self.gridLayout_2.addWidget(self.ActivationGroupBoxRNN, 0, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.ModelSettingsGroupBoxRNN)
        self.ForecastingSettingsGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.ForecastingSettingsGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 270))
        self.ForecastingSettingsGroupBoxRNN.setObjectName("ForecastingSettingsGroupBoxRNN")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.ForecastingSettingsGroupBoxRNN)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QualitIndicatorGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.QualitIndicatorGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 45))
        self.QualitIndicatorGroupBoxRNN.setObjectName("QualitIndicatorGroupBoxRNN")
        self.QualitIndicatorComboBoxRNN = QtWidgets.QComboBox(self.QualitIndicatorGroupBoxRNN)
        self.QualitIndicatorComboBoxRNN.setGeometry(QtCore.QRect(10, 20, 451, 22))
        self.QualitIndicatorComboBoxRNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QualitIndicatorComboBoxRNN.setObjectName("QualitIndicatorComboBoxRNN")
        self.verticalLayout.addWidget(self.QualitIndicatorGroupBoxRNN)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.RelevantFeaturesGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.RelevantFeaturesGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 110))
        self.RelevantFeaturesGroupBoxRNN.setObjectName("RelevantFeaturesGroupBoxRNN")
        self.RelevantFeaturesRNN = QtWidgets.QListWidget(self.RelevantFeaturesGroupBoxRNN)
        self.RelevantFeaturesRNN.setGeometry(QtCore.QRect(8, 20, 451, 81))
        self.RelevantFeaturesRNN.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.RelevantFeaturesRNN.setObjectName("RelevantFeaturesRNN")
        self.gridLayout_17.addWidget(self.RelevantFeaturesGroupBoxRNN, 1, 0, 1, 1)
        self.TimeDiapazonRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.TimeDiapazonRNN.setMaximumSize(QtCore.QSize(600, 60))
        self.TimeDiapazonRNN.setObjectName("TimeDiapazonRNN")
        self.gridLayoutWidget_16 = QtWidgets.QWidget(self.TimeDiapazonRNN)
        self.gridLayoutWidget_16.setGeometry(QtCore.QRect(8, 14, 451, 41))
        self.gridLayoutWidget_16.setObjectName("gridLayoutWidget_16")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.StartDateLabelRNN = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.StartDateLabelRNN.setObjectName("StartDateLabelRNN")
        self.gridLayout_18.addWidget(self.StartDateLabelRNN, 1, 0, 1, 1)
        self.FromDateTimeRNN = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_16)
        self.FromDateTimeRNN.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FromDateTimeRNN.setObjectName("FromDateTimeRNN")
        self.gridLayout_18.addWidget(self.FromDateTimeRNN, 2, 0, 1, 1)
        self.EndDateLabelRNN = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.EndDateLabelRNN.setObjectName("EndDateLabelRNN")
        self.gridLayout_18.addWidget(self.EndDateLabelRNN, 1, 1, 1, 1)
        self.ToDateTimeRNN = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_16)
        self.ToDateTimeRNN.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ToDateTimeRNN.setObjectName("ToDateTimeRNN")
        self.gridLayout_18.addWidget(self.ToDateTimeRNN, 2, 1, 1, 1)
        self.gridLayout_17.addWidget(self.TimeDiapazonRNN, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_17)
        self.verticalLayout_9.addWidget(self.ForecastingSettingsGroupBoxRNN)
        self.LearnGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.LearnGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 50))
        self.LearnGroupBoxRNN.setObjectName("LearnGroupBoxRNN")
        self.gridLayoutWidget_17 = QtWidgets.QWidget(self.LearnGroupBoxRNN)
        self.gridLayoutWidget_17.setGeometry(QtCore.QRect(10, 20, 471, 25))
        self.gridLayoutWidget_17.setObjectName("gridLayoutWidget_17")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.LearnButtonRNN = QtWidgets.QPushButton(self.gridLayoutWidget_17)
        self.LearnButtonRNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LearnButtonRNN.setObjectName("LearnButtonRNN")
        self.gridLayout_19.addWidget(self.LearnButtonRNN, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.LearnGroupBoxRNN)
        self.ModelsValidationGroupBoxRNN = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.ModelsValidationGroupBoxRNN.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ModelsValidationGroupBoxRNN.setObjectName("ModelsValidationGroupBoxRNN")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ModelsValidationGroupBoxRNN)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 17, 471, 25))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.RocPushButtonRNN = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RocPushButtonRNN.setMaximumSize(QtCore.QSize(469, 16777215))
        self.RocPushButtonRNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RocPushButtonRNN.setObjectName("RocPushButtonRNN")
        self.gridLayout.addWidget(self.RocPushButtonRNN, 2, 1, 1, 1)
        self.AccuracyLabelRNN = QtWidgets.QLabel(self.gridLayoutWidget)
        self.AccuracyLabelRNN.setObjectName("AccuracyLabelRNN")
        self.gridLayout.addWidget(self.AccuracyLabelRNN, 2, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.ModelsValidationGroupBoxRNN)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(7, 14, 471, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ModelNameLineEditRNN = QtWidgets.QLineEdit(self.groupBox_2)
        self.ModelNameLineEditRNN.setGeometry(QtCore.QRect(12, 20, 291, 20))
        self.ModelNameLineEditRNN.setObjectName("ModelNameLineEditRNN")
        self.SaveModelPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.SaveModelPushButton.setGeometry(QtCore.QRect(319, 18, 150, 23))
        self.SaveModelPushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.SaveModelPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveModelPushButton.setObjectName("SaveModelPushButton")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.tabWidget_2.addTab(self.RNN_tab, "")
        self.verticalLayout_7.addWidget(self.tabWidget_2)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)

        self.retranslateUi(AdministratorWindow)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(AdministratorWindow)

    def retranslateUi(self, AdministratorWindow):
        _translate = QtCore.QCoreApplication.translate
        AdministratorWindow.setWindowTitle(_translate("AdministratorWindow", "AdministratorWindow"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.TSA_tab), _translate("AdministratorWindow", "Анализ временных рядов"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.MDC_tab), _translate("AdministratorWindow", "Сжатие данных"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.DBSCAN_tab), _translate("AdministratorWindow", "DBSCAN"))
        self.ModelsDbGroupBoxRNN.setTitle(_translate("AdministratorWindow", "База данных моделей"))
        self.DeleteModelPushButtonRNN.setText(_translate("AdministratorWindow", "Удалить выбранную модель"))
        self.ModelSettingsGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Синтез модели"))
        self.OptimizerGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Оптимизатор"))
        self.ActivationGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Функция активации"))
        self.ForecastingSettingsGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Настройки прогнозирования"))
        self.QualitIndicatorGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Прогнозируемый показатель качества"))
        self.RelevantFeaturesGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Выбор влияющих параметров производства"))
        self.TimeDiapazonRNN.setTitle(_translate("AdministratorWindow", "Выбор временного диапазона"))
        self.StartDateLabelRNN.setText(_translate("AdministratorWindow", "Начальная дата"))
        self.EndDateLabelRNN.setText(_translate("AdministratorWindow", "Конечная дата"))
        self.LearnGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Запуск вычислений"))
        self.LearnButtonRNN.setText(_translate("AdministratorWindow", "Обучить"))
        self.ModelsValidationGroupBoxRNN.setTitle(_translate("AdministratorWindow", "Верификация и сохранение модели"))
        self.RocPushButtonRNN.setText(_translate("AdministratorWindow", "ROC-кривая"))
        self.AccuracyLabelRNN.setText(_translate("AdministratorWindow", "Точность:"))
        self.groupBox.setTitle(_translate("AdministratorWindow", "Сохранение модели"))
        self.groupBox_2.setTitle(_translate("AdministratorWindow", "Наименование"))
        self.SaveModelPushButton.setText(_translate("AdministratorWindow", "Сохранить"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.RNN_tab), _translate("AdministratorWindow", "Прогнозирование качества"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdministratorWindow = QtWidgets.QWidget()
    ui = Ui_AdministratorWindow()
    ui.setupUi(AdministratorWindow)
    AdministratorWindow.show()
    sys.exit(app.exec_())
