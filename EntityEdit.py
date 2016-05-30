from HandlerConf import *

class EEWidget(QFrame):
    def __init__(self):
        super(QFrame,self).__init__()

        loadUi('EntityMaker.ui',self)

        self.FillETable()
        self.ETable.setCurrentCell(0,0)
        self.FillEPTable()
        self.ETable.cellPressed.connect(self.FillEPTable)
        #self.ETable.clicked.connect(self.FillEPTable())



    def FillETable(self):
        sqlLn = al.text('select * from "Entity"')
        resultEE = con.execute(sqlLn)
        self.ETable.setRowCount(resultEE.rowcount)
        self.ETable.setColumnCount(2)
        #self.ETable.setVerticalHeaderItem.hiden()
        self.ETable.setHorizontalHeaderLabels(['№','Сущность'])
        self.ETable.verticalHeader().hide()
        self.ETable.horizontalHeader().setResizeMode(QHeaderView.Stretch)

        #print(type(resultEE))
        i = 0
        for fe in list(resultEE):
        #print(f[4])
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(str(fe[5]))
            self.ETable.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsTristate | Qt.ItemIsDropEnabled)
            item.setText(fe[4])
            self.ETable.setItem(i, 1, item)
            i += 1

    def FillEPTable(self,EntityId=1):
        tx = self.ETable.currentItem().text()

        #print(help(self.ETable.currentItem))
        sqlLnP = al.text('select * from "EntityProp" where "EntityID"=:eid')
        resultEP = con.execute(sqlLnP,{"eid":tx})
        self.EPTable.setRowCount(resultEP.rowcount)
        self.EPTable.setColumnCount(2)
        #print(sqlLnP)
        j = 0
        for fp in list(resultEP):

            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(str(fp[3]))
            self.EPTable.setItem(j, 0, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(fp[1])
            self.EPTable.setItem(j, 1, item)
            j += 1