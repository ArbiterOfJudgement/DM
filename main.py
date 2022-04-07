import sys

import pandas as pd
from pyqt_checkbox_list_widget import CheckBoxListWidget

import Model.Translation
from Model import TSAModule
import dbWorker

from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


from View.MainWindow import Ui_MainWindow
from View.DataLoadWindow import Ui_LoadDataWindow
from View.AdministratorWindow import Ui_AdministratorWindow

import numpy as np

app = QtWidgets.QApplication(sys.argv)

mainUI = Ui_MainWindow()
dataLoadUI = Ui_LoadDataWindow()
administratorUI = Ui_AdministratorWindow()

MainWindow = QtWidgets.QMainWindow()
DataLoadWindow = QtWidgets.QDialog()
AdministratorWindow = QtWidgets.QDialog()

dbw = dbWorker.dbWorker()
tsa = TSAModule.TSA()

def openMainWindow():
    mainUI.setupUi(MainWindow)
    initializeDates(mainUI)
    initializeActions(mainUI)
    initializeLists(mainUI)
    MainWindow.show()
def openDataLoadWindow():
    dataLoadUI.setupUi(DataLoadWindow)
    initializeDates(dataLoadUI)
    initializeActions(dataLoadUI)
    DataLoadWindow.exec_()
def openAdministratorWindow():
    administratorUI.setupUi(AdministratorWindow)
    initializeDates(administratorUI)
    initializeLists(administratorUI)
    initializeActions(administratorUI)
    AdministratorWindow.exec_()

def initializeDates(ui):
    if type(ui) == Ui_LoadDataWindow:
        dataLoadUI.FromDateTimeLOAD.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        dataLoadUI.ToDateTimeLOAD.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        dataLoadUI.FromDateTimeLOAD.setDateTime(datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S'))
        dataLoadUI.ToDateTimeLOAD.setDateTime(datetime.strptime(dbw.maxDate, '%Y-%m-%d %H:%M:%S'))
    if type(ui) == Ui_AdministratorWindow:
        ##RNN
        administratorUI.FromDateTimeRNN.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        administratorUI.ToDateTimeRNN.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        administratorUI.FromDateTimeRNN.setDateTime(datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S'))
        administratorUI.ToDateTimeRNN.setDateTime(datetime.strptime(dbw.maxDate, '%Y-%m-%d %H:%M:%S'))
    if type(ui) == Ui_MainWindow:
        ##RNN
        mainUI.FromDateTimeRNN.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        mainUI.ToDateTimeRNN.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        mainUI.FromDateTimeRNN.setDateTime(datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S'))
        mainUI.ToDateTimeRNN.setDateTime(datetime.strptime(dbw.maxDate, '%Y-%m-%d %H:%M:%S'))
        ##TSA
        mainUI.FromDateTimeTSA.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        mainUI.ToDateTimeTSA.setDisplayFormat('dd.MM.yyyy hh:mm:ss')
        mainUI.FromDateTimeTSA.setMinimumDateTime(datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S'))
        mainUI.ToDateTimeTSA.setMaximumDateTime(datetime.strptime(dbw.maxDate, '%Y-%m-%d %H:%M:%S'))
        mainUI.FromDateTimeTSA.setDateTime(datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S'))
        mainUI.ToDateTimeTSA.setDateTime(datetime.strptime(dbw.maxDate, '%Y-%m-%d %H:%M:%S'))

def initializeLists(ui):
    if type(ui) == Ui_AdministratorWindow:
        ##RNN
        administratorUI.OptimizerComboBoxRNN.addItems(dbw.optimizers.values())
        administratorUI.ActivationComboBoxRNN.addItems(dbw.activationFunctions.values())
        administratorUI.QualitIndicatorComboBoxRNN.addItems(dbw.getNames(dbw.ruNames, dbw.defects))
        administratorUI.RelevantFeaturesRNN.addItems(dbw.getNames(dbw.ruNames, dbw.features))
    if type(ui) == Ui_MainWindow:
        #
        mainUI.language_comboBox.currentIndexChanged.connect(langchange)
        ##RNN
        mainUI.FromDateTimeRNN.setDateTime(datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S'))
        ##TSA
        ParametersListTSA = CheckBoxListWidget()
        ParametersListTSA.addItems(dbw.getNames(dbw.ruNames, dbw.x))
        mainUI.gridLayout_5.addWidget(ParametersListTSA)

def langchange():
    if (mainUI.language_comboBox.currentIndex() == 0):
        mainUI.retranslateUi()
    else:
        Model.Translation.retranslateEngUI(mainUI)

def loadData():
    if validateDates(dataLoadUI.FromDateTimeLOAD, dataLoadUI.ToDateTimeLOAD):
        dbw.loadData(str(dataLoadUI.FromDateTimeLOAD.dateTime().toPyDateTime()), str(dataLoadUI.ToDateTimeLOAD.dateTime().toPyDateTime()))
        DataLoadWindow.close()

def validateDates(fromDT, toDT):
    enabledMin = datetime.strptime(dbw.minDate, '%Y-%m-%d %H:%M:%S')
    enabledMax = datetime.strptime(dbw.maxDate, '%Y-%m-%d %H:%M:%S')
    min = fromDT.dateTime().toPyDateTime()
    max = toDT.dateTime().toPyDateTime()
    if min < enabledMin:
        min = enabledMin
    if min > enabledMax:
        min = enabledMax
    if max < enabledMin:
        max = enabledMin
    if max > enabledMax:
        max = enabledMax
    if min == max:
        print("Start date time can't be equal finish! Select another interval and try again!")
        return False
    if min > max:
        tmp = min
        min = max
        max = tmp
        fromDT.setDateTime(datetime.strptime(str(min), '%Y-%m-%d %H:%M:%S'))
        toDT.setDateTime(datetime.strptime(str(max), '%Y-%m-%d %H:%M:%S'))
    return True


#TODO ADD ACTIONS
def initializeActions(ui):
    if type(ui) == Ui_LoadDataWindow:
        dataLoadUI.loadButton.clicked.connect(loadData)
    if type(ui) == Ui_AdministratorWindow:
        ##RNN
        administratorUI.SaveModelPushButton.clicked.connect(openAdministratorWindow)
        administratorUI.RocPushButtonRNN.clicked.connect(openAdministratorWindow)
        administratorUI.LearnButtonRNN.clicked.connect(openAdministratorWindow)
        administratorUI.DeleteModelPushButtonRNN.clicked.connect(openAdministratorWindow)
    if type(ui) == Ui_MainWindow:
        mainUI.administrator_button.clicked.connect(openAdministratorWindow)
        mainUI.language_comboBox.currentIndexChanged.connect(openAdministratorWindow)
        ##RNN
        mainUI.TrendsButtonRNN.clicked.connect(openAdministratorWindow)
        mainUI.StartButtonRNN.clicked.connect(openAdministratorWindow)
        mainUI.ModelComboBoxRNN.currentIndexChanged.connect(openAdministratorWindow)
        ##TSS
        mainUI.StartButtonTSA.clicked.connect(TimeSeriesAnalyser)


def TimeSeriesAnalyser():
    #items = mainUI.ParametersListTSA.selectedItems();
    timeseries = pd.DataFrame({'time': pd.Series(dbw.dates)})
    for items in dbw.x:
        timeseries[items] = items;
    tsa.TimeSeriesAnalyser(timeseries);


if __name__ == "__main__":
    openDataLoadWindow()
    if dbw.isDataLoaded:
        openMainWindow()
        sys.exit(app.exec_())
    else:
        sys.exit()