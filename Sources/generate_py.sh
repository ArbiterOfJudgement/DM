#!/bin/bash
python -m PyQt5.uic.pyuic -x Main.ui -o "../View/MainWindow.py"
python -m PyQt5.uic.pyuic -x DataLoad.ui -o "../View/DataLoadWindow.py"
python -m PyQt5.uic.pyuic -x Administrator.ui -o "../View/AdministratorWindow.py"