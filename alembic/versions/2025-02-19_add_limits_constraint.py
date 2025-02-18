"""add_limits_constraint

Revision ID: c54fbf42caca
Revises: bf2ca324465f
Create Date: 2025-02-19 00:07:26.208203

"""

from typing import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c54fbf42caca'
down_revision: str | None = 'bf2ca324465f'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("UPDATE user_subscriptions SET generation_photos_left = 0 where generation_photos_left < 0")

    op.execute("ALTER TABLE user_subscriptions ADD CONSTRAINT check_generations_photos_left CHECK (generation_photos_left >= 0)")

    pass


def downgrade() -> None:
    op.execute("ALTER TABLE user_subscriptions DROP CONSTRAINT check_generation_photos_left")

    pass
