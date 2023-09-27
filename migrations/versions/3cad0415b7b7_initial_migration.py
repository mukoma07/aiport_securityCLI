"""initial migration

Revision ID: 3cad0415b7b7
Revises: 88ff91ae9a4c
Create Date: 2023-09-14 21:29:30.254225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cad0415b7b7'
down_revision: Union[str, None] = '88ff91ae9a4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
