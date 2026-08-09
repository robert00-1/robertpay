"""rename public key to publishable key

Revision ID: d3dae8ffc85c
Revises: c050e16f058d
Create Date: 2026-08-08 20:58:55.345090
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d3dae8ffc85c"
down_revision: Union[str, Sequence[str], None] = "c050e16f058d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rename public_key to publishable_key and add environment."""

    conn = op.get_bind()
    inspector = sa.inspect(conn)

    columns = {
        column["name"]
        for column in inspector.get_columns("api_keys")
    }

    # Rename public_key if it exists.
    if "public_key" in columns and "publishable_key" not in columns:
        op.alter_column(
            "api_keys",
            "public_key",
            new_column_name="publishable_key",
            existing_type=sa.String(length=255),
            existing_nullable=False,
        )

    # Add environment if it does not exist.
    if "environment" not in columns:
        op.add_column(
            "api_keys",
            sa.Column(
                "environment",
                sa.String(length=20),
                nullable=False,
                server_default="SANDBOX",
            ),
        )


def downgrade() -> None:
    """Reverse the migration."""

    conn = op.get_bind()
    inspector = sa.inspect(conn)

    columns = {
        column["name"]
        for column in inspector.get_columns("api_keys")
    }

    if "environment" in columns:
        op.drop_column("api_keys", "environment")

    if "publishable_key" in columns and "public_key" not in columns:
        op.alter_column(
            "api_keys",
            "publishable_key",
            new_column_name="public_key",
            existing_type=sa.String(length=255),
            existing_nullable=False,
        )