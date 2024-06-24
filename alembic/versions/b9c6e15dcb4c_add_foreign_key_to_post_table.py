"""add foreign key to post table

Revision ID: b9c6e15dcb4c
Revises: 88dc61496d2f
Create Date: 2024-06-24 11:29:00.514990

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b9c6e15dcb4c'
down_revision = '88dc61496d2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', 'posts')
    op.drop_column('posts', 'owner_id')
