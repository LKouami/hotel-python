from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime, Float
from sqlalchemy.orm import relationship


from ..database import Base

class Space(Base):

    __tablename__ = "spaces"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    price = Column(Float, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    space_type_id = Column(Integer, ForeignKey("space_types.id"))
    space_state_id = Column(Integer, ForeignKey("space_states.id"))

    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, index=True, default= DateTime)
    modified_by = Column(Integer, ForeignKey("users.id"))
    modified_at = Column(DateTime, index=True, default= DateTime)
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, index=True, default= DateTime)