from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime, Float
from sqlalchemy.orm import relationship


from ..database import Base

class SpaceType(Base):

    __tablename__ = "space_types"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, index=True, default= DateTime)
    modified_by = Column(Integer, ForeignKey("users.id"))
    modified_at = Column(DateTime, index=True, default= DateTime)
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, index=True, default= DateTime)