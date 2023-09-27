# models/security_gate.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base  # Import the Base object
from .security_personnel import SecurityPersonnel


class SecurityGate(Base):
    __tablename__ = 'security_gate'

    id = Column(Integer, primary_key=True)  # Define the primary key column
    name = Column(String, index=True, unique=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    
    # Define the one-to-many relationship with Visitor
    visitors = relationship("Visitor", back_populates="gate")

      # Define the one-to-many relationship with SecurityPersonnel
    personnel = relationship("SecurityPersonnel", back_populates="gate")



