from PyQt5.QtWidgets import QFrame, QWidget, QAction, QTableWidget, QTableWidgetItem, QHeaderView, QDialog
from ui.ui_plane_registration import *
import numpy as np
class DlgPlaneRegistration(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PlaneRegistrationDialog()
        self.ui.setupUi(self)
        self.setModal(True)     
        
        table_view = self.ui.table_widget_points
        #table_view.verticalHeader().hide()  
        #table_view.setColumnWidth(0, 40)
        for i in range(6):
            table_view.setColumnWidth(i, 100)
        header  = self.ui.table_widget_points.horizontalHeader()
        vheader = self.ui.table_widget_points.verticalHeader()
        header.setStyleSheet(
        "QHeaderView::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:white;"
            "padding:4px;"
        "}"
        "QTableCornerButton::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:white;"
        "}")
        vheader.setStyleSheet("QHeaderView::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:white;"
            "padding:4px;"
        "}")
        self.ui.table_widget_points.setHorizontalHeader(header)  
        
        table_view.setAlternatingRowColors( True )
        
        self.ui.pb_Add.clicked.connect(self.add_point)
        self.ui.pb_Del.clicked.connect(self.del_point)
        self.ui.pb_Clear.clicked.connect(self.clear_points)
        self.ui.pb_gen_translation.clicked.connect(self.gen_translation)
        self.ui.pb_OK.clicked.connect(self.OK)
        self.ui.pb_Cancel.clicked.connect(self.Cancel)
           
    def show(self):
        super(DlgPlaneRegistration, self).show()
        self.exec_()
        
    def add_point(self):
        #get point from self.controller
        Col = 6
        p = np.random.random(Col)  # x,y,z,rx,ry,rz
        
        table_view = self.ui.table_widget_points
        rows = table_view.rowCount()
        table_view.insertRow (rows)  
        
        
        new_row = p
        for col in range(Col):
            table_view.setItem(rows, col, QTableWidgetItem(str(new_row[col])));  
        
        table_view.scrollToBottom()
    
    def del_point(self):
        table_view = self.ui.table_widget_points
        selection = table_view.selectionModel().selectedRows()
        
        #Multiple rows can be selected
        selected_row = set(index.row() for index in table_view.selectedIndexes())
        for i in selected_row:        
            #index = selection.at(i)
            table_view.removeRow(i)
            self.message("row {} is deleted".format(i+1)) 
    
    def clear_points(self):
        self.ui.table_widget_points.setRowCount(0)
    
    def gen_translation(self):
        pass
    
    def OK(self):
        pass
    
    def Cancel(self):
        self.close()
    
    def set_controller(self, ctrl):
        self.controller = ctrl
        
    def message(self, msg):
        win = self.ui.planText_message
        win.appendPlainText(msg)
        
        
    
        