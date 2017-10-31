from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QDialog, 
                             QVBoxLayout, QAction, QMessageBox)
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
import platform

import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        # Create the File menu
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.actionSaveAs.triggered.connect(self.saveas)
        self.actionQuit = QAction("&Quit", self)
        self.actionQuit.triggered.connect(self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionQuit])
        
        # Create the Help menu
        self.menuHelp = self.menuBar().addMenu("&Help")
        self.actionAbout = QAction("&About",self)
        self.actionAbout.triggered.connect(self.about)
        self.menuHelp.addActions([self.actionAbout])
        
        # Setup main widget
        widget = QDialog()
        self.edit1 = QLineEdit("function")
        self.edit2 = QLineEdit("value")
        self.edit3 = QLineEdit("output")
        layout = QVBoxLayout()
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)
        layout.addWidget(self.edit3)
        widget.setLayout(layout)
        
        self.edit1.returnPressed.connect(self.evaluate_function)
        
        self.setCentralWidget(widget)
    
    def evaluate_function(self):
        fun = str(self.edit1.text)
        print(fun)
        
        
    def saveas(self) :
        pass
                
    def about(self) :
        QMessageBox.about(self, 
            "About Function Evaluator",
            """<b>Function Evaluator</b>
               <p>Copyright &copy; 2017 John Boyington, All Rights Reserved.
               <p>Python %s -- Qt %s -- PyQt %s on %s""" %
            (platform.python_version(),
             QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
        
app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
app.exec_()

# TODO: RENAME AS .PYW INSTEAD OF .PY
