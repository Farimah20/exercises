#1_Window construction
#from PyQt5.QtWidgets import *
#import sys
#from time import sleep
#Creating the window class and its related settings
#class Window(QWidget):
#    def __init__(self):
#        QWidget.__init__(self)
#        self.resize(400,300)
#Run the program
#app=QApplication(sys.argv)
#screen=Window()
#screen.show()
#Change the length of the window after a 2 second delay
#sleep(2)
#screen.setMinimumWidth(800)
#The program will not end until the exit command is given and It returned an error
#sys.exit(app.exec_())

#2_Boxlayout
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.resize(500,500)
#         layout=QBoxLayout(QBoxLayout.LeftToRight)
#         self.setLayout(layout)
#         label=QLabel("hello world")
#         layout.addWidget(label,0,Qt.AlignCenter)
#         layout2=QBoxLayout(QBoxLayout.TopToBottom)
#         layout.addChildLayout(layout2)
#         #Widget definition
#         label=QLabel("hi")
#         layout2.addWidget(label)
#         label=QLabel("i am a program")
#         layout2.addWidget(label)
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#3_Gridlayout
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         label1=QLabel("label1 spanning 2 columns")
#         layout.addWidget(label1,0,0,0,2)
#         label2=QLabel("label2 spanning 2 rows")
#         layout.addWidget(label2,2,0,2,0)
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#4_label
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         label=QLabel("hello i am a program")
#         #It is placed inside the main label
#         layout.addWidget(label)
#         label.setIndent(10)
#         label.setIndent(50)
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#5_pushButton
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5 import QtGui
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,500)
#         button=QPushButton("Click ME")
#         layout.addWidget(button)
#         button.setIcon(QtGui.QIcon("gang.jpg"))
#         button.clicked.connect(self.buttonclicked)
#     def buttonclicked(self):
#         print("the pushbuton clicked")
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#6_Rediobutton
# from PyQt5.QtWidgets import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,500)
#         rb1=QRadioButton("python")
#         layout.addWidget(rb1)
#         rb1.toggled.connect(self.rb1clicked)
#         rb2=QRadioButton("java")
#         layout.addWidget(rb2)
#         rb2.toggled.connect(self.rb2clicked)
#     def rb1clicked(self):
#         #To read two radio buttons
#         rb1=self.sender()

#         if rb1.isChecked():
#             print("python selected")
#     def rb2clicked(self):
#         rb2=self.sender()
#         if rb2.isChecked():
#             print("java seleckted")
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#7_CheckBox
# from PyQt5.QtWidgets import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         self.cb1=QCheckBox("number 1")
#         self.cb1.setChecked(True)
#         layout.addWidget(self.cb1)
#         self.cb1.toggled.connect(self.checkbox)
#         self.cb2=QCheckBox("number 2")
#         layout.addWidget(self.cb2)
#         self.cb2.toggled.connect(self.checkbox)
#         self.cb2.setChecked(True)
#     def checkbox(self):
#         if self.cb1.isChecked():
#             print("checkbox1 checked")
#         if self.cb2.isChecked():
#             print("checkbox2 checked")
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#8_ToolTip
# from PyQt5.QtWidgets import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         button1=QPushButton("button1")
#         button2=QPushButton("button2")
#         button3=QPushButton("button3")
#         button1.setToolTip("Tooltip button1")
#         button2.setToolTip("Tooltip button2")
#         button3.setWhatsThis("WhatsThis button3")
#         layout.addWidget(button1,0,0)
#         layout.addWidget(button2,1,0)
#         layout.addWidget(button3,2,0)
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#9_ButtonGroup
# from PyQt5.QtWidgets import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         global button_group
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         button1=QPushButton("button1")
#         layout.addWidget(button1)
#         button2=QPushButton("button2")
#         layout.addWidget(button2)
#         button3=QPushButton("button3")
#         layout.addWidget(button3)
#         button_group=QButtonGroup()
#         #add and ID button
#         button_group.addButton(button1,1)
#         button_group.addButton(button2,2)
#         button_group.addButton(button3,3)
#         #Return the number of each button
#         button_group.buttonClicked[int].connect(self.on_button)
#     def on_button(self,id):
#         print("number %s clicked" %id)
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())

#10_GroupBox 
#11_SizeGrip
# from PyQt5.QtWidgets import *
# import sys
# class window(QWidget):
#     def __init__(self):
#         global button_group
#         QWidget.__init__(self)
#         layout=QGridLayout()
#         self.setLayout(layout)
#         self.resize(400,400)
#         box=QGroupBox("group box")
#         layout.addWidget(box)
#         box.setCheckable(True)
#         sublayout=QGridLayout()
#         box.setLayout(sublayout)
#         button1=QPushButton("button1")
#         sublayout.addWidget(button1)
#         button2=QPushButton("button2")
#         sublayout.addWidget(button2)
# app=QApplication(sys.argv)
# screen=window()
# screen.show()
# sys.exit(app.exec_())