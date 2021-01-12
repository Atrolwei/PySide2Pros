import sys
from PySide2.QtCore import QLine 
from PySide2.QtWidgets import QApplication,QDialog,QLineEdit,QPushButton, QVBoxLayout

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("My Form")
        self.edit=QLineEdit("Write my name here..")
        self.button=QPushButton("Show Greetings")
        layout=QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        # To connect the function and the widget, use .connect and the function's "()" is omitted.
        self.button.clicked.connect(self.greetings)
    
    def greetings(self):
        # Use the .text() to get the text here.
        print("Hello {}".format(self.edit.text()))

if __name__ == "__main__":
    app=QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec_())