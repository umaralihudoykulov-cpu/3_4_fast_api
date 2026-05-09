"""rename_content_to_body_in_posts

Revision ID: 595f5240ba07
Revises: 41fb7d16ce2b
Create Date: 2026-05-06 20:23:48.059971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '595f5240ba07'
down_revision: Union[str, Sequence[str], None] = '41fb7d16ce2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
