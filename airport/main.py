import argparse
import sys
import os

# Add the project root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.security_gate import Base, SecurityGate
from models.visitor import Visitor
from models.security_personnel import SecurityPersonnel
from database import SessionLocal, initialize_database

def create_parser():
    parser = argparse.ArgumentParser(description="Airport Security Gate Management CLI")
    parser.add_argument("--add-visitor", action="store_true", help="Add a new visitor")
    parser.add_argument("--list-visitors", action="store_true", help="List all visitors")
    parser.add_argument("--update-visitor", type=int, help="Update visitor information by ID")
    parser.add_argument("--delete-visitor", type=int, help="Delete a visitor by ID")
    parser.add_argument("--search-visitor", type=str, help="Search for visitors by name or passport number")
    return parser

def initialize_and_populate_database():
    # Initialize the database
    initialize_database()
        # Create a database session using SessionLocal
    session = SessionLocal()

    # Create and add instances to the tables
    gate1 = SecurityGate(name="Gate 1", location="Terminal A")
    gate2 = SecurityGate(name="Gate 2", location="Terminal B")

    visitor1 = Visitor(
        name="Florence Nduta",
        passport_number="AB123456",
        id_number="5214780",
        telephone="0728030872",
        email="florencenduta@gmail.com",
        gate=gate1,
    )

    visitor2 = Visitor(
        name="Ann Mukuhi",
        passport_number="CD789012",
        id_number="6789063",
        telephone="0714988079",
        email="annmukuhi@gmail.com",
        gate=gate2,
    )

    visitor3 = Visitor(
        name="Bedan Mwathi",  # Add the name field
        passport_number="EF456789",
        id_number="29784741",
        telephone="0718999067",
        email="bedanmwathi@gmail.com",
        gate=gate1,
    )

    visitor4 = Visitor(
        name="Onesmus Muniu",  # Add the name field
        passport_number="GH123456",
        id_number="27162345",
        telephone="0717894885",
        email="onesmusmuniu@gmail.com",
        gate=gate2,
    )

    visitor5 = Visitor(
        name="James Kimani",  # Add the name field
        passport_number="IJ789012",
        id_number="45678908",
        telephone="0716323067",
        email="jameskimani@gmail.com",
        gate=gate1,
    ) 

    security_personnel1 = SecurityPersonnel(
        name="John Karanja",
        employee_id="SP123",
        role="Security Officer",
        gate=gate1,
    )
    security_personnel2 = SecurityPersonnel(
        name="Jane Wambui",
        employee_id="SP456",
        role="Security Officer",
        gate=gate2, 
   )


    # Add instances to the session
    session.add(gate1)
    session.add(gate2)
    session.add(visitor1)
    session.add(visitor2)
    
    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
    print("Database initialized and populated with initial data.")

def main():
    parser = create_parser()
    args = parser.parse_args()

      # Initialize the database before executing any Click commands
    initialize_and_populate_database()

    if args.add_visitor:
        # Implement logic to capture visitor information from the user and add a new visitor to the database
        pass
    elif args.list_visitors:
        # Query the database for a list of visitors and print the results
        session = SessionLocal()
        visitors = session.query(Visitor).all()
        for visitor in visitors:
            print(f"Visitor ID: {visitor.id}, Name: {visitor.name}, Passport: {visitor.passport_number}")
        session.close()
    # Handle other CLI commands
    else:
         print("No valid command provided.")

if __name__ == "__main__":
    main()
