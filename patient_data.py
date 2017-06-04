# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:22:03 2017

@author: archan_d
"""
import json, sys, datetime, os
from csv import DictWriter
import tablib
from PyQt5 import QtCore, QtGui, QtWidgets, uic
file = None
try:
    with open('patients.json') as datafile:
        try:
            master = json.load(datafile)
        except ValueError:
            master = {}
            master['patients'] = []
        file = datafile
except(OSError, IOError, FileNotFoundError) as e:
    file = open('patients.json', 'x')
    master = {}
    master['patients'] = []
 
qtCreatorFile = "Patient_data_ui.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.addpatient.clicked.connect(self.addpatientf)
        self.opencsv.clicked.connect(self.opencsv)
    def opencsv(self):
        os.system("start /wait cmd /c patients.csv")
    def addpatientf(self):
        keys = ['ID', 'Name', 'Height_feet', 'Height_inches', 'Weight', 'DOB', 'Gender', 'Date of First Procedure']
        Patient = dict.fromkeys(keys)
        Patient['ID'] = int(self.ID.text())
        Patient['Height_feet'] = self.height_feet.value()
        Patient['Height_inches'] = self.height_inches.value()
        Patient['DOB'] = self.dob.date().toPyDate().isoformat()
        Patient['Date of First Procedure'] = self.dofp.date().toPyDate().isoformat()
        if(self.Male.isChecked()==True):
            Patient['Gender'] = "Male"
        elif(self.Female.isChecked() == True):
            Patient['Gender'] = "Female"
        elif(self.Other.isChecked() == True):
            Patient['Gender'] = "Other"
        Patient['Weight'] = self.weight.value()
        Patient['Name'] = self.name.text()
        master['patients'].append(Patient)
        with open('patients.json', 'w') as datafile:
            json.dump(master, datafile)
        with open('patients.csv','w') as outfile:
            writer = DictWriter(outfile, keys)
            writer.writeheader()
            writer.writerows(master['patients'])

 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


        
        
        