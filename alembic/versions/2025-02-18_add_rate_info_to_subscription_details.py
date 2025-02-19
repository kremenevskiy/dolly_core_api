"""add rate info to subscription_details

Revision ID: 9265cc576d99
Revises: bf2ca324465f
Create Date: 2025-02-18 21:04:45.849872

"""

from typing import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9265cc576d99'
down_revision: str | None = 'bf2ca324465f'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE subscriptions_details ADD COLUMN ru_description JSONB NULL;
    """)


def downgrade() -> None:
    op.execute("""
        ALTER TABLE subscriptions_details DROP COLUMN ru_description;
    """)
