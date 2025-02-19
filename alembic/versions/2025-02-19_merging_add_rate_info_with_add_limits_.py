"""Merging add_rate_info with add_limits_constraint

Revision ID: f3b468219a0b
Revises: 9265cc576d99, c54fbf42caca
Create Date: 2025-02-19 02:28:42.997048

"""

from typing import Sequence

# revision identifiers, used by Alembic.
revision: str = 'f3b468219a0b'
down_revision: str | None = ('9265cc576d99', 'c54fbf42caca')
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
