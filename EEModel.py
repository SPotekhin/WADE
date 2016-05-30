#-*- coding=utf-8 -*-

from HandlerConf import *
from amodel import AlchemicalTableModel



class EEMWidget(QFrame):
    def __init__(self):
        super(QFrame,self).__init__()









if __name__ == '__main__':
    app = QApplication([])
    mw = EEMWidget()
    mw.show()
    #mw.showEntity()
    app.exec_()
