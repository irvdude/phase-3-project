"""updated chore_name

Revision ID: 2c20dcb8f86d
Revises: 41f27099d2b3
Create Date: 2023-09-16 17:25:32.533930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2c20dcb8f86d"
down_revision: Union[str, None] = "41f27099d2b3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a new table with the desired schema
    op.create_table(
        "chores_temp",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("chore_name", sa.String(), nullable=True),
        sa.Column("priority", sa.String(), nullable=True),
        sa.Column("chore_id", sa.Integer(), sa.ForeignKey("person.id"), nullable=True),
    )

    # Copy data from the old table to the new table
    op.execute(
        "INSERT INTO chores_temp (id, chore_name, priority, chore_id) SELECT id, CAST(chore_name AS TEXT), priority, chore_id FROM chores"
    )

    # Delete the old table
    op.drop_table("chores")

    # Rename the new table to the old table's name
    op.rename_table("chores_temp", "chores")


def downgrade() -> None:
    # Create a new table with the old schema
    op.create_table(
        "chores_temp",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("chore_name", sa.Integer(), nullable=True),
        sa.Column("priority", sa.String(), nullable=True),
        sa.Column("chore_id", sa.Integer(), sa.ForeignKey("person.id"), nullable=True),
    )

    # Copy data from the old table to the new table
    op.execute(
        "INSERT INTO chores_temp (id, chore_name, priority, chore_id) SELECT id, CAST(chore_name AS INTEGER), priority, chore_id FROM chores"
    )

    # Delete the old table
    op.drop_table("chores")

    # Rename the new table to the old table's name
    op.rename_table("chores_temp", "chores")
