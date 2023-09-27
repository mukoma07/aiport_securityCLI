from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base # Import the Base object
from .security_gate import SecurityGate  # Import the related model

class Visitor(Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True) 
    name = Column(String, nullable=False)
    passport_number = Column(String, unique=True, nullable=False)
    id_number = Column(String, unique=True, nullable=False)
    telephone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    # Define the foreign key column
    gate_id = Column(Integer, ForeignKey('security_gate.id'))
    
    # Define the relationship to SecurityGate
    gate = relationship("SecurityGate", back_populates="visitors")



