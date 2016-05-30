#(leaves out sqlalchemy & PyQt boilerplate, will not run)
#Define SQL Alchemy model
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4.QtCore import *
from sqlalchemy.orm import Session

from qvariantalchemy import String, Integer, Boolean
from sqlalchemy.ext.declarative import * #declarative_base

from sqlalchemy import *

Base = declarative_base()

class Entity(Base):
	__tablename__ = 'entities'

	ent_id = Column(Integer, primary_key=True)
	name = Column(String)
	enabled = Column(Boolean)
    
#create QTable Model/View
from alchemical_model import AlchemicalTableModel
model = AlchemicalTableModel(
    Session, #FIXME pass in sqlalchemy session object
    Entity, #sql alchemy mapped object
    [ # list of column 4-tuples(header, sqlalchemy column, column name, extra parameters as dict
      # if the sqlalchemy column object is Entity.name, then column name should probably be name,
      # Entity.name is what will be used when setting data, and sorting, 'name' will be used to retrieve the data.
        ('Entity Name', Entity.name, 'name', {'editable': True}),
        ('Enabled', Entity.enabled, 'enabled', {}),
    ])

table = QTableView()
table.setModel(model)