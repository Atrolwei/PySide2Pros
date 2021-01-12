import sys 
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtCore import QFile,Slot
from Ui_mainwindow1 import Ui_MainWindow
from PySide2.QtWebSockets import QWebSocket
from PySide2.QtNetwork import QAbstractSocket



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.testslot)
        # QAbstractSocket.connectToHost()
    
    @Slot()
    def testslot(self):
        print("hello")

if __name__ == "__main__":
    app=QApplication([])
    window=MainWindow()
    window.show()

    sys.exit(app.exec_())
