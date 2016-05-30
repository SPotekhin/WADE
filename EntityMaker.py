# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EntityMaker.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(800, 556)
        Frame.setWindowTitle(_fromUtf8("Создание и редактирование сущностей"))
        Frame.setToolTip(_fromUtf8(""))
        Frame.setWhatsThis(_fromUtf8(""))
        Frame.setWindowFilePath(_fromUtf8(""))
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(Frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.EPTable = QtGui.QTableWidget(Frame)
        self.EPTable.setObjectName(_fromUtf8("EPTable"))
        self.EPTable.setColumnCount(0)
        self.EPTable.setRowCount(0)
        self.gridLayout_2.addWidget(self.EPTable, 0, 4, 1, 1)
        self.frame = QtGui.QFrame(Frame)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2.addWidget(self.frame, 0, 3, 1, 1)
        self.EEClosebt = QtGui.QPushButton(Frame)
        self.EEClosebt.setObjectName(_fromUtf8("EEClosebt"))
        self.gridLayout_2.addWidget(self.EEClosebt, 1, 4, 1, 1)
        self.SaveOKcb = QtGui.QCheckBox(Frame)
        self.SaveOKcb.setObjectName(_fromUtf8("SaveOKcb"))
        self.gridLayout_2.addWidget(self.SaveOKcb, 1, 2, 1, 1)
        self.ETable = QtGui.QTreeWidget(Frame)
        self.ETable.setObjectName(_fromUtf8("ETable"))
        self.ETable.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout_2.addWidget(self.ETable, 0, 2, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QObject.connect(self.EEClosebt, QtCore.SIGNAL(_fromUtf8("clicked()")), Frame.close)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.ETable, self.EPTable)
        Frame.setTabOrder(self.EPTable, self.SaveOKcb)
        Frame.setTabOrder(self.SaveOKcb, self.EEClosebt)

    def retranslateUi(self, Frame):
        self.EPTable.setToolTip(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt;\">Таблица свойств сущностей (EntityProp) </span></p></body></html>", None))
        self.EEClosebt.setToolTip(_translate("Frame", "Закрыть окно без сохранения изменений", None))
        self.EEClosebt.setText(_translate("Frame", "Закрыть", None))
        self.SaveOKcb.setText(_translate("Frame", "Сохранить изменения при выходе", None))
        self.ETable.setToolTip(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt;\">Окно дерева сущностей (Entity)</span></p><p><span style=\" font-size:8pt; font-style:italic;\"> (пока таблица, над деревом поработаем)</span></p></body></html>", None))

