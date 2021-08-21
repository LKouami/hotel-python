from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime
from sqlalchemy.orm import relationship


from .database import Base




class User(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")



class Item(Base):

    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

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
    client_type_id = Column(Integer, ForeignKey("type_client.id"))
    client = relationship("TypeClient", back_populates="type_clients")

    created_by = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, index=True, default= DateTime)

    modified_by = Column(Integer, ForeignKey("user.id"))
    modified_at = Column(DateTime, index=True, default= DateTime)

    deleted_by = Column(Integer, ForeignKey("user.id"))
    deleted_at = Column(DateTime, index=True, default= DateTime)


