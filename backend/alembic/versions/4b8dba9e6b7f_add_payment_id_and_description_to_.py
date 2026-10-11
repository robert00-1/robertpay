"""add payment_id and description to transactions

Revision ID: 4b8dba9e6b7f
Revises: 7fb0200b519d
Create Date: 2026-07-25 19:44:31.451370
"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "4b8dba9e6b7f"
down_revision: Union[str, Sequence[str], None] = "7fb0200b519d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # The previous migration already creates these columns
    # and their foreign key.
    pass


def downgrade() -> None:
    # The previous migration owns these database changes.
    pass
