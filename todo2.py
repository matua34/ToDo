from typing import Text
from warnings import simplefilter
from PyQt5 import QtWidgets
import sys
from pymongo import TEXT
from todo import Ui_TodoList
from PyQt5.QtGui import QIcon
from data import mycollection,mydb
from os import name, system
from time import sleep



class Myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Myapp,self).__init__()
        self.ui = Ui_TodoList()
        self.ui.setupUi(self)
        self.ui.submit.clicked.connect(self.clicked)
        self.ui.show_todos.clicked.connect(self.clicked)
        self.ui.clear.clicked.connect(self.clicked)
        self.ui.ToDo.stateChanged.connect(self.statues)
        self.ui.Done.stateChanged.connect(self.statues)
        self.ui.InProgres.stateChanged.connect(self.statues)

    def statues(self,value):
        cb = self.sender()

    def clicked(self):
        sender = self.sender().text()
        todo = self.ui.linetodo.text()
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        status =""

        for i in  items:
            if i.isChecked():
                status = i.text()

                if sender == "Submit":
                    todo = {"name":todo, "statues":status}
                    mycollection.insert_one(todo)
                    self.ui.list_todos.addItems([f"{status} durumlu görev eklendi."])

                elif sender == "Show Todos":
                    filter = {"statues":status,}
                    for i in  mycollection.find(filter):
                        self.ui.list_todos.addItems([i["name"]+"         "+i["statues"]])

        if sender == "Clear":
            self.ui.list_todos.clear()
            self.ui.linetodo.clear()


def app():
    app= QtWidgets.QApplication(sys.argv)
    win =Myapp()
    win.setWindowIcon(QIcon("todo_logo.gif"))
    win.setToolTip("My Todo App.")
    win.show()
    sys.exit(app.exec_())
app()
