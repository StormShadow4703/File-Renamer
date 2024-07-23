'''Copy this file to the folder with files to be renamed 
then open the folder in VS code. Hit the run button and confirm
the path'''

import os
import sys
from pathlib import Path
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        currdir = os.path.dirname(os.path.realpath(sys.executable)) #__file__
        os.chdir(currdir)
        
        lis = os.listdir()
        
        #Add a title
        self.setWindowTitle("File Renamer")
        
        #Set layout
        self.setLayout(qtw.QVBoxLayout())
        
        #Create a label
        my_label = qtw.QLabel(f"Available files in {currdir}")
        my_label2 = qtw.QLabel(str(lis))
        self.layout().addWidget(my_label)
        self.layout().addWidget(my_label2)
        
        #Change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 10))
        
        #Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("Extension of file to rename")
        self.layout().addWidget(my_entry)
        
        #Create a button
        my_button = qtw.QPushButton("Rename!", clicked = lambda: press_it(lis, my_entry.text()))
        self.layout().addWidget(my_button)
        
        #Show the app
        self.show()
        
        def press_it(lis, exten):
            num = 1
            print(lis, exten)
            for i in lis:
                pth = os.path.join(os.getcwd(), i)
                
                file_extension = Path(pth).suffix
                
                if file_extension == exten:
                    os.rename(pth, f"{num}{exten}")
                    num += 1
            my_label.setText(f"Renamed all files with {exten}")
            my_label2.setText("")

app = qtw.QApplication([])
mw = MainWindow()

#Run the app
app.exec_()