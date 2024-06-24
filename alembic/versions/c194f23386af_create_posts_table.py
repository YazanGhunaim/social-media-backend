"""create posts table

Revision ID: c194f23386af
Revises: 
Create Date: 2024-06-24 10:50:05.375482

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c194f23386af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('posts')
