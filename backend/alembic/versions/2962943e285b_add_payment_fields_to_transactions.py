"""add payment fields to transactions

Revision ID: 2962943e285b
Revises: 4b8dba9e6b7f
Create Date: 2026-07-25 19:55:44.142846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2962943e285b'
down_revision: Union[str, Sequence[str], None] = '4b8dba9e6b7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
