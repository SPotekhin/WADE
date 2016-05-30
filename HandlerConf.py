#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
from PyQt4.QtSql import *
import pyqtgraph as pg
import sqlalchemy as al
import sqlalchemy.orm as alo
import passlib.hash as pl
import sys
import ctypes

#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

try:
    myEngine = al.create_engine('postgres://postgres:1234@127.0.0.1/postgres',echo=0)

    con = myEngine.connect()

except:
    class ErrMessage(QWidget):
        def __init__(self):
            super(ErrMessage,self).__init__()
            QMessageBox.information( self,"Connection error...", "Не удалось подключиться к серверу")
            exit()

if __name__ == '__main__':
    app = QApplication([])
    errMess = ErrMessage()
    errMess.show()
    app.exec_()


#metadata = al.MetaData(con)

#ALSession = alo.sessionmaker(bind=con)

# metadata.create_all(con)

