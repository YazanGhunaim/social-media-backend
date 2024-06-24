"""add user table

Revision ID: 88dc61496d2f
Revises: df7c255a4535
Create Date: 2024-06-24 11:21:33.753684

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '88dc61496d2f'
down_revision = 'df7c255a4535'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"),
                              nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('users')
