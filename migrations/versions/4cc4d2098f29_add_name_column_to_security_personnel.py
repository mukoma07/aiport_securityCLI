"""Add name column to security_personnel

Revision ID: 4cc4d2098f29
Revises: edae00564c45
Create Date: 2023-09-16 11:24:23.096735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cc4d2098f29'
down_revision: Union[str, None] = 'edae00564c45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('security_personnel', sa.Column('name', sa.String(length=255), nullable=False))


def downgrade() -> None:
    op.drop_column('security_personnel', 'name')

