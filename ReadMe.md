#### Description

FreeCAMΪ���ڻ�е�۹����Ķ����ӡ�ṩһ���򵥵����ʵ�ֿ�ܣ�ͨ����װ�ͺϲ������˿������ͼ������������Ĳ�����ʵ�ּ��������е�۵�ͬ�����ƺͲ��ԡ�

#### Framework

![img](Doc/images/ui.png)

* Device
  - Robot
  - Extruder


* CAMData
����з�װ��CAMDataģ�飬���GCode��ռ��ӡ·���滮����ת��������.



#### Coding Tips

* UI ���
```
pip install pyqt5-tools
design UI generate .ui file by [pythonpath]\Lib\site-packages\pyqt5-tools\designer.exe
compile rc and ui
  - pyrcc5 resource.qrc -o resource_rc.py
  - pyuic5 ./**.ui -o ui_**.py
```
��ƴ������װ���ɴ�����룬Ϊ����ui�����Ϣ��Ӧ������
```
class Viewer(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.controller = Controller(self)    # ѭ�����ã�ע���ͷ�
               
        #self.setupUi(self)
        #self._connect_signals()
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        Ui_MainWindow.setupUi(self,MainWindow)      
        ...
```

* 

#### Dependency