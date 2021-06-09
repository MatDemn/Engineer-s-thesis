#serverSession.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from DBManager import dbmanager

class ServerSessionModel(dbmanager.Base):
    __tablename__ = "ServerSession"

    ID_ServerSession = Column(Integer, 
                              primary_key=True, 
                              autoincrement=True)
    ID_Server = Column(Integer)
    SessionShort = Column(String)
    ID_GM = Column(Integer)
    SoundBoardSwitch = Column(Boolean)

    UsersNames = relationship("UserNameModel", 
                              cascade="all,delete,delete-orphan")