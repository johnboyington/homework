from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QDialog, 
                             QVBoxLayout, QAction, QMessageBox, QFileDialog,
                             QSizePolicy, QComboBox)
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from numpy import sin, cos, tan, exp, pi
import numpy as np
import platform

import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        # Create the File menu
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.actionQuit = QAction("&Quit", self)
        self.actionQuit.triggered.connect(self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionQuit])
        
        # Create the Help menu
        self.menuHelp = self.menuBar().addMenu("&Help")
        self.actionAbout = QAction("&About",self)
        self.actionAbout.triggered.connect(self.about)
        self.menuHelp.addActions([self.actionAbout])
        
        # create the canvas
        self.plot = MatplotlibCanvas()
        
        # Setup main widget
        widget = QDialog()
        
        self.edit1 = QComboBox(self)
        self.edit1.addItem ('sin(x)')
        self.edit1.addItem ('x**5')
        self.edit1.addItem ('exp(-x)')
        self.edit1.addItem ('custom')
        self.edit2 = QLineEdit("np.linspace(-2*pi,2*pi,100)")
        self.edit3 = QLineEdit("output")
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)
        layout.addWidget(self.edit3)
        widget.setLayout(layout)
        
        self.x = np.arange(0.0, 3.0, 0.01)
        self.y = np.sin(2*np.pi*self.x)
        
        self.edit2.returnPressed.connect(self.evaluate_function)
        self.edit3.returnPressed.connect(self.evaluate_function)
        self.edit1.currentIndexChanged.connect(self.make_editable)
        self.actionSaveAs.triggered.connect(self.save_data)
        
        self.setCentralWidget(widget)
        
    
    def make_editable(self):
        if self.edit1.currentIndex() == 3: 
            self.edit1.setEditable(True)
        else:
            self.edit1.setEditable(False)
    
    def evaluate_function(self):
        fun = self.edit1.currentText()
        s = self.edit2.text()
        x_values = eval(str(s))
        print(type(x_values))
        if isinstance(x_values, tuple):
            y = []
            for x in x_values:
                fx = eval(fun)
                y.append(fx)
        else:
            x = x_values
            y = eval(fun)
        print(x, y)
        self.edit3.setText(str(y))
        self.plot.redraw(x_values, y)
        self.x, self.y = x_values, y
        # self.save_data(x, y)
    
    def update_plot(self):
        s = str(self.edit1.text())
        self.plot.redraw(s)
        
        
    def save_data(self):
        x, y = self.x, self.y
        s = 'x values:\n'
        for val in x:
            s += str(val) + ' '
        
        s += '\n f(x) values:\n'
        for val in y:
            s += str(val) + ' '
        
        with open('data.txt', 'w+') as f:
            f.write(s)
            
                
    def about(self) :
        QMessageBox.about(self, 
            "About Function Evaluator",
            """<b>Function Evaluator</b>
               <p>Copyright &copy; 2017 John Boyington, All Rights Reserved.
               <p>Python %s -- Qt %s -- PyQt %s on %s""" %
            (platform.python_version(),
             QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))


class MatplotlibCanvas(FigureCanvas) :
    """ This is borrowed heavily from the matplotlib documentation;
        specifically, see:
        http://matplotlib.org/examples/user_interfaces/embedding_in_qt5.html
    """
    def __init__(self):
        
        # Initialize the figure and axes
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        
        # Give it some default plot (if desired).  
        x = np.linspace(-2*pi,2*pi,100)
        y = np.sin(x)
        self.axes.plot(x, y)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y(x)')  
        self.axes.set_title('default title')
        
        # Now do the initialization of the super class
        FigureCanvas.__init__(self, self.fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
         
        
    def redraw(self, x, y) :
        """ Redraw the figure with new x and y values.
        """
        # clear the old image (axes.hold is deprecated)
        self.axes.clear()
        self.axes.plot(x, y)
        self.draw()    
        
    def set_title(self, s):
        self.axes.set_title(s)
        self.draw()
        
app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
app.exec_()

