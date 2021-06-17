#username.py
from sqlalchemy import Column, Integer, String, ForeignKey
from DBManager import dbmanager

class UserNameModel(dbmanager.Base):
    __tablename__ = "UserName"

    ID_UserName = 
            Column(Integer, primary_key=True)
    ID_ServerSession = 
            Column(Integer, 
                   ForeignKey('ServerSession.ID_ServerSession'))
    HeroName = Column(String)
    ID_User = 
            Column(Integer, 
                   ForeignKey('UserNameBackup.ID_User'))