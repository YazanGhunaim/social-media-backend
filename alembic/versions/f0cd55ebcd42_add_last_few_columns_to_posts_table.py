"""add last few columns to posts table

Revision ID: f0cd55ebcd42
Revises: b9c6e15dcb4c
Create Date: 2024-06-24 11:34:42.872919

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f0cd55ebcd42'
down_revision = 'b9c6e15dcb4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
