"""create_tables

Revision ID: edae00564c45
Revises: 3cad0415b7b7
Create Date: 2023-09-14 21:37:11.080304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edae00564c45'
down_revision: Union[str, None] = '3cad0415b7b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        # Define and create the 'security_gate' table
    op.create_table(
        'security_gate',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Define and create the 'visitor' table
    op.create_table(
        'visitor',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=255), nullable=False),
        sa.Column('last_name', sa.String(length=255), nullable=False),
        sa.Column('passport_number', sa.String(length=255), nullable=False),
        sa.Column('id_number', sa.String(length=255), nullable=False),
        sa.Column('telephone', sa.String(length=20), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('gate_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['gate_id'], ['security_gate.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Define and create the 'security_personnel' table
    op.create_table(
        'security_personnel',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),  # Add the 'name' column
        sa.Column('employee_id', sa.String(length=255), nullable=False),
        sa.Column('role', sa.String(length=255), nullable=False),
        sa.Column('gate_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['gate_id'], ['security_gate.id'], ),
        sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    pass
