import sqlalchemy as al
import passlib.hash as pl
import sys

hashPass = pl.md5_crypt.encrypt('18401775')
userName = 'local'




myEngine = al.create_engine('postgres://postgres@192.168.32.150/wade') #, echo=True)

metadata = al.MetaData()

con = myEngine.connect()
users = al.Table('Users',metadata,autoload=True,autoload_with=myEngine)

ins = users.insert().values(UserName=userName, PassHash=hashPass)
try:
    con.execute(ins)
except:
    print( sys.exc_info()[1])

