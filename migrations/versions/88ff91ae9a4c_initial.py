"""initial

Revision ID: 88ff91ae9a4c
Revises: 
Create Date: 2023-09-13 06:39:29.362307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88ff91ae9a4c'
down_revision: Union[str, None] = None
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
        sa.Column('first_name', sa.String(length=255), nullable=False),
        sa.Column('last_name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###