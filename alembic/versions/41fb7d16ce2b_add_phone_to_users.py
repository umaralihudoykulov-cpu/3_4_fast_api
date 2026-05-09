"""add_phone_to_users

Revision ID: 41fb7d16ce2b
Revises: 236a924c6a65
Create Date: 2026-05-06 20:17:36.793818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41fb7d16ce2b'
down_revision: Union[str, Sequence[str], None] = '236a924c6a65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'posts',
        'content',      # Eski nom
        new_column_name='body'   # Yangi nom
    )

def downgrade() -> None:
    op.alter_column(
        'posts',
        'body',
        new_column_name='content'
    )