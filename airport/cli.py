import click
from sqlalchemy.orm import sessionmaker
from database import engine
from models.visitor import Visitor

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def add_visitor():
    """Add a new visitor."""
    try:
        # Interactive input or command-line arguments to get visitor information
        name = click.prompt("Visitor Name")
        passport_number = click.prompt("Passport Number")
        id_number = click.prompt("ID Number")
        telephone = click.prompt("Telephone")
        email = click.prompt("Email")

        # Create a new visitor instance and add it to the database
        visitor = Visitor(
            name=name,
            passport_number=passport_number,
            id_number=id_number,
            telephone=telephone,
            email=email,
        )
        session.add(visitor)
        session.commit()
        click.echo("Visitor added successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")

@cli.command()
def view_visitors():
    """View all visitors."""
    try:
        # Query and display all visitors
        visitors = session.query(Visitor).all()
        for visitor in visitors:
            click.echo(f"ID: {visitor.id}, Name: {visitor.name}, Passport: {visitor.passport_number}")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

@cli.command()
@click.argument("visitor_id", type=int)
def update_visitor(visitor_id):
    """Update a visitor's information."""
    try:
        # Query the visitor by ID
        visitor = session.query(Visitor).filter_by(id=visitor_id).first()
        if not visitor:
            click.echo("Visitor not found.")
            return

        # Interactive input or command-line arguments to get updated information
        name = click.prompt("Visitor Name", default=visitor.name)
        passport_number = click.prompt("Passport Number", default=visitor.passport_number)
        id_number = click.prompt("ID Number", default=visitor.id_number)
        telephone = click.prompt("Telephone", default=visitor.telephone)
        email = click.prompt("Email", default=visitor.email)

        # Update the visitor's information
        visitor.name = name
        visitor.passport_number = passport_number
        visitor.id_number = id_number
        visitor.telephone = telephone
        visitor.email = email

        session.commit()
        click.echo("Visitor updated successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")

@cli.command()
@click.argument("visitor_id", type=int)
def delete_visitor(visitor_id):
    """Delete a visitor."""
    try:
        # Query the visitor by ID
        visitor = session.query(Visitor).filter_by(id=visitor_id).first()
        if not visitor:
            click.echo("Visitor not found.")
            return

        # Confirm deletion
        confirmation = click.confirm(f"Delete visitor with ID {visitor.id} and Name {visitor.name}?")
        if confirmation:
            session.delete(visitor)
            session.commit()
            click.echo("Visitor deleted successfully.")
        else:
            click.echo("Deletion canceled.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")

if __name__ == "__main__":
    cli()
