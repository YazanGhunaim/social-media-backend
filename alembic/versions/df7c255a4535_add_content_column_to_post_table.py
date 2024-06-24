"""add content column to post table

Revision ID: df7c255a4535
Revises: c194f23386af
Create Date: 2024-06-24 11:17:18.460345

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'df7c255a4535'
down_revision = 'c194f23386af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("content", sa.String(), nullable=False),
                  )


def downgrade() -> None:
    op.drop_column('posts', 'content')
