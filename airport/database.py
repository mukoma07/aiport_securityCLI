from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base 

# Define the database URL.
DATABASE_URL = "sqlite:///security.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)


# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database():
    """Initialize the database by creating tables defined in the models."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_database()
    print("Database tables created.")
