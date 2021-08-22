from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime, Float
from sqlalchemy.orm import relationship


from ..database import Base

class Client(Base):

    __tablename__ = "clients"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    nationality = Column(String, index=True)
    email = Column(String, index=True)
    birthdate = Column(DateTime, index=True)
    residence = Column(String, index=True)
    phone = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    description = Column(String, index=True)
    client_type_id = Column(Integer, ForeignKey("client_types.id"))
    client = relationship("ClientType", back_populates="client_types")

    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, index=True, default= DateTime)
    modified_by = Column(Integer, ForeignKey("users.id"))
    modified_at = Column(DateTime, index=True, default= DateTime)
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, index=True, default= DateTime)

