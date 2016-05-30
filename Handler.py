#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------------
# Handler.py - main window for lounch programm
# version 0.0.0
# Start 25.03.2016
# autor PSV
#------------------------------------------------------------------------------------

# coding=UTF-8

from HandlerConf import *
from EntityEdit import *
from example1 import Examle1

MainUserName = ''

class loginDialog(QDialog):
    def __init__(self):

        super(loginDialog, self).__init__()
        self.setWindowIcon(QIcon('ico/lock-silver.ico'))
        loadUi('loginDialog.ui',self)
        self.loginOKbt.clicked.connect(self.checkLogin)
    def reject(self):
        QMessageBox.information(self,"Неудача!","До свидания...")
        exit()

    def checkLogin(self):
        logName = self.loginNamele.text()
        logPass = self.loginPassle.text()

        global MainUserName
        MainUserName = logName

        if logName == '':
            QMessageBox.information(self,"Empty logName","Введите имя...")
            return 1
        if logPass == '':
            QMessageBox.information(self,"Empty logPass","Введите пароль...")
            return 1

        sqlLine='select "UserName", "PassHash" from "Users" where "UserName" = :User'
        userRow=con.execute(al.text(sqlLine),User=logName)
        if userRow.rowcount == 0:
            QMessageBox.information(self,"Name not found!","Имя пользователя не найдено! Попробуйте ещё разок...")
            return 1
        for row in userRow:
            if pl.md5_crypt.verify(logPass,row.PassHash):
                MainUserName=logName
                self.accept()
                self.close()
            else:
                QMessageBox.information(self,"Wrong password!","Пароль не верен! Попробуйте ещё разок...")
                return 1



