import subprocess

subprocess.call("pyuic5 Controller.ui -o ui_mainwindow.py")
subprocess.call("pyuic5 about.ui -o ui_about.py")
subprocess.call("pyuic5 plane_registration.ui -o ui_plane_registration.py")
subprocess.call("dir ui_*.py")