#!/usr/bin/env python
#-*- coding:utf-8 -*-
import csv
import sys
sys.path.append("..")

from PyQt5 import QtCore, QtGui, QtWidgets
from utils.suCAMData import CAMData, GCode
import numpy as np

class GcodeTableModelProxy(QtCore.QIdentityProxyModel):
    COLORS = [QtCore.Qt.white, QtCore.Qt.lightGray, QtCore.Qt.red]
    def calculate_color(self, model, row):
        line = str(model.index(row, 0).data())
        if 'G1' in line:
            return QtGui.QBrush(QtCore.Qt.white)
        if ';' in line:
            return QtGui.QBrush(QtCore.Qt.lightGray)
        if 'M140' in line:
            return QtGui.QBrush(QtCore.Qt.red)
        else:
            return QtGui.QBrush(QtCore.Qt.yellow)
        
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            sm = self.sourceModel()
            row = index.row()
            color = self.calculate_color(sm, row)
            if color is not None and color != index.data(QtCore.Qt.BackgroundRole):
                for i in range(sm.columnCount()):
                    sm.setData(sm.index(row, i), color, QtCore.Qt.BackgroundRole)   
                    
        return super(GcodeTableModelProxy, self).data(index, role)
            

class GcodeView(QtWidgets.QTableView):    
    def __init__(self, parent_widget=None):
        super(GcodeView, self).__init__(parent_widget)
        self.data = {}
        self.model = QtGui.QStandardItemModel()#QtGui.QStandardItemModel(self)
        
        self.proxy = GcodeTableModelProxy(self)
        self.proxy.setSourceModel(self.model) 
        self.setModel(self.proxy)
        
        self.horizontalHeader().hide()
        #self.verticalHeader().hide() 
        self.setAlternatingRowColors( True )
        
    
    def bind_data(self, filename):
        with open(filename, 'r') as reader:
            for line in reader:
                line = line.strip()
                items = [
                     QtGui.QStandardItem(line)                    
                ]
                self.model.appendRow(items)        
        
    def get_value(self):
        model = self.model()
        self.data = {}
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            key = str(model.data(index).toString())
            index = model.index(row, 1)
            value = model.data(index)
            self.data[key] = value   
            
        return self.data
        
    def set_value(self, key, value):
        self.data[key] = value
        self.bind_data(self.data)
        
    def changeColor(self, model):
        model.setData(model.index(1, 5), 1)
        model.setData(model.index(2, 5), 2)
        model.emit(QtCore.SIGNAL('dataChanged(QModelIndex,QModelIndex)'), model.index(1, 5), model.index(2, 5))    
        

class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = fileName

        self.model = QtGui.QStandardItemModel(self)

        #self.tableView = QtWidgets.QTableView(self)
        self.tableView = GcodeView()
        #self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushButtonLoad = QtWidgets.QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)

        self.pushButtonWrite = QtWidgets.QPushButton(self)
        self.pushButtonWrite.setText("Write Csv File!")
        self.pushButtonWrite.clicked.connect(self.on_pushButtonWrite_clicked)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)
        self.layoutVertical.addWidget(self.pushButtonWrite)

    def load_gcode(self, filename):
        with open(filename, 'r') as reader:
            for line in reader:
                items = [
                     QtGui.QStandardItem(line)                    
                ]
                self.model.appendRow(items)
    def write_gcode(self, filename):
        with open(filename, 'w') as writer:
            for row_number in range(self.model.rowCount()):
                pass
                
    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def writeCsv(self, fileName):
        with open(fileName, "w") as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)

    @QtCore.pyqtSlot()
    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        #self.loadCsv(self.fileName)
        #self.load_gcode(self.fileName)
        self.tableView.bind_data(self.fileName)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow("r:/data.csv")
    main.show()

    sys.exit(app.exec_())