class HandlerClass(QMainWindow):
    def __init__(self):
        super(HandlerClass, self).__init__()

        self.height = 700
        self.width = 940
        self.setWindowIcon(QIcon('ico/wade.png'))
        #self.setMaximumHeight(768)
        #self.setMaximumWidth(1024)
        #self.mainLy = QGridLayout(self)
        self.resize(self.width,self.height)

        # tool bar
        self.toolBar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea,self.toolBar)
        self.toolBar.setAllowedAreas(Qt.LeftToolBarArea | Qt.TopToolBarArea)
        self.exitAction = QAction(QIcon('ico/exit.ico'), 'Exit', self)
        self.toolBar.addAction(self.exitAction)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(app.quit)
        self.toolBar.addSeparator()
        self.runAction = QAction(QIcon('ico/arrow-right-3.ico'), 'Выполнить', self)
        self.toolBar.addAction(self.runAction)
        self.runAction.triggered.connect(self.NoAction)
        self.checkAction = QAction(QIcon('ico/dialog-apply.ico'), 'Проверка', self)
        self.toolBar.addAction(self.checkAction)
        self.checkAction.triggered.connect(self.NoAction)
        self.filterAction = QAction(QIcon('ico/filter.ico'), 'Фильтр', self)
        self.toolBar.addAction(self.filterAction)
        self.filterAction.triggered.connect(self.NoAction)
        self.attAction = QAction(QIcon('ico/view-statistics.ico'), 'Статистика', self)
        self.toolBar.addAction(self.attAction)
        self.attAction.triggered.connect(self.NoAction)
        self.searchAction = QAction(QIcon('ico/search.png'), 'Поиск', self)
        self.toolBar.addAction(self.searchAction)
        self.searchAction.triggered.connect(self.NoAction)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.addUserActionTB = QAction(QIcon('ico/user-new-3.ico'),'Добавить пользователя',self)
        self.delUserActionTB = QAction(QIcon('ico/user-delete-2.ico'),'Удалить пользователя',self)
        self.cngPasswordActionTB = QAction(QIcon('ico/user-properties.ico'),'Сменить пароль',self)
        self.addUserActionTB.triggered.connect(self.AddUserSLOT)
        self.delUserActionTB.triggered.connect(self.DelUserSLOT)
        self.cngPasswordActionTB.triggered.connect(self.ChangePassSLOT)
        self.toolBar.addAction(self.addUserActionTB)
        self.toolBar.addAction(self.delUserActionTB)
        self.toolBar.addAction(self.cngPasswordActionTB)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.EEditTB = QAction('Редактор Entity',self)
        self.EEditTB.setIcon(QIcon('ico/entity.ico'))
        self.EEditTB.triggered.connect(self.EntityEditSLOT)
        self.toolBar.addAction(self.EEditTB)
        # end tool bar

        self.menuHandler = QMenuBar()
        self.setMenuBar(self.menuHandler)
        self.menuSet = QMenu('Настройки')


        self.AddUserAction = QAction('Добавить пользователя',self)
        self.AddUserAction.setIcon(QIcon('ico/user-new-3.ico'))
        self.AddUserAction.triggered.connect(self.AddUserSLOT)
        self.DelUserAction = QAction('Удалить пользователя',self)
        self.DelUserAction.setIcon(QIcon('ico/user-delete-2.ico'))
        self.DelUserAction.triggered.connect(self.DelUserSLOT)
        self.ChangePassAction = QAction('Сменить пароль',self)
        self.ChangePassAction.setIcon(QIcon('ico/user-properties.ico'))
        self.ChangePassAction.triggered.connect(self.ChangePassSLOT)
        self.menuHandler.addMenu(self.menuSet)
        self.menuSet.addAction(self.AddUserAction)
        self.menuSet.addAction(self.DelUserAction)
        self.menuSet.addAction(self.ChangePassAction)
        self.menuDo = QMenu('Операции')
        self.EEdit = QAction('Редактор Entity',self)
        self.EEdit.setIcon(QIcon('ico/entity.ico'))
        self.EEdit.triggered.connect(self.EntityEditSLOT)
        self.ActionSelect = QAction('Пример№1',self)
        self.ActionSelect.triggered.connect(self.ActionSelectSLOT)
        self.menuDo.addAction(self.EEdit)
        self.menuDo.addAction(self.ActionSelect)
        self.menuHandler.addMenu(self.menuDo)
        self.setWindowTitle('Обработчик')
        self.logDialog = loginDialog()
        self.logDialog.exec_()
        self.MainUserName = 'none'

    def NoAction(self):
        msgText = self.sender().text()
        msg = QMessageBox()
        msg.setText('Функция <<'+msgText+'>> не определена.')
        msg.setWindowTitle('Упс...')
        msg.setWindowIcon(QIcon('ico/face-sad.ico'))
        msg.setIcon(3)
        #msg.exec()
        return
    def ActionSelectSLOT(self):
        try:
            oldcw = self.centralWidget()
            oldcw.close()
        except:
            pass
        ex = Examle1()
        self.setCentralWidget(ex)
        ex.show()

    class AddUserDialog(QDialog):
        def __init__(self):
            super(QDialog,self).__init__()
            self.setWindowIcon(QIcon('ico/user-new-3.ico'))
            loadUi('AddUserDialog.ui',self)
            self.AUOKbt.clicked.connect(self.addUtoBD)
            self.NoAUbt.clicked.connect(self.reject)

        def addUtoBD(self):
            auName = self.AUNamele.text()
            auPass = self.AUPassle.text()
            if auName == '':
                QMessageBox.information(self,"Неудача!","Некого добавлять...")
                return
            if auPass == '':
                QMessageBox.information(self,"Неудача!","Без пароля нельзя...")
                return

            try:
                AUHashPass = pl.md5_crypt.encrypt(auPass)
                sqlLine = 'insert into "Users" ("UserName","PassHash") values (  :un,  :ph)'
                con.execute(al.text(sqlLine),{'un':auName,"ph":AUHashPass})
                QMessageBox.information(self,"User added!!",'Пользователь '+auName+' успешно добавлен!')
                self.accept()
                self.close()
            except:
                QMessageBox.information(self,"Error!!","Запись в базу не прошла, смотри log-file")
                print(sys.exc_info())
                self.close()

    def AddUserSLOT(self):
        AUDialog = self.AddUserDialog()
        AUDialog.exec_()

    class DelUserDialog(QDialog):
        def __init__(self):
            super(QDialog,self).__init__()
            self.setWindowIcon(QIcon('ico/user-delete-2.ico'))
            loadUi('DelUserDialog.ui',self)
            self.DUOKbt.clicked.connect(self.DUfromBD)
            self.NoDUbt.clicked.connect(self.reject)

        def DUfromBD(self):
            duName = self.DUNamele.text()

            if duName == MainUserName:
                QMessageBox.information(self,"Неудача!","Нельзя удалить самого себя...")
                return
            if duName == '':
                QMessageBox.information(self,"Неудача!","Некого удалять...")
                return

            Tran=con.begin()
            try:
                sqlLine= al.text('select "UserName" from "Users" where "UserName"=:un ')
                userRow=con.execute(sqlLine,{'un': duName})
                if userRow.rowcount == 0:
                    QMessageBox.information(self,"Неудача!","Нет такого пользователя...")
                    self.close()
                    return

                sqlLine = al.text('Delete from  "Users" where "UserName" = :un')

                con.execute(sqlLine,{'un':duName})
                QMessageBox.information(self,"User dropped!!",'Пользователь '+duName+' успешно удален!')
                self.accept()
                self.close()
                Tran.commit()
                return
            except:
                QMessageBox.information(self,"Error!!","Запись в базу не прошла, смотри log-file")
                print(sys.exc_info())
                self.reject()
                Tran.rollback()
                return

    def DelUserSLOT(self):
        DUDialog = self.DelUserDialog()
        DUDialog.exec_()

    class ChangePassDialog(QDialog):
        def __init__(self):
            super(QDialog,self).__init__()
            self.setWindowIcon(QIcon('ico/user-properties.ico'))
            loadUi('ChangePassDialog.ui',self)
            self.CPOKbt.clicked.connect(self.CPfromBD)
            self.NoCPbt.clicked.connect(self.reject)

        def CPfromBD(self):
            NewPass = self.NewPassle.text()
            NewHashPass = pl.md5_crypt.encrypt(NewPass)
            Tran=con.begin()
            try:
                sqlLine=al.text('update "Users" set "PassHash"= :ph where "UserName"=:un ')
                userRow=con.execute(sqlLine,{'un': MainUserName, 'ph':NewHashPass})
                Tran.commit()
                QMessageBox.information(self,"Password changed!","Пароль изменен!")
                self.accept()
                self.close()

                return
            except:
                QMessageBox.information(self,"Error!!","Запись в базу не прошла, смотри log-file")
                print(sys.exc_info())
                self.reject()
                Tran.rollback()
                return

    def ChangePassSLOT(self):
        CPDialog = self.ChangePassDialog()
        CPDialog.exec_()


    def EntityEditSLOT(self):
        try:
            oldcw = self.centralWidget()
            oldcw.show()
        except:
            pass
        EE = EEWidget()
        self.setCentralWidget(EE)
        EE.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet("QPushButton { background-color: lightblue }")
    mw = HandlerClass()
    mw.show()
    app.exec_()


