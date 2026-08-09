"""create transactions table

Revision ID: 7fb0200b519d
Revises: 4662a5114992
Create Date: 2026-07-25 19:37:19.975574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fb0200b519d'
down_revision: Union[str, Sequence[str], None] = '4662a5114992'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
def upgrade():
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
        "fk_transactions_payment",
        "transactions",
        "payments",
        ["payment_id"],
        ["id"],
    )
def downgrade():
    op.drop_constraint(
        "fk_transactions_payment",
        "transactions",
        type_="foreignkey",
    )

    op.drop_column(
        "transactions",
        "payment_id",
    )

    op.drop_column(
        "transactions",
        "description",
    )    