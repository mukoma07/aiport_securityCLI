# models/security_personnel.py
from sqlalchemy import Column, Integer, String, ForeignKey  # Import ForeignKey
from sqlalchemy.orm import relationship
from  models.base import Base  # Import the Base object

class SecurityPersonnel(Base):
    __tablename__ = 'security_personnel'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    employee_id = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)  # Define the 'role' column
    gate_id = Column(Integer, ForeignKey('security_gate.id'))


    gate = relationship("SecurityGate", back_populates="personnel")
