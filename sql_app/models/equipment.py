from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime, Float
from sqlalchemy.orm import relationship


from ..database import Base

class Equipment(Base):

    __tablename__ = "equipments"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, index=True)

    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, index=True, default= DateTime)
    modified_by = Column(Integer, ForeignKey("users.id"))
    modified_at = Column(DateTime, index=True, default= DateTime)
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, index=True, default= DateTime)