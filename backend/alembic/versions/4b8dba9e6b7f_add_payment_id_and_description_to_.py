"""add payment_id and description to transactions

Revision ID: 4b8dba9e6b7f
Revises: 7fb0200b519d
Create Date: 2026-07-25 19:44:31.451370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b8dba9e6b7f'
down_revision: Union[str, Sequence[str], None] = '7fb0200b519d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "transactions",
        sa.Column(
            "payment_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.add_column(
        "transactions",
        sa.Column(
            "description",
            sa.String(length=255),
            nullable=True,
        ),
    )

    op.create_foreign_key(
        "fk_transactions_payment_id",
        "transactions",
        "payments",
        ["payment_id"],
        ["id"],
    )
def downgrade() -> None:
    op.drop_constraint(
        "fk_transactions_payment_id",
        "transactions",
        type_="foreignkey",
    )

    op.drop_column("transactions", "description")
    op.drop_column("transactions", "payment_id")  