import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://subsequent-yarn-5f0.notion.site/c5e9d49771134a319b132c9ff6e2f5b5?v=09e12e4d23554f86acf4db4353a34705"))

        self.setCentralWidget(self.browser)

        self.showMaximized()
        
    def close(self):
        self.close()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()
window.close()
