# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Controller.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_robot_connect = QtWidgets.QPushButton(self.centralwidget)
        self.cb_robot_connect.setGeometry(QtCore.QRect(20, 160, 151, 41))
        self.cb_robot_connect.setObjectName("cb_robot_connect")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 8, 341, 151))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_robot_info = DictView(self.groupBox)
        self.tableWidget_robot_info.setGeometry(QtCore.QRect(10, 20, 321, 121))
        self.tableWidget_robot_info.setObjectName("tableWidget_robot_info")
        self.tableWidget_robot_info.setColumnCount(0)
        self.tableWidget_robot_info.setRowCount(0)
        self.cb_extruder_connect = QtWidgets.QPushButton(self.centralwidget)
        self.cb_extruder_connect.setGeometry(QtCore.QRect(20, 397, 151, 41))
        self.cb_extruder_connect.setObjectName("cb_extruder_connect")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 341, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget_extruder_info = DictView(self.groupBox_2)
        self.tableWidget_extruder_info.setGeometry(QtCore.QRect(10, 20, 321, 141))
        self.tableWidget_extruder_info.setObjectName("tableWidget_extruder_info")
        self.tableWidget_extruder_info.setColumnCount(0)
        self.tableWidget_extruder_info.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 10, 741, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.text_code_view = QtWidgets.QTextEdit(self.groupBox_3)
        self.text_code_view.setGeometry(QtCore.QRect(5, 20, 731, 171))
        self.text_code_view.setObjectName("text_code_view")
        self.cb_robot_disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.cb_robot_disconnect.setGeometry(QtCore.QRect(190, 160, 151, 41))
        self.cb_robot_disconnect.setObjectName("cb_robot_disconnect")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 220, 331, 211))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gl_model_view = QtWidgets.QOpenGLWidget(self.groupBox_4)
        self.gl_model_view.setGeometry(QtCore.QRect(10, 20, 311, 181))
        self.gl_model_view.setObjectName("gl_model_view")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(730, 220, 391, 211))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gl_AR_view = QtWidgets.QOpenGLWidget(self.groupBox_5)
        self.gl_AR_view.setGeometry(QtCore.QRect(10, 20, 371, 181))
        self.gl_AR_view.setObjectName("gl_AR_view")
        self.cb_extruder_init = QtWidgets.QPushButton(self.centralwidget)
        self.cb_extruder_init.setGeometry(QtCore.QRect(190, 397, 151, 41))
        self.cb_extruder_init.setObjectName("cb_extruder_init")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 460, 341, 151))
        self.groupBox_6.setObjectName("groupBox_6")
        self.tableWidget_printer_info = DictView(self.groupBox_6)
        self.tableWidget_printer_info.setGeometry(QtCore.QRect(10, 20, 321, 121))
        self.tableWidget_printer_info.setObjectName("tableWidget_printer_info")
        self.tableWidget_printer_info.setColumnCount(0)
        self.tableWidget_printer_info.setRowCount(0)
        self.cb_stop = QtWidgets.QPushButton(self.centralwidget)
        self.cb_stop.setGeometry(QtCore.QRect(190, 620, 151, 41))
        self.cb_stop.setObjectName("cb_stop")
        self.cb_print = QtWidgets.QPushButton(self.centralwidget)
        self.cb_print.setGeometry(QtCore.QRect(20, 620, 151, 41))
        self.cb_print.setObjectName("cb_print")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(380, 440, 741, 231))
        self.groupBox_7.setObjectName("groupBox_7")
        self.text_console = QtWidgets.QPlainTextEdit(self.groupBox_7)
        self.text_console.setGeometry(QtCore.QRect(5, 70, 731, 151))
        self.text_console.setObjectName("text_console")
        self.cb_send_command = QtWidgets.QPushButton(self.groupBox_7)
        self.cb_send_command.setGeometry(QtCore.QRect(530, 28, 51, 31))
        self.cb_send_command.setObjectName("cb_send_command")
        self.comboBox_device = ComboAddress(self.groupBox_7)
        self.comboBox_device.setGeometry(QtCore.QRect(590, 27, 141, 31))
        self.comboBox_device.setObjectName("comboBox_device")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.text_send = QtWidgets.QLineEdit(self.groupBox_7)
        self.text_send.setGeometry(QtCore.QRect(6, 27, 521, 31))
        self.text_send.setObjectName("text_send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_system = QtWidgets.QMenu(self.menubar)
        self.menu_system.setObjectName("menu_system")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_connection_setting = QtWidgets.QAction(MainWindow)
        self.action_connection_setting.setObjectName("action_connection_setting")
        self.action_extruder_setting = QtWidgets.QAction(MainWindow)
        self.action_extruder_setting.setObjectName("action_extruder_setting")
        self.action_registration = QtWidgets.QAction(MainWindow)
        self.action_registration.setObjectName("action_registration")
        self.action_load_gcode = QtWidgets.QAction(MainWindow)
        self.action_load_gcode.setObjectName("action_load_gcode")
        self.action_load_path = QtWidgets.QAction(MainWindow)
        self.action_load_path.setObjectName("action_load_path")
        self.action_load_model = QtWidgets.QAction(MainWindow)
        self.action_load_model.setObjectName("action_load_model")
        self.action_load_config = QtWidgets.QAction(MainWindow)
        self.action_load_config.setObjectName("action_load_config")
        self.action_save_config = QtWidgets.QAction(MainWindow)
        self.action_save_config.setObjectName("action_save_config")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu_file.addAction(self.action_load_gcode)
        self.menu_file.addAction(self.action_load_path)
        self.menu_file.addAction(self.action_load_model)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_system.addAction(self.action_connection_setting)
        self.menu_system.addAction(self.action_extruder_setting)
        self.menu_system.addAction(self.action_registration)
        self.menu_system.addSeparator()
        self.menu_system.addAction(self.action_load_config)
        self.menu_system.addAction(self.action_save_config)
        self.menu_about.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_system.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FreeCAM多轴打印系统"))
        self.cb_robot_connect.setText(_translate("MainWindow", "连接测试"))
        self.groupBox.setTitle(_translate("MainWindow", "机械臂状态"))
        self.cb_extruder_connect.setText(_translate("MainWindow", "连接测试"))
        self.groupBox_2.setTitle(_translate("MainWindow", "挤出机状态"))
        self.groupBox_3.setTitle(_translate("MainWindow", "代码浏览"))
        self.cb_robot_disconnect.setText(_translate("MainWindow", "设置设备"))
        self.groupBox_4.setTitle(_translate("MainWindow", "模型预览"))
        self.groupBox_5.setTitle(_translate("MainWindow", "打印预览"))
        self.cb_extruder_init.setText(_translate("MainWindow", "设置设备"))
        self.groupBox_6.setTitle(_translate("MainWindow", "打印状态"))
        self.cb_stop.setText(_translate("MainWindow", "停止"))
        self.cb_print.setText(_translate("MainWindow", "打印"))
        self.groupBox_7.setTitle(_translate("MainWindow", "控制台"))
        self.cb_send_command.setText(_translate("MainWindow", "发送"))
        self.comboBox_device.setItemText(0, _translate("MainWindow", "COM3"))
        self.comboBox_device.setItemText(1, _translate("MainWindow", "COM4"))
        self.comboBox_device.setItemText(2, _translate("MainWindow", "192.168.1.2"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_system.setTitle(_translate("MainWindow", "系统"))
        self.menu_about.setTitle(_translate("MainWindow", "帮助"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_connection_setting.setText(_translate("MainWindow", "机械臂设置.."))
        self.action_extruder_setting.setText(_translate("MainWindow", "挤出机设置.."))
        self.action_registration.setText(_translate("MainWindow", "打印平面配准.."))
        self.action_registration.setShortcut(_translate("MainWindow", "Alt+R"))
        self.action_load_gcode.setText(_translate("MainWindow", "装入GCode.."))
        self.action_load_gcode.setShortcut(_translate("MainWindow", "Alt+G"))
        self.action_load_path.setText(_translate("MainWindow", "装入轨迹.."))
        self.action_load_path.setShortcut(_translate("MainWindow", "Alt+P"))
        self.action_load_model.setText(_translate("MainWindow", "装入模型.."))
        self.action_load_model.setShortcut(_translate("MainWindow", "Alt+M"))
        self.action_load_config.setText(_translate("MainWindow", "装入配置.."))
        self.action_load_config.setShortcut(_translate("MainWindow", "Alt+C"))
        self.action_save_config.setText(_translate("MainWindow", "保存配置.."))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_exit.setStatusTip(_translate("MainWindow", "退出程序"))
        self.action_exit.setShortcut(_translate("MainWindow", "Alt+Q"))

from ui.suWidgets import ComboAddress, DictView